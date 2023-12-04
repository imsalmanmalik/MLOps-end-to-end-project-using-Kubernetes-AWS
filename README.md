# MLOps-end-to-end-project

End-to-end prediction model development using PySpark with Docker and Streamlit, incorporating AWS Elastic Kubernetes Service (EKS) for deployment.

## Project Features

- Exploratory Data Analysis and Feature Engineering using PySpark.
- Model Development with Spark ML pipelines.
- Serialization of models into pickle files for transitioning between environments.
- Streamlit-based User Interface for real-time predictions.
- Containerization of development environment with Docker.
- API testing with Postman.
- Networking setup between Docker containers for services communication.
- CI/CD pipeline using GitHub Actions with Docker Hub.
- Deployment and orchestration using Kubernetes on AWS EKS.
- Images for EKS deployment are hosted on AWS Elastic Container Registry (ECR).

## Using Docker for Deployment (Alternative to Kubernetes)

For those preferring Docker over Kubernetes, you can build your own images and use the provided `docker-compose.yml` file to run the services.

Build your own images:

```bash
docker build -t your-custom-streamlit-image ./streamlitapi
docker build -t your-custom-pyspark-image ./pysparkapi
```
Run the services using Docker Compose:

```bash
docker-compose up -d
```

This will use the docker-compose.yml file to start the services locally without the need for Kubernetes.
**Note**: Replace url in your Streamlit application `webapp.py` with the string `http://pyspark:5000`. As currently it is set up for the Streamlit application to properly resolve and communicate with the PySpark API service within the Kubernetes cluster.

## CI/CD Pipeline

The CI/CD pipeline is configured with Docker Hub to automate the build and deployment process. However, for AWS EKS deployment, the images are available on AWS ECR.

## IAM Policies and AWS EKS Configuration

The following IAM policies are required for provisioning an EKS cluster and its nodes:

- **EKS Cluster IAM Role**: `AmazonEKSClusterPolicy`
- **EKS Node IAM Role**: `AmazonEKSWorkerNodePolicy`, `AmazonEC2ContainerRegistryReadOnly`, `AmazonEKS_CNI_Policy`

Configure your `kubeconfig` to access your AWS EKS cluster:

```bash
aws eks --region <region> update-kubeconfig --name <cluster-name>
```
## Docker Images
While Docker images are built and pushed to Docker Hub via the CI/CD pipeline, the images used for EKS deployment are stored in ECR:

```bash
docker pull public.ecr.aws/d4r6m7g7/streamlit:latest
docker pull public.ecr.aws/d4r6m7g7/pyspark:latest
```
## Kubernetes Manifests for EKS Deployment
Apply the Kubernetes manifests to deploy the services:

```bash
kubectl apply -f pyspark-api-deployment.yaml
kubectl apply -f pyspark-api-service.yaml
kubectl apply -f streamlit-api-deployment.yaml
kubectl apply -f streamlit-api-service.yaml
```

## Accessing the Application UI
The Streamlit UI is exposed via a LoadBalancer and can be accessed at the DNS name provided by AWS:

```bash
http://<LoadBalancer-DNS-name>:8501
```
## Conclusion
This project demonstrates a comprehensive MLOps workflow integrating Docker, Kubernetes, and AWS services, from development through to a scalable production deployment.

