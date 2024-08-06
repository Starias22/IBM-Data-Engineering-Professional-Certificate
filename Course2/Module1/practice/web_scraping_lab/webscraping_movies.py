import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
# mkdir web_scraping_env
#python3 -m venv web_scraping_env/
#source web_scraping_env/bin/activate
#pip install requests html5lib bs4 pandas  
url='https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

response=requests.get(url)
print('Response status code:',response.status_code)
html_content=response.text
#parser='html5lib'
parser='html.parser'

soup = BeautifulSoup(html_content,parser)
movies_table=soup.find('table')
#print(movies_table)
n=50

movie_entries=movies_table.find_all('tr')[1:]
print(movie_entries)
movies_list=[]
for movie in movie_entries:
    
    movie_data=movie.find_all('td')

    if len(movie_data)==0:
        continue
    
    if len(movies_list)==50:
        break
    average_rank=movie_data[0].text
    name=movie_data[1].text
    year=movie_data[2].text
    movie_dict={'average_rank': movie_data[0].text,
                'name':movie_data[1].text,
                'year':movie_data[2].text
                }
    movies_list.append(movie_dict)
    
    print(movie_dict)

movies_df=pd.DataFrame(movies_list)
print(movies_df)
movies_df.to_csv('top_50_films.csv',index=False)

DB_NAME = 'Movies.db'
TABLE_NAME = 'Top_50'

conn=sqlite3.connect(DB_NAME)
movies_df.to_sql(TABLE_NAME,conn,if_exists='replace',index=False)
conn.close()

