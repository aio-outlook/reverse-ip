from typing import Optional
from fastapi import FastAPI, Request, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.templating import Jinja2Templates
import logging
from starlette_context import middleware, plugins
from starlette_context import context
# SQLAlchemy setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./reversed_ips.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define a SQLAlchemy model for reversed IPs
class ReversedIP(Base):
    __tablename__ = "reversed_ips"

    id = Column(Integer, primary_key=True, index=True)
    original_ip = Column(String, unique=True, index=True)
    reversed_ip = Column(String, index=True)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Jinja2 templates setup
templates = Jinja2Templates(directory="templates")

# FastAPI app instance
app = FastAPI()

app.add_middleware(
    middleware.ContextMiddleware,
    plugins=(
        plugins.ForwardedForPlugin(),
    ),
)

# Function to reverse an IP address
def reverse_ip(ip: str) -> str:
    return '.'.join(ip.split('.')[::-1])

# Pydantic model for response
class ReversedIPResponse(BaseModel):
    reversed_ip: str

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_first_ip(ip_list: str) -> str:
    """
    Splits the input string by commas and returns the first IP address.
    
    :param ip_list: A string containing multiple IP addresses separated by commas.
    :return: The first IP address.
    """
    ip_addresses = ip_list.split(',')
    return ip_addresses[0].strip() if ip_addresses else None


# FastAPI endpoint to store reversed IP in database
@app.get("/", response_model=ReversedIPResponse)
async def store_reversed_origin_ip(request: Request, db: Session = Depends(get_db)):
    ip_list = context.data["X-Forwarded-For"] or request.client.host  # Get client's IP address
    
    client_ip = get_first_ip(ip_list)
    
    logging.error(client_ip)
    
    if client_ip is None:
        raise HTTPException(status_code=400, detail="Cannot retrieve client IP")

    reversed_ip = reverse_ip(client_ip)

    try:
        # Check if the IP is already stored
        db_ip = db.query(ReversedIP).filter(ReversedIP.original_ip == client_ip).first()
        
        if db_ip is None:
            # Create a new record in the database
            db_record = ReversedIP(original_ip=client_ip, reversed_ip=reversed_ip)
            db.add(db_record)
            db.commit()
            db.refresh(db_record)
            
    except Exception as e:
        logging.error(f"Error storing reversed IP: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

    return templates.TemplateResponse("index.html", {"request": request, "reversed_ip": reversed_ip})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
