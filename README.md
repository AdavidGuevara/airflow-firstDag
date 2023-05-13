# Primer codigo con airflow en un entorno virtual.

#### Comandos:
- export AIRFLOW_HOME=`pwd`/airflow
- export AIRFLOW__CORE__LOAD_EXAMPLES=False
- pip install apache-airflow
- airflow db init

- airflow users create \
    --username [] \
    --firstname [] \
    --lastname [] \
    --role [] \
    --email []s

- airflow webserver --port 8080
- airflow scheduler