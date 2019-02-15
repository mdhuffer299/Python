
"""
Create dictionary data frame
"""

import pyodbc
import pandas as pd

def createDataDictionary(DSN_Connection_Name, database_name, env_name):
    conn = pyodbc.connect("DSN=" + DSN_Connection_Name, autocommit=True)
    showTableSql = ("SHOW TABLES IN " + database_name)
    
    tableNameDF = pd.read_sql_query(showTableSql, conn)
    
    tableDescriptionDF = pd.DataFrame(columns = ["col_name", "data_type", "comment", "tab_name", "db_name", "env_name"])
    for index, row in tableNameDF.iterrows():
        tableName = (row["tab_name"])
        describeTableSql = ("DESCRIBE " + str(database_name) + "." + str(tableName))
        
        if len(tableDescriptionDF.index) == 0:
            tableDescriptionDF = pd.read_sql_query(describeTableSql, conn)
            tableDescriptionDF["tab_name"] = tableName
            tableDescriptionDF["db_name"] = database_name
            tableDescriptionDF["env_name"] = env_name
        else:
            appendTableDescriptionDF = pd.read_sql_query(describeTableSql, conn)
            appendTableDescriptionDF["tab_name"] = tableName
            tableDescriptionDF["db_name"] = database_name
            tableDescriptionDF["env_name"] = env_name
            tableDescriptionDF = tableDescriptionDF.append(appendTableDescriptionDF)
    
    return(tableDescriptionDF)

"""
Write to HDFS
"""
from pywebhdfs.webhdfs import PyWebHdfsClient
from requests_kerberos import HTTPKerberosAuth

def writeFileToHdfs(hostName, userName, writePath, dataframe, fileName):
    auth = HTTPKerberosAuth()
    hdfsClient = PyWebHdfsClient(host = hostName,port = '50070', user_name = userName, request_extra_opts={'auth': auth})
    
    outputPath = writePath
    stringDF = dataframe.to_csv(columns = ["env_name","db_name","tab_name","col_name", "data_type", "comment"], index = False)
    
    hdfsClient.create_file(path = outputPath + fileName + ".csv", file_data = stringDF, overwrite = True)
    

"""
Reads the tables from production ec_consolidated zone and assigns to a pandas dataframe using createDataDictionary
Write dataframe out as CSV File in HDFS dev using writeFileToHdfs function


createDataDictionary(<Your DSN Connection Name>, <Database>, <Environment Name>)
writeFileToHdfs(<Host Name>, <Your Username>, <output directory>, <Dataframe>, <File Name>)
"""    
dataDictionaryDF = createDataDictionary("DSN Name", "DB", "PRD")

writeFileToHdfs('Host', 'User', 'Directory', DF, 'File Name')


db_names = ["List of Database Name"]
for db in db_names:
    dataDictionaryDF = createDataDictionary()
    writeFileToHdfs()
