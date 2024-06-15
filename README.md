# FastAPI Reversed IP Application

## Overview

This FastAPI application receives requests and responds with the client's IP address reversed. It also stores the original and reversed IP addresses in an SQLite database.

## Features

- Retrieves the client's public IP address.
- Reverses the IP address (e.g., 1.2.3.4 becomes 4.3.2.1).
- Stores the reversed IP in a SQLite database.
- Displays the reversed IP on an HTML page using FastAPI's templating system.
- Containerized with Docker.
- Deployable to Kubernetes using Helm.
- Automated CI/CD pipeline using GitHub Actions.

## Prerequisites

- Python 3.8 or higher
- Docker
- Kubernetes Cluster
- Helm
- GCP (for cloud deployment)
- GitHub account (for CI/CD)

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com:aio-outlook/reverse-ip.git
cd reverse-ip

```

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

##  Running the Application Locally

```bash
uvicorn main:app --reload
```

## Docker Deployment

### 1. Build Docker Image

```bash
docker build -t your-docker-repo/reverse-ip:v1 .
```

### 2. Run Docker Container

```bash
docker run -d -p 8000:8000 your-docker-repo/reverse-ip:v1

```

### 3. Push Docker Image to Docker Hub

```bash
docker push your-docker-repo/reverse-ip:v1
```

## Kubernetes Deployment with Helm

### 1. Add Nginx Ingress Controller to Helm

```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install nginx-ingress ingress-nginx/ingress-nginx

```

### 2. Deploy the Application with Helm

```bash
helm dependency build helm-chart/fastapi-ip-reversal
helm install fastapi-ip-reversal helm-chart/fastapi-ip-reversal --namespace your-namespace

```

## Helm Chart Structure

```bash
helm-chart/
└── reverse-ip-app/
    ├── Chart.yaml
    ├── values.yaml
    ├── templates/
    │   ├── _helpers.tpl
    │   ├── deployment.yaml
    │   ├── service.yaml
    │   └── ingress.yaml
    └── charts/
```

## Chart.yaml

```bash
apiVersion: v2
name: reversed-ip-app
description: A Helm chart for deploying a FastAPI application that reverses IP addresses

# A chart can be either an 'application' or a 'library' chart.
#
# Application charts are a collection of templates that can be packaged into versioned archives
# to be deployed.
#
# Library charts provide useful utilities or functions for the chart developer. They're included as
# a dependency of application charts to inject those utilities and functions into the rendering
# pipeline. Library charts do not define any templates and therefore cannot be deployed.
type: application

# This is the chart version. This version number should be incremented each time you make changes
# to the chart and its templates, including the app version.
# Versions are expected to follow Semantic Versioning (https://semver.org/)
version: 0.1.0

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "1.0.0"

dependencies:
  - name: ingress-nginx
    version: "4.0.3"
    repository: "https://kubernetes.github.io/ingress-nginx"

```

## Temporary Application URL

```bash
https://reverseip.motoyakouture.org/

 curl http://reverseip.motoyakouture.org/

```