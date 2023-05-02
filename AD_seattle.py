from airflow import DAG
from datetime import datetime
import pandas as pd
from airflow.operators.python_operator import PythonOperator

columns_to_drop =['X',
         'Y',
         'EXCEPTRSNCODE',
         'EXCEPTRSNDESC',
         'PEDCOUNT', 
         'PEDCYLCOUNT', 
         'VEHCOUNT',
         'INJURIES',
         'SERIOUSINJURIES', 
         'FATALITIES',
         'SPEEDING',
         'ST_COLCODE',
         'PEDROWNOTGRNT',
         'SDOTCOLNUM',
         'SPEEDING',
         'SEGLANEKEY',
         'CROSSWALKKEY', 
         'HITPARKEDCAR'
        ]
def read_csv_file():
    df = pd.read_csv('/home/abc/airflow/dags/Collisions.csv')
    return df

def clean_data(df):
    df = df.drop(columns=columns_to_drop)
    df = df.dropna(0)
    cleaned_df = df.drop_duplicates()
    print(list(df["WEATHER"].unique()))
    Total_accident = df.groupby(['WEATHER'])['WEATHER'].count()
    print(Total_accident)
    return cleaned_df

def write_csv_file(cleaned_df):
    cleaned_df.to_csv('/home/abc/airflow/dags/new_Collisions.csv', index=False)


with DAG(dag_id='AD_seattle',
         description='Traffic accidient data in the city of seattle',
         schedule_interval=None, 
         start_date=datetime(2020, 1, 1), 
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