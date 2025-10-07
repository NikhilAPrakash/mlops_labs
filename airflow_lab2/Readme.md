# Airflow Lab 2

This project demonstrates the use of Apache Airflow for orchestrating machine learning workflows. It includes data preprocessing, model training, saving, and loading using Airflow DAGs. 

## Project Structure

- `docker-compose.yaml`: Docker Compose file to set up Airflow and its dependencies.
- `config/`: Configuration files for Airflow.
- `dags/`: Contains DAG definitions and related code.
  - `airflow.py`: Main DAG file orchestrating the workflow.
  - `model/`: Stores the trained model (`model.sav`).
  - `src/`: Source code for data processing and model training (`lab.py`).
- `logs/`: Airflow logs for DAG runs and tasks.
- `plugins/`: Custom Airflow plugins (if any).
- `working_data/`: Directory for intermediate or working data.


## Main Components

- **DAG (`airflow.py`)**: Defines the workflow for data loading, preprocessing, model training, saving, and loading.
- **Model (`model.sav`)**: Serialized machine learning model.
- **Source Code (`src/lab.py`)**: Contains functions for data processing and model operations.

## Getting Started

1. **Clone the repository**
2. **Navigate to the `airflow_lab2` directory**
3. **Start Airflow using Docker Compose:**
   ```sh
   docker-compose up
   ```
4. **Access the Airflow UI:**
   - Open your browser and go to `http://localhost:8080`
   - Credentials: `airflow2` / `airflow2`
5. **Trigger the DAG** from the Airflow UI to run the workflow.

## Requirements

- Docker & Docker Compose
- Apache Airflow (managed via Docker)

## Notes

- All logs are stored in the `logs/` directory.
- Update the DAG or source code as needed for your specific ML workflow.

## References
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
