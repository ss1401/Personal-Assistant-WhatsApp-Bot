#import pypyodbc as odbc # pip install pypyodbc
import pandas as pd # pip install pandas
import pyodbc

#connection
conn=pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-8UVAR6B;"
    "Database=test;"
    "Trusted_Connection=yes;"
)

#Importing dataset from CSV

df = pd.read_csv('sample.csv')

columns = ['Name', 'Class', 'Contact']

df_data = df[columns]
records = df_data.values.tolist()
#print(records)

"""
cursor=conn.cursor()
x=len(records)
for i in range(x):
    cursor.execute("INSERT into test2 values (%s,%s,%s)", ((records[i][0],records[i][1],records[i][2]),))
"""

