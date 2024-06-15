# FastAPI Reversed IP Application

## Overview

This FastAPI application receives requests and responds with the client's IP address reversed. It also stores the original and reversed IP addresses in an SQLite database.

## Features

- Reverse the IP address of the requester.
- Store the original and reversed IP addresses in a database.
- Serve the reversed IP address on an HTML page.
- Deployable via Docker and Kubernetes using Helm.

## Prerequisites

- Python 3.8 or higher
- Docker
- Kubernetes
- Helm

## Setup and Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>

# Install Dependencies

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

#  Run the Application
uvicorn main:app --host 0.0.0.0 --port 8000
