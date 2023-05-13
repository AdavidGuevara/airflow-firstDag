from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from airflow import DAG
import logging

default_args = {
    "owner": "adavid",
    "depends_on_past": False,
    "email": ["example@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def scrape():
    logging.info("performing scraping")


def process():
    logging.info("performing processing")


def save():
    logging.info("performing saving")


with DAG(
    "first",
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=["example"],
) as dag:
    scrape_task = PythonOperator(task_id="scrape", python_callable=scrape)
    process_task = PythonOperator(task_id="process", python_callable=process)
    save_task = PythonOperator(task_id="save", python_callable=save)

    scrape_task >> process_task >> save_task