import pyodbc
import pandas as pd

# Method 1
conn = pyodbc.connect("DSN=ethicscompliance_stg", autocommit=True)
sql = ("SELECT * FROM event_refined.hibbert_event_rfnd LIMIT 5000")

df = pd.read_sql_query(sql, conn)

print(df)


# Method 2
conn = pyodbc.connect("DSN=ethicscompliance_stg", autocommit=True)
cursor = conn.cursor()
cur_df = cursor.execute("SELECT * FROM event_refined.hibbert_event_rfnd LIMIT 50")

df = pd.DataFrame(data = cur_df.fetchall())
