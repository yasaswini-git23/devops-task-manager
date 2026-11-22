# devops-task-manager
# DevOps Task Manager
### Containerized Flask Application | CI/CD | AWS EC2
# DevOps Task Manager
### Containerized Flask Application | CI/CD | AWS EC2


A containerized task management application built with Python Flask and delivered through an automated CI/CD pipeline using GitHub Actions, Docker, Docker Hub, and AWS EC2.


## Overview


This project demonstrates an end-to-end application delivery workflow, covering source-code management, automated testing, containerization, image publishing, and cloud deployment.


The application is packaged as a Docker image and deployed on an AWS EC2 virtual machine. GitHub Actions automates the testing, Docker image build, and publishing stages whenever code is pushed to the main branch.


## Architecture
text
                 Developer
                     |
                     v
              GitHub Repository
                     |
                     v
              GitHub Actions
                     |
              +------+------+
              |             |
              v             v
         Build & Test    Docker Build
              |             |
              v             v
            Pytest       Docker Image
                            |
                            v
                        Docker Hub
                            |
                            v
                         AWS EC2
                            |
                            v
                     Docker Container
                            |
                            v
                     Flask Application


## Technology Stack


| Area | Technology |
|---|---|
| Application | Python, Flask |
| Testing | Pytest |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Container Registry | Docker Hub |
| Cloud Platform | AWS |
| Compute | Amazon EC2 |
| Operating System | Amazon Linux |


## Application Features


Create and manage tasks through a web interface.
View tasks in the application.
Mark tasks as completed.
Check application availability through a health endpoint.
### Application Endpoints


| Endpoint | Method | Purpose |
|---|---|---|
| / | GET | Displays the application interface |
| /tasks | POST | Creates a task |
| /tasks/<id>/complete | POST | Marks a task as completed |
| /health | GET | Returns application health status |


## Repository Structure
text
devops-task-manager/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md


## CI/CD Workflow


The CI/CD workflow is implemented using GitHub Actions.


It consists of two jobs:


### 1. Build and Test


Checks out the source code.
Configures Python 3.12.
Installs application dependencies.
Executes automated tests using Pytest.
### 2. Docker Build and Push


Runs after the build-and-test job succeeds.
Authenticates with Docker Hub using GitHub repository secrets.
Builds the Docker image.
Publishes the image to Docker Hub.
The workflow runs on pushes and pull requests targeting main. Docker image publishing is performed on pushes to main.


### GitHub Actions Secrets


The following repository secrets are used for Docker Hub authentication:


DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
Credentials are managed through GitHub Secrets and are not hardcoded in the workflow.


## Containerization


The Flask application is packaged using Docker to provide a consistent and portable runtime environment.


Build the image:
bash
docker build -t devops-task-manager:v1 .


Run the container:
bash
docker run -d \
  --name task-manager \
  -p 80:5000 \
  devops-task-manager:v1


Verify the running container:
bash
docker ps


Check application health:
bash
curl http://localhost/health


Expected response:
json
{"status":"healthy"}


## AWS EC2 Deployment


The containerized application is hosted on an AWS EC2 instance.


Deployment activities:


1. Provisioned an EC2 instance through the AWS Management Console.
2. Connected to the virtual machine using EC2 Instance Connect.
3. Configured the application environment and Docker.
4. Retrieved the application source code from GitHub.
5. Built and ran the Docker container.
6. Configured network access through the EC2 security group.
7. Verified application accessibility using the EC2 public IP.


### Application Access


Application URL:
text
http://<EC2-PUBLIC-IP>


Health-check URL:
text
http://<EC2-PUBLIC-IP>/health


## Validation Results


The following implementation checks were successfully completed:


| Validation | Result |
|---|---|
| Flask application startup | Passed |
| Automated test suite | 4 tests passed |
| Docker image build | Passed |
| Docker container startup | Passed |
| Docker Hub image publishing | Passed |
| GitHub Actions build-and-test job | Passed |
| GitHub Actions Docker build-and-push job | Passed |
| EC2 application accessibility | Passed |
| Application health check | Passed |


## Implementation Notes


The project was completed using available cloud resources and alternative tooling.


**Source control:** The GlobalLogic GitLab instance was inaccessible. GitHub was used as the source-code repository and GitHub Actions as the CI/CD platform.
**Infrastructure provisioning:** EC2 was provisioned manually through the AWS Management Console instead of Terraform, following the permitted alternative approach.
**Container environment:** Docker was configured on the cloud virtual machine rather than the corporate laptop.
**Deployment:** The application was deployed directly to EC2 using Docker. Deployment is currently a manual step; the GitHub Actions workflow automates testing and Docker image publishing.
These alternatives enabled the application delivery and deployment workflow to be completed despite the environment and access limitations.


## Future Enhancements


Integrate persistent storage using a database.
Automate deployment to EC2 after successful image publishing.
Introduce infrastructure provisioning through Terraform.
Implement application monitoring and centralized logging.
Configure HTTPS and secure application access.
## Key Outcomes


Implemented automated application testing.
Built and managed Docker images and containers.
Created a multi-job CI/CD workflow using GitHub Actions.
Published container images to Docker Hub.
Deployed and validated a containerized application on AWS EC2.
---


**Repository:** [devops-task-manager](https://github.com/yasaswini-git23/devops-task-manager)


**Project focus:** Application delivery, containerization, CI/CD automation, and cloud deployment.

A containerized task management application built with Python Flask and delivered through an automated CI/CD pipeline using GitHub Actions, Docker, Docker Hub, and AWS EC2.


## Overview


This project demonstrates an end-to-end application delivery workflow, covering source-code management, automated testing, containerization, image publishing, and cloud deployment.


The application is packaged as a Docker image and deployed on an AWS EC2 virtual machine. GitHub Actions automates the testing, Docker image build, and publishing stages whenever code is pushed to the main branch.


## Architecture
text
                 Developer
                     |
                     v
              GitHub Repository
                     |
                     v
              GitHub Actions
                     |
              +------+------+
              |             |
              v             v
         Build & Test    Docker Build
              |             |
              v             v
            Pytest       Docker Image
                            |
                            v
                        Docker Hub
                            |
                            v
                         AWS EC2
                            |
                            v
                     Docker Container
                            |
                            v
                     Flask Application


## Technology Stack


| Area | Technology |
|---|---|
| Application | Python, Flask |
| Testing | Pytest |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Container Registry | Docker Hub |
| Cloud Platform | AWS |
| Compute | Amazon EC2 |
| Operating System | Amazon Linux |


## Application Features


Create and manage tasks through a web interface.
View tasks in the application.
Mark tasks as completed.
Check application availability through a health endpoint.
### Application Endpoints


| Endpoint | Method | Purpose |
|---|---|---|
| / | GET | Displays the application interface |
| /tasks | POST | Creates a task |
| /tasks/<id>/complete | POST | Marks a task as completed |
| /health | GET | Returns application health status |


## Repository Structure
text
devops-task-manager/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md


## CI/CD Workflow


The CI/CD workflow is implemented using GitHub Actions.


It consists of two jobs:


### 1. Build and Test


Checks out the source code.
Configures Python 3.12.
Installs application dependencies.
Executes automated tests using Pytest.
### 2. Docker Build and Push


Runs after the build-and-test job succeeds.
Authenticates with Docker Hub using GitHub repository secrets.
Builds the Docker image.
Publishes the image to Docker Hub.
The workflow runs on pushes and pull requests targeting main. Docker image publishing is performed on pushes to main.


### GitHub Actions Secrets


The following repository secrets are used for Docker Hub authentication:


DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
Credentials are managed through GitHub Secrets and are not hardcoded in the workflow.


## Containerization


The Flask application is packaged using Docker to provide a consistent and portable runtime environment.


Build the image:
bash
docker build -t devops-task-manager:v1 .


Run the container:
bash
docker run -d \
  --name task-manager \
  -p 80:5000 \
  devops-task-manager:v1


Verify the running container:
bash
docker ps


Check application health:
bash
curl http://localhost/health


Expected response:
json
{"status":"healthy"}


## AWS EC2 Deployment


The containerized application is hosted on an AWS EC2 instance.


Deployment activities:


1. Provisioned an EC2 instance through the AWS Management Console.
2. Connected to the virtual machine using EC2 Instance Connect.
3. Configured the application environment and Docker.
4. Retrieved the application source code from GitHub.
5. Built and ran the Docker container.
6. Configured network access through the EC2 security group.
7. Verified application accessibility using the EC2 public IP.


### Application Access


Application URL:
text
http://<EC2-PUBLIC-IP>


Health-check URL:
text
http://<EC2-PUBLIC-IP>/health


## Validation Results


The following implementation checks were successfully completed:


| Validation | Result |
|---|---|
| Flask application startup | Passed |
| Automated test suite | 4 tests passed |
| Docker image build | Passed |
| Docker container startup | Passed |
| Docker Hub image publishing | Passed |
| GitHub Actions build-and-test job | Passed |
| GitHub Actions Docker build-and-push job | Passed |
| EC2 application accessibility | Passed |
| Application health check | Passed |


## Implementation Notes


The project was completed using available cloud resources and alternative tooling.


**Source control:** The GlobalLogic GitLab instance was inaccessible. GitHub was used as the source-code repository and GitHub Actions as the CI/CD platform.
**Infrastructure provisioning:** EC2 was provisioned manually through the AWS Management Console instead of Terraform, following the permitted alternative approach.
**Container environment:** Docker was configured on the cloud virtual machine rather than the corporate laptop.
**Deployment:** The application was deployed directly to EC2 using Docker. Deployment is currently a manual step; the GitHub Actions workflow automates testing and Docker image publishing.
These alternatives enabled the application delivery and deployment workflow to be completed despite the environment and access limitations.


## Future Enhancements


Integrate persistent storage using a database.
Automate deployment to EC2 after successful image publishing.
Introduce infrastructure provisioning through Terraform.
Implement application monitoring and centralized logging.
Configure HTTPS and secure application access.
## Key Outcomes


Implemented automated application testing.
Built and managed Docker images and containers.
Created a multi-job CI/CD workflow using GitHub Actions.
Published container images to Docker Hub.
Deployed and validated a containerized application on AWS EC2.
---


**Repository:** [devops-task-manager](https://github.com/yasaswini-git23/devops-task-manager)


**Project focus:** Application delivery, containerization, CI/CD automation, and cloud deployment.# DevOps Task Manager
### Containerized Flask Application | CI/CD | AWS EC2


A containerized task management application built with Python Flask and delivered through an automated CI/CD pipeline using GitHub Actions, Docker, Docker Hub, and AWS EC2.


## Overview


This project demonstrates an end-to-end application delivery workflow, covering source-code management, automated testing, containerization, image publishing, and cloud deployment.


The application is packaged as a Docker image and deployed on an AWS EC2 virtual machine. GitHub Actions automates the testing, Docker image build, and publishing stages whenever code is pushed to the main branch.


## Architecture
text
                 Developer
                     |
                     v
              GitHub Repository
                     |
                     v
              GitHub Actions
                     |
              +------+------+
              |             |
              v             v
         Build & Test    Docker Build
              |             |
              v             v
            Pytest       Docker Image
                            |
                            v
                        Docker Hub
                            |
                            v
                         AWS EC2
                            |
                            v
                     Docker Container
                            |
                            v
                     Flask Application


## Technology Stack


| Area | Technology |
|---|---|
| Application | Python, Flask |
| Testing | Pytest |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Container Registry | Docker Hub |
| Cloud Platform | AWS |
| Compute | Amazon EC2 |
| Operating System | Amazon Linux |


## Application Features


Create and manage tasks through a web interface.
View tasks in the application.
Mark tasks as completed.
Check application availability through a health endpoint.
### Application Endpoints


| Endpoint | Method | Purpose |
|---|---|---|
| / | GET | Displays the application interface |
| /tasks | POST | Creates a task |
| /tasks/<id>/complete | POST | Marks a task as completed |
| /health | GET | Returns application health status |


## Repository Structure
text
devops-task-manager/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md


## CI/CD Workflow


The CI/CD workflow is implemented using GitHub Actions.


It consists of two jobs:


### 1. Build and Test


Checks out the source code.
Configures Python 3.12.
Installs application dependencies.
Executes automated tests using Pytest.
### 2. Docker Build and Push


Runs after the build-and-test job succeeds.
Authenticates with Docker Hub using GitHub repository secrets.
Builds the Docker image.
Publishes the image to Docker Hub.
The workflow runs on pushes and pull requests targeting main. Docker image publishing is performed on pushes to main.


### GitHub Actions Secrets


The following repository secrets are used for Docker Hub authentication:


DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
Credentials are managed through GitHub Secrets and are not hardcoded in the workflow.


## Containerization


The Flask application is packaged using Docker to provide a consistent and portable runtime environment.


Build the image:
bash
docker build -t devops-task-manager:v1 .


Run the container:
bash
docker run -d \
  --name task-manager \
  -p 80:5000 \
  devops-task-manager:v1


Verify the running container:
bash
docker ps


Check application health:
bash
curl http://localhost/health


Expected response:
json
{"status":"healthy"}


## AWS EC2 Deployment


The containerized application is hosted on an AWS EC2 instance.


Deployment activities:


1. Provisioned an EC2 instance through the AWS Management Console.
2. Connected to the virtual machine using EC2 Instance Connect.
3. Configured the application environment and Docker.
4. Retrieved the application source code from GitHub.
5. Built and ran the Docker container.
6. Configured network access through the EC2 security group.
7. Verified application accessibility using the EC2 public IP.


### Application Access


Application URL:
text
http://<EC2-PUBLIC-IP>


Health-check URL:
text
http://<EC2-PUBLIC-IP>/health


## Validation Results


The following implementation checks were successfully completed:


| Validation | Result |
|---|---|
| Flask application startup | Passed |
| Automated test suite | 4 tests passed |
| Docker image build | Passed |
| Docker container startup | Passed |
| Docker Hub image publishing | Passed |
| GitHub Actions build-and-test job | Passed |
| GitHub Actions Docker build-and-push job | Passed |
| EC2 application accessibility | Passed |
| Application health check | Passed |


## Implementation Notes


The project was completed using available cloud resources and alternative tooling.


**Source control:** The GlobalLogic GitLab instance was inaccessible. GitHub was used as the source-code repository and GitHub Actions as the CI/CD platform.
**Infrastructure provisioning:** EC2 was provisioned manually through the AWS Management Console instead of Terraform, following the permitted alternative approach.
**Container environment:** Docker was configured on the cloud virtual machine rather than the corporate laptop.
**Deployment:** The application was deployed directly to EC2 using Docker. Deployment is currently a manual step; the GitHub Actions workflow automates testing and Docker image publishing.
These alternatives enabled the application delivery and deployment workflow to be completed despite the environment and access limitations.


## Future Enhancements


Integrate persistent storage using a database.
Automate deployment to EC2 after successful image publishing.
Introduce infrastructure provisioning through Terraform.
Implement application monitoring and centralized logging.
Configure HTTPS and secure application access.
## Key Outcomes


Implemented automated application testing.
Built and managed Docker images and containers.
Created a multi-job CI/CD workflow using GitHub Actions.
Published container images to Docker Hub.
Deployed and validated a containerized application on AWS EC2.
---


**Repository:** [devops-task-manager](https://github.com/yasaswini-git23/devops-task-manager)


**Project focus:** Application delivery, containerization, CI/CD automation, and cloud deployment.
