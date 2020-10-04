import os
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

db_username = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASreaS')
engine = create_engine('postgres://dbuser:dbpass@localhost:5432/sample_database')

sql_df = pd.read_sql('sample_table', engine)
#sql_df = pd.read_sql_query('SELECT * FROM sample_table', engine)
print(sql_df)
