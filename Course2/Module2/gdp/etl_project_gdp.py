import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime

log_file = "etl_project_log.txt" 
target_file = "Countries_by_GDP.csv" 
#python3 -m venv etl_env/
#source etl_env/bin/activate
#pip install requests bs4 pandas  
url='https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

gdp_column='country_gdp_USD_millions'
gdp_billions_column='country_gdp_USD_billions'
country_column='country_name'
table_name='Countries_by_GDP'
db_name='World_Economies.db'


# Code for ETL operations on Country-GDP data

# Importing the required libraries

def extract(url, table_attribs=None):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''

    response=requests.get(url)
    print('Response status code:',response.status_code)
    html_content=response.text
    #parser='html5lib'
    parser='html.parser'

    soup = BeautifulSoup(html_content,parser)
    gdps_table=soup.find_all('tbody')[2]

    gdps_entries= gdps_table.find_all('tr')[3:]
    print(gdps_entries)

    print(type(gdps_entries))


    countries_list=[]
    for row in gdps_entries:
        
        data=row.find_all('td')

        if len(data)==0:
            continue
        
        country_dict={'country_name': data[0].text,
                    'country_gdp_USD_millions':data[2].text                }
        countries_list.append(country_dict)
        
    print(countries_list)

    gdp_df=pd.DataFrame(countries_list)
    print(gdp_df)

    return gdp_df

def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''

    
    df[gdp_column] = df[gdp_column].str.replace(',', '').replace('—', '0').astype(float) / 1000
    df[gdp_column] = df[gdp_column].round(2)
    df.rename(columns={gdp_column: gdp_billions_column}, inplace=True)

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
    print(f'Query output: {query_output}')

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



log_progress('Extracting countries GDPs data')


gdp_df=extract(url)

log_progress('Transforming countries GDPs data')

transformed_df=transform(gdp_df)
print(transformed_df)
log_progress('Loading countries GDPs data to CSV')

load_to_csv(transformed_df,target_file)

log_progress('Connecting to SQLite database')
conn=sqlite3.connect(db_name)

log_progress('Loading countries GDPs data to SQLite database')

load_to_db(transformed_df,conn,table_name)

query=f'SELECT * FROM {table_name} WHERE {gdp_billions_column} > 100'
log_progress('Running the query')

run_query(query,conn)
conn.close()

log_progress('SQLite database connection closed')


