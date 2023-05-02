from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from ETL_script import read_csv_file, clean_data, write_csv_file


with DAG(dag_id='AD_seattle',
         description='Traffic accidient data in the city of seattle',
         schedule_interval="@daily", 
         start_date=datetime(2023, 5, 1), 
         catchup=False) as dag:
        
    
        Read_csv = PythonOperator(
          task_id='Read_csv',
          python_callable= read_csv_file
          )
        
        Data_transformation= PythonOperator(
          task_id='Data_transformation',
          python_callable= clean_data,
          op_kwargs={'df': Read_csv.output}
          )

        Write_csv= PythonOperator(
          task_id='Write_csv',
          python_callable= write_csv_file,
          op_kwargs={'cleaned_df': Data_transformation.output}
          )

Read_csv >> Data_transformation >> Write_csv