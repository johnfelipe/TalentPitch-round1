import pandas as pd

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
