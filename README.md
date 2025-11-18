# MLOps Labs

This repository contains hands-on labs and projects for learning and practicing MLOps concepts, including workflow orchestration, model training, deployment, and automation using tools like Apache Airflow and FastAPI.

## Repository Structure

- `airflow_lab2/`  
  Orchestrate machine learning workflows using Apache Airflow. Includes DAGs for data preprocessing, model training, and more.
- `fastapi_lab1/`  
  Build and serve machine learning models using FastAPI. Includes endpoints for training and prediction.

## Labs Overview


### Tensorboard Logging Lab 5
- Lab 5 of IE7374 MLOPs Lab
- Combination of the four labs available in MLOPs Repo 


### Experiment Tracking - Weights and Biases Lab 4
- Lab 4 of IE7374 MLOPs Lab
- Key Components
  - Sentiment Analysis
  - Defines a Pytorch LSTM model
  - logs confusion matrix to WanDB
  - storing best validation model to wandb artifact
  
### Github Actions and GCP Lab 3
- Lab 3 of IE7374 MLOPs Lab
- Please refer the below link:
```bash
https://github.com/NikhilAPrakash/ghactions-gcp-beginner-lab.git
```
- Using GCP and github actions to automate workflows
- Key components:
  - Setting up a GCP project and service account
  - Github Actions access setup with GCP
  - Using GCS to store trained models

### Airflow Lab 2
- Lab 2 of IE7374 MLOPs Lab
- Using Apache Airflow for automating ML pipelines.
- Key components:
  - DAGs for data loading, preprocessing, model training, saving, and loading.
  - Docker Compose setup for easy deployment.
  - Logs and configuration for Airflow tasks.

### FastAPI Lab 1
- Lab 1 of IE7374 MLOPs Lab
- Building REST API for ML models using FastAPI.
- Key components:
  - Endpoints for training and prediction.
  - Pre-trained models for iris and wine datasets.
  - Example results and assets.

## Getting Started

1. Clone the repository:
   ```sh
   git clone https://github.com/NikhilAPrakash/mlops_labs.git
   ```
2. Explore each lab's folder for specific setup and usage instructions.

## Requirements
- Docker & Docker Compose (for Airflow Lab)
- Python 3.8+ (for FastAPI Lab)
- See each lab's `requirements.txt` for dependencies


---
