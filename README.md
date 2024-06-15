# FastAPI Reversed IP Application

## Overview

This FastAPI application receives requests and responds with the client's IP address reversed. It also stores the original and reversed IP addresses in an SQLite database.

## Features

- Retrieves the client's public IP address.
- Reverses the IP address (e.g., 1.2.3.4 becomes 4.3.2.1).
- Stores the reversed IP in a SQLite database.
- Displays the reversed IP on an HTML page using FastAPI's templating system.

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
```

## Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

##  Running the Application Locally

```bash
uvicorn main:app --reload
```

