# DevOps Task Manager


**A Containerized Flask Application with CI/CD Automation and AWS EC2 Deployment**


## 1. Project Overview


This project demonstrates an end-to-end application delivery workflow using DevOps practices and tools.


A Flask-based Task Manager application is developed, tested, containerized using Docker, and deployed on an AWS EC2 virtual machine.


GitHub is used for source code management, while GitHub Actions automates application testing, Docker image building, and publishing images to Docker Hub.


The project covers:


Application development using Python and Flask
Source code management using Git and GitHub
Automated testing using Pytest
Application containerization using Docker
CI/CD automation using GitHub Actions
Container image publishing using Docker Hub
Cloud deployment using AWS EC2
Application health verification
## 2. Architecture


The project follows this application delivery workflow:
text
                 Developer
                     |
                     v
              GitHub Repository
                     |
                     v
               GitHub Actions
                     |
          +----------+----------+
          |                     |
          v                     v
     Build & Test        Docker Build & Push
          |                     |
          v                     v
      Pytest Tests           Docker Hub
                                |
                                v
                             AWS EC2
                                |
                                v
                         Docker Container
                                |
                                v
                         Flask Application


## 3. Technology Stack


| Area | Technology |
|---|---|
| Application | Python, Flask |
| Testing | Pytest |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Container Registry | Docker Hub |
| Cloud Platform | AWS |
| Compute Service | Amazon EC2 |
| Operating System | Amazon Linux 2023 |


## 4. Application Features


The Task Manager application provides a simple web interface to manage tasks.


Key features:


Create new tasks.
View existing tasks.
Mark tasks as completed.
Check application availability through a health endpoint.
### Application Endpoints


| Endpoint | Method | Purpose |
|---|---|---|
| / | GET | Displays the application interface |
| /tasks | POST | Creates a new task |
| /tasks/<task_id>/complete | POST | Marks a task as completed |
| /health | GET | Returns application health status |


## 5. Repository Structure
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


## 6. CI/CD Workflow


The CI/CD pipeline is implemented using GitHub Actions.


The workflow is triggered when code is pushed to the main branch or when a pull request targets the main branch.


It consists of two jobs.


### Job 1: Build and Test


This job:


1. Checks out the source code.
2. Configures Python 3.12.
3. Installs application dependencies.
4. Executes automated tests using Pytest.


### Job 2: Docker Build and Push


This job runs after the Build and Test job succeeds, and only for pushes to the repository.


It:


1. Checks out the source code.
2. Authenticates with Docker Hub using GitHub repository secrets.
3. Builds the Docker image.
4. Publishes the image to Docker Hub with the latest tag.


### GitHub Actions Secrets


The following repository secrets are configured for Docker Hub authentication:


DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
Credentials are securely managed through GitHub Secrets and are not hardcoded in the workflow.


## 7. Containerization Using Docker


The Flask application is packaged into a Docker image to provide a consistent and portable runtime environment.


### Build Docker Image
bash
docker build -t devops-task-manager:v1 .


### Run Docker Container
bash
docker run -d \
  --name task-manager \
  -p 80:5000 \
  devops-task-manager:v1


### Verify Running Container
bash
docker ps


### Verify Application Health
bash
curl http://localhost/health


Expected response:
json
{"status":"healthy"}


## 8. Docker Hub Image


The application Docker image is published to Docker Hub.


**Docker Hub Repository:**


https://hub.docker.com/r/yasaswinidocker123/devops-task-manager


The image can be retrieved using:
bash
docker pull yasaswinidocker123/devops-task-manager:latest


## 9. AWS EC2 Deployment


The containerized application is hosted on an AWS EC2 instance.


### Deployment Activities


1. Provisioned an EC2 instance through the AWS Management Console.
2. Connected to the virtual machine using EC2 Instance Connect.
3. Configured Docker on the Amazon Linux 2023 environment.
4. Retrieved the application source code from GitHub.
5. Built and ran the Docker container.
6. Configured network access through the EC2 security group.
7. Verified application accessibility using the EC2 public IPv4 address.


### Application Access


**Application URL:**


http://YOUR_EC2_PUBLIC_IPV4/


**Health Check URL:**


http://YOUR_EC2_PUBLIC_IPV4/health


Replace YOUR_EC2_PUBLIC_IPV4 with the actual public IPv4 address of the EC2 instance.


## 10. Validation Results


The following implementation checks were successfully completed:


| Validation | Result |
|---|---|
| Flask application execution | Passed |
| Automated Pytest test cases | Passed (4 tests) |
| Docker image build | Passed |
| Docker container execution | Passed |
| Docker Hub image publishing | Passed |
| GitHub Actions Build and Test job | Passed |
| GitHub Actions Docker Build and Push job | Passed |
| EC2 application accessibility | Passed |
| Application health check | Passed |


## 11. Implementation Notes and Alternatives


The project was completed using available cloud resources and alternative tooling, following the permitted approach.


**Source Code Management:** The GlobalLogic GitLab instance was inaccessible. GitHub was used as the source code repository, with GitHub Actions serving as the CI/CD platform.


**Infrastructure Provisioning:** Terraform-based EC2 provisioning was skipped as permitted by the trainer. The EC2 instance was provisioned manually through the AWS Management Console.


**Container Environment:** Docker was configured and executed on the cloud virtual machine instead of the corporate laptop.


**Deployment:** The application was deployed manually to the AWS EC2 instance using Docker. GitHub Actions automates application testing and Docker image publishing; deployment to EC2 remains a manual step.


These alternatives enabled the application delivery and deployment workflow to be completed despite the environment and access limitations.


## 12. Key Outcomes


Through this project, the following DevOps capabilities were implemented and demonstrated:


Developed and tested a Flask application.
Implemented automated testing using Pytest.
Containerized an application using Docker.
Built a multi-job CI/CD workflow using GitHub Actions.
Published Docker images to Docker Hub.
Provisioned and configured an AWS EC2 environment.
Deployed and validated a containerized application on AWS EC2.
Implemented application health verification.

## 13. AI Assistance


Representative prompts used for AI-assisted implementation and troubleshooting:


**Prompt 1 – Application Development**


"Create a Flask-based Task Manager application with functionality to add tasks, view tasks, mark tasks as completed, and expose a health-check endpoint. Include Pytest test cases."


**Prompt 2 – Docker Containerization**


"Create a Dockerfile for the Flask application using Python 3.12, install dependencies, expose the application port, and provide Docker build and run commands."


**Prompt 3 – CI/CD Pipeline**


"Create a GitHub Actions CI/CD workflow that checks out the repository, configures Python, installs dependencies, runs Pytest, builds a Docker image, and publishes it to Docker Hub using GitHub Secrets."


---


**Project Repository:** https://github.com/yasaswini-git23/devops-task-manager


**Docker Hub:** https://hub.docker.com/r/yasaswinidocker123/devops-task-manager


**Project Focus:** Application Delivery | Containerization | CI/CD Automation | Cloud Deployment
