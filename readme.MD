# Airflow with Docker
## Prerequisites
* Docker
* Docker Compose
## Install airflow wtih docker compose file
follow below cammands:
To install airflow with docker compose file
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.1.1/docker-compose.yaml'
```

To create dad, logs and plugins folder
```bash
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```

To init database
```bash
docker-compose up airflow-init
```
Every time you need to run this cammand for airflow instance up
Start the Docker containers:
```bash
docker-compose up
```
To stop the containers, run:
```bash
docker-compose down
```

# Airflow with dockerfile
Step1: Create a new directory for your Airflow project:
```bash
mkdir airflow-project
cd airflow-project
```
Step2: Create a file named Dockerfile in your project directory 

Step3: Build the Docker image using the following command:
```bash
docker build -t airflow_image
```
Step4: Start a Docker container using the following command:
```bash
docker run -d -p 8080:8080 airflow_image
```
Step5: You can access the Airflow webserver by opening a web browser and navigating to http://localhost:8080.

To stop running container:
```bash
docker stop <container-id-or-name>
```
To get list of running containers for container id or name
```bash
docker ps
```