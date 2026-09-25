\# CloudDeploy Sentinel



A production-style CI/CD learning project built around a Python Flask application.



CloudDeploy Sentinel demonstrates an end-to-end DevOps workflow using GitHub, Jenkins, Docker, Docker Hub, Trivy, automated health checks, deployment validation, and automatic rollback.



\---



\## Overview



CloudDeploy Sentinel is a hands-on DevOps portfolio project designed to demonstrate practical CI/CD concepts.



The project starts with a Python Flask application and builds an automated CI/CD workflow around it.



The current V1 pipeline performs:



\- Source code checkout from GitHub

\- Python virtual environment setup

\- Dependency installation

\- Code linting with Flake8

\- Automated testing with Pytest

\- Docker image creation

\- Container health validation

\- Security scanning with Trivy

\- Docker image publishing to Docker Hub

\- Automated deployment

\- Deployment health validation

\- Last-known-good version tracking

\- Automatic rollback when deployment health checks fail



\---



\## Architecture



```text

&#x20;                   ┌─────────────────┐

&#x20;                   │     GitHub      │

&#x20;                   │  Source Code    │

&#x20;                   └────────┬────────┘

&#x20;                            │

&#x20;                            ▼

&#x20;                   ┌─────────────────┐

&#x20;                   │     Jenkins     │

&#x20;                   │   CI/CD Engine  │

&#x20;                   └────────┬────────┘

&#x20;                            │

&#x20;            ┌───────────────┼───────────────┐

&#x20;            │               │               │

&#x20;            ▼               ▼               ▼

&#x20;       ┌─────────┐     ┌─────────┐    ┌─────────┐

&#x20;       │ Flake8  │     │ Pytest  │    │  Docker │

&#x20;       │  Lint   │     │  Tests  │    │  Build  │

&#x20;       └─────────┘     └─────────┘    └────┬────┘

&#x20;                                            │

&#x20;                                            ▼

&#x20;                                     ┌─────────────┐

&#x20;                                     │    Trivy    │

&#x20;                                     │Security Scan│

&#x20;                                     └──────┬──────┘

&#x20;                                            │

&#x20;                                            ▼

&#x20;                                     ┌─────────────┐

&#x20;                                     │ Docker Hub  │

&#x20;                                     │   Registry  │

&#x20;                                     └──────┬──────┘

&#x20;                                            │

&#x20;                                            ▼

&#x20;                                     ┌─────────────┐

&#x20;                                     │ Deployment  │

&#x20;                                     └──────┬──────┘

&#x20;                                            │

&#x20;                                            ▼

&#x20;                                     ┌─────────────┐

&#x20;                                     │ Health Check│

&#x20;                                     │   /health   │

&#x20;                                     └──────┬──────┘

&#x20;                                            │

&#x20;                             ┌──────────────┴──────────────┐

&#x20;                             │                             │

&#x20;                             ▼                             ▼

&#x20;                        ┌─────────┐                 ┌────────────┐

&#x20;                        │ SUCCESS │                 │  FAILURE   │

&#x20;                        └────┬────┘                 └─────┬──────┘

&#x20;                             │                            │

&#x20;                             ▼                            ▼

&#x20;                      Record Last-Good              Automatic

&#x20;                          Version                    Rollback

&#x20;                                                          │

&#x20;                                                          ▼

&#x20;                                                  Last Known Good

&#x20;                                                     Version

\## Technology Stack



| Component          | Technology                 |

| ------------------ | -------------------------- |

| Application        | Python / Flask             |

| Source Control     | Git / GitHub               |

| CI/CD              | Jenkins                    |

| Containerization   | Docker                     |

| Container Registry | Docker Hub                 |

| Code Quality       | Flake8                     |

| Testing            | Pytest                     |

| Security Scanning  | Trivy                      |

| Health Check       | HTTP `/health` endpoint    |

| Deployment         | Docker                     |

| Rollback           | Jenkins automated rollback |





\## Project Structure:-



clouddeploy-sentinel/

│

├── app/

│   ├── \_\_init\_\_.py

│   └── routes.py

│

├── static/

│

├── templates/

│

├── tests/

│   └── test\_health.py

│

├── .dockerignore

├── .gitignore

├── Dockerfile

├── Jenkinsfile

├── pytest.ini

├── requirement.txt

├── run.py

└── README.md







**CI Pipeline**



The Jenkins pipeline validates the application before deployment.



**1. Checkout**



Jenkins checks out the application source code from GitHub.



**2. Environment Check**



The pipeline verifies the available Python and Docker environment.



**3. Create Virtual Environment**



A Python virtual environment is created for the CI process.



**4. Install Dependencies**



Application dependencies are installed from requirement.txt.



**5. Lint**



Flake8 checks the Python source code for coding and formatting issues.



**6. Test**



Pytest executes the automated test suite.



The pipeline stops if linting or tests fail.







**## Docker Containerization**



After the application passes the CI checks, Jenkins builds a Docker image.



Images are tagged using the Jenkins build number.



**Example:**



clouddeploy-sentinel:3

clouddeploy-sentinel:4

clouddeploy-sentinel:5



Version-specific image tags make it possible to identify a particular application version and support rollback.









**Container Health Check**



The application exposes a health endpoint:



**/health**



The pipeline starts the container and verifies that the application becomes healthy before continuing.



Example response:



{

&#x20; "service": "CloudDeploy Sentinel",

&#x20; "status": "healthy"

}





**Security Scanning**



Trivy scans the Docker image for vulnerabilities.



The pipeline performs the security scan before publishing the image to Docker Hub.



A JSON security report is generated and archived by Jenkins.



**Docker Hub**



Successfully validated Docker images are published to Docker Hub.



Docker Hub repository:



yadavpradeep22/clouddeploy-sentinel





**The pipeline publishes:**



Build-number versioned images

latest image



Example:



yadavpradeep22/clouddeploy-sentinel:3

yadavpradeep22/clouddeploy-sentinel:latest





**## Continuous Deployment**



After the image is published, Jenkins performs the deployment step.



The deployment process:



Reads the previously recorded last-known-good version.

Pulls the new image from Docker Hub.

Starts the new application container.

Waits for application startup.

Performs an HTTP health check.

Records the new version as the last-known-good version if the health check succeeds.

Automatic Rollback



CloudDeploy Sentinel includes an automatic rollback mechanism.



The pipeline stores the last successful deployment version in a persistent deployment-state location.



C:\\jenkins-agent\\deployment-state\\

└── clouddeploy-sentinel-last-good.txt



If the newly deployed version fails its health check:



New Deployment

&#x20;     │

&#x20;     ▼

Health Check

&#x20;     │

&#x20;     ▼

&#x20;   FAILED

&#x20;     │

&#x20;     ▼

Remove Failed Version

&#x20;     │

&#x20;     ▼

Pull Last Known Good

&#x20;     │

&#x20;     ▼

Start Previous Version

&#x20;     │

&#x20;     ▼

Health Check

&#x20;     │

&#x20;     ▼

Rollback Successful



The pipeline intentionally marks the deployment build as failed even when rollback succeeds.



This provides a clear operational distinction:



The new deployment failed.

Recovery succeeded.

Failure Recovery Test



The automatic rollback mechanism was tested by intentionally changing the deployment health-check endpoint to a non-existent endpoint.



The new deployment returned HTTP **404**.



Jenkins detected the failed deployment, removed the failed container, restored the previous known-good image, and verified that the restored application returned a healthy response.



This validated the failure detection and automatic rollback workflow.



**## Local Setup**

Prerequisites

Python

Git

Docker Desktop

Jenkins

Clone the Repository

git clone https://github.com/yadavpradeep22/clouddeploy-sentinel.git

cd clouddeploy-sentinel

Create a Virtual Environment



Windows PowerShell:



python -m venv .venv



Activate it:



.\\.venv\\Scripts\\Activate.ps1

Install Dependencies

pip install -r requirement.txt

Run the Application

python run.py

Run Tests Locally

pytest



Expected result:



1 passed

Run Lint Locally

flake8 app tests run.py



A clean execution produces no lint errors.



Build Docker Image Locally

docker build -t clouddeploy-sentinel:local .



Run the container:



docker run -d -p 5001:5000 --name clouddeploy-sentinel clouddeploy-sentinel:local



Test the health endpoint:



curl.exe http://localhost:5001/health

Jenkins Pipeline



The CI/CD pipeline is defined using a Jenkinsfile.



The pipeline currently follows this flow:



Checkout

&#x20;  ↓

Environment Check

&#x20;  ↓

Create Virtual Environment

&#x20;  ↓

Install Dependencies

&#x20;  ↓

Lint

&#x20;  ↓

Test

&#x20;  ↓

Docker Build

&#x20;  ↓

Docker Image Check

&#x20;  ↓

Docker Run \& Health Check

&#x20;  ↓

Trivy Security Scan

&#x20;  ↓

Archive Security Report

&#x20;  ↓

Docker Hub Push

&#x20;  ↓

CD Deployment

&#x20;  ↓

Health Validation

&#x20;  ↓

Record Successful Deployment



If deployment validation fails:



CD Deployment

&#x20;     ↓

Health Check FAILED

&#x20;     ↓

Automatic Rollback

&#x20;     ↓

Restore Last Known Good Version

&#x20;     ↓

Rollback Health Check





**Current V1 Capabilities**

Flask application

GitHub source control

Jenkins CI/CD

Automated linting

Automated testing

Docker containerization

Docker health validation

Trivy vulnerability scanning

Docker Hub image publishing

Automated deployment

Last-known-good version tracking

Automatic rollback

Jenkins build artifacts and reports



Future Roadmap

**V2 — Cloud Deployment**

AWS-based deployment

Cloud infrastructure

Remote deployment target

Environment separation



**V3 — Infrastructure \& Orchestration**

Terraform

Kubernetes

Container orchestration

Deployment strategies



**V4 — Observability**

Monitoring

Centralized logging

Metrics

Alerting

Production-grade security improvements



**V5 — Advanced CI/CD**

Blue/Green deployments

Canary deployments

Advanced rollback strategies

GitHub Actions comparison

Production-style cloud architecture

Learning Goals





CloudDeploy Sentinel is also a hands-on DevOps learning project.



The project is designed to build practical understanding of:



CI/CD

Jenkins pipelines

Docker

Container lifecycle

Docker image registries

Automated testing

Code quality

Container security

Deployment validation

Failure handling

Rollback strategies

DevOps automation

Author



Pradeep Yadav

