# First code with airflow in a virtual environment.

#### Commands:
- export AIRFLOW_HOME=`pwd`/airflow
- export AIRFLOW__CORE__LOAD_EXAMPLES=False
- pip install apache-airflow
- airflow db init

- airflow users create \
    --username [] \
    --firstname [] \
    --lastname [] \
    --role [] \
    --email []

- airflow webserver --port 8080
- airflow scheduler
