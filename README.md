# End to End ML Project: Student Performance Prediction

The objective of the project is to learn about end-to-end project implementation including
- ML Project Structure (Python Packaging & Modular Coding)
- Create train and predict pipelines
- Custom Exception handling, logging of information
- FastAPI Server
- Dockerization of project
- CI-CD pipeline
    - GitHub Actions, Workflows
    - GitHub self-hosted runners
- Deployment on AWS
    - ECR
    - EC2
    - IAM

## Video: Running docker image on Docker Engine


https://github.com/abhijeetk597/student-performance-prediction/assets/138308825/f8d91398-4304-4d93-82c0-f8b368bc3088



## Video: Project deployed on AWS EC2 Instance using GitHub Actions


https://github.com/abhijeetk597/student-performance-prediction/assets/138308825/8b056d15-c6f9-4870-8009-afa428a75a1d



## Acknowledgement
For this project I took inspiration from **Krish Naik**'s [Youtube Playlist](https://www.youtube.com/watch?v=Rv6UFGNmNZg&list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG&index=4)

## My contribution
- Created model training pipeline
- Hyperparameter tuning performed by reading parameters from `YAML` file
- Created FASTApi server
- Docker Image was pushed to and pulled from an **AWS ECR Public Repository**

## IMP EC2 CLI Commands for reference
- sudo apt-get update -y
- sudo apt-get upgrade -y
- curl -fsSL https://get.docker.com -o get-docker.sh
- sudo sh get-docker.sh
- sudo usermod -aG docker ubuntu
- newgrp docker
- *other commands for configuring self-hosted runner*
