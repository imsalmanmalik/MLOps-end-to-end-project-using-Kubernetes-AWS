# MLOps-end-to-end-project
End-to-end prediction model development using PySpark with Docker and Streamlit

### Adapted from the book 'Applied Data Science using PySpark' from R. Kakarla, S. Krishnan and S. Alla

# Use Case

Development and deployment of a Random Forest Classifier using Spark ML to determine loan approval success based on individual profile and default status

* Exploratory analysis using PySpark
* Feature engineering using Spark SQL
* Model developement using Spark ML and Vector Assembler to create ML pipelines
* Compiled models in seperate pickle files to migrate from development to staging environment
* Developed UI using Streamlit 
* Build Docker Image to containerise model development
* Establish API connect using Postman 
* Create a Docker compose file to build CI/CD pipeline between the backend PySpark API and Streamlit API

# Docker Images

Docker images are hosted on Docker Hub.

[Repository](https://hub.docker.com/r/salmanmalik98/ml-ops-end-to-end)

# Quick start

By default docker-compose uses images defined in the file with `latest` tag.

```shell
docker-compose up -d
```

# Development

When in development mode use below command to build the image to get quick feedback loop for fixes / new features.

This will build docker image from local build context

```shell
docker-compose up -d --build
```