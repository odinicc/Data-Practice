# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago
import tarfile

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'ivan Odintsov',
    'start_date': days_ago(0),
    'email': ['odinicc@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(minutes=1),
)

# define the tasks

# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago
import tarfile

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'ivan Odintsov',
    'start_date': days_ago(0),
    'email': ['odinicc@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(minutes=1),
)

# define the tasks

# define the tasks #1 to unzip data
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='/home/project/airflow/dags/finalassignment/unzip_data.sh ',
    dag=dag,
)

# define the tasks #2 to extract data from csv
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d# -f1-4 /home/project/airflow/dags/finalassignment/vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)

# define the tasks #3 to extract data from tsv
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -d# -f5-7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv > /home/project/airflow/dags/finalassignment/tsv_data.csv',
    dag=dag,
)


# define the tasks #4 to extract data from txt
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='/home/project/airflow/dags/finalassignment/extract_data_from_fixed_width.sh ',
    dag=dag,
)

# define the tasks #5 to consolidate data extracted from previous tasks
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='paste /home/project/airflow/dags/finalassignment/csv_data.csv /home/project/airflow/dags/finalassignment/tsv_data.csv /home/project/airflow/dags/finalassignment/fixed_width_data.csv > extracted_data.csv ',
    dag=dag,
)

# define the tasks #6 to transform vehicle_type field in extracted_data.csv into capital letters 
transform_data = BashOperator(
    bash_command='awk '{print $1, $2, toupper($3), toupper($4), toupper($5), toupper($6), toupper($7), toupper($8), toupper($9), toupper($10), toupper($11)}' /home/project/airflow/dags/finalassignment/extracted_data.csv > /home/project/airflow/dags/finalassignment/transformed_data.csv ',
    dag=dag,
)
    
# task pipeline
    task_id='transform_data',
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
