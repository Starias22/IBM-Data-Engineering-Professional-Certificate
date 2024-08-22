import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime

log_file = "code_log.txt" 
target_file = "Largest_banks_data.csv" 
exchange_rate_csv='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv'
#python3 -m venv etl_env/
#source etl_env/bin/activate
#pip install requests bs4 pandas  
url='https://en.wikipedia.org/wiki/List_of_largest_banks'

name_column='Name'
mc_usd_billion_column='MC_USD_Billion'
mc_gbp_billion_column='MC_GBP_Billion'
mc_eur_billion_column='MC_EUR_Billion'
mc_inr_billion_column='MC_INR_Billion'

table_name='Largest_banks'
db_name='Banks.db'


# Code for ETL operations on Country-GDP data

# Importing the required libraries

def extract(url, table_attribs=None):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''

    response=requests.get(url)
    print('Response status code:',response.status_code)
    html_content=response.text
    parser='html.parser'

    soup = BeautifulSoup(html_content,parser)
    banks_table=soup.find_all('tbody')[2]
    banks_entries= banks_table.find_all('tr')[0:]

    banks_list=[]
    for row in banks_entries:
        
        data=row.find_all('td')

        if len(data)==0:
            continue
        
        bank_dict={name_column: data[1].text[:-1],
                    mc_usd_billion_column:data[2].text [:-1]               }
        banks_list.append(bank_dict)
        
    print(banks_list)

    gdp_df=pd.DataFrame(banks_list)
    print(gdp_df)

    return gdp_df

def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''
    
    exchange_rate_df=pd.read_csv(exchange_rate_csv)
    eur_rate=exchange_rate_df.iloc[0]['Rate']
    gbp_rate=exchange_rate_df.iloc[1]['Rate']
    inr_rate=exchange_rate_df.iloc[2]['Rate']

    df[mc_usd_billion_column]=df[mc_usd_billion_column].astype(float)

    df[mc_eur_billion_column]=(eur_rate*df[mc_usd_billion_column]).round(2)
    df[mc_gbp_billion_column]=(gbp_rate*df[mc_usd_billion_column]).round(2)
    df[mc_inr_billion_column]=(inr_rate*df[mc_usd_billion_column]).round(2)

    return df

def load_to_csv(df, csv_path):
    ''' This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.'''
    df.to_csv(csv_path,index=False)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final dataframe as a database table
    with the provided name. Function returns nothing.'''

    df.to_sql(table_name,sql_connection,if_exists='replace',index=False)

def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    print(f'Query statement: {query_statement}')
    query_output=pd.read_sql(query_statement,sql_connection)
    print(f'Query output\n {query_output}')

def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''

    ''' Here, you define the required entities and call the relevant 
    functions in the correct order to complete the project. Note that this
    portion is not inside any function.'''

    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n')



log_progress('Extracting banks market capital data')


gdp_df=extract(url)

log_progress('Transforming banks market capital data')

transformed_df=transform(gdp_df)
print(transformed_df)

log_progress('Loading banks market capital to CSV')

load_to_csv(transformed_df,target_file)


log_progress('Connecting to SQLite database')
conn=sqlite3.connect(db_name)

log_progress('Loading banks market capital data to SQLite database')

load_to_db(transformed_df,conn,table_name)

query=f'SELECT AVG({mc_gbp_billion_column}) FROM {table_name}'
log_progress('Running the query')

run_query(query,conn)
conn.close()

log_progress('SQLite database connection closed')