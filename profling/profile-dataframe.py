import pandas as pd
import numpy as np

def profileDataFrame(df):
    columnNames = list(df)
    profileDF = pd.DataFrame(columns = ["tableName", "columnName", "pandasDataType", "inferredDataType", "columnMin", "columnMax", "stringLength", "precision", "distinctValues", "columnMean", "columnSD", "missingValues", "percentMissing"])
    
    for column in columnNames:

        # Return Table and Column Name
        if "." in column:
            tableName  = column.split(".")[0]
            columnName = column.split(".")[1]
        else:
            tableName = "NA"
            columnName = column
        
        # Return Pandas Data Type for each column
        columnType = df[column].dtypes
        
        # Return the Inferred Data Type for SQL
        if columnType == 'object':
            inferredColumnType = 'VARCHAR'
        elif columnType == 'int64':
            inferredColumnType = 'INT'
        elif columnType == 'float64':
            inferredColumnType = 'DECIMAL'
        else:
            inferredColumnType = 'UNKNOWN'
        
        # Return the minimum and maximum value of a column
        try:
            columnMin = df[column].min()
            columnMax = df[column].max()
        except:
            columnMin = None
            columnMax = None
            
        # Return the length of the max string
        try:
            if inferredColumnType == "VARCHAR":
                stringLength = len(columnMax)
            else:
                stringLength = None
        except:
            stringLength = None
        
        # Return the precision after the decimal
        try:
            if inferredColumnType == "DECIMAL":
                precision = len(str(columnMax).split(".")[1])
            else:
                precision = None
        except:
            precision = None
            
        # Distinct String Values
        if inferredColumnType == "VARCHAR":
            distinctValues = len(set(df[column]))
        else:
            distinctValues = None
            
        # Return the Column Mean and Standard Deviation
        if inferredColumnType == "DECIMAL" or inferredColumnType == "INT":
            columnMean = np.mean(df[column])
            columnSD = np.std(df[column])
        else:
            columnMean = None
            columnSD = None

        # Number of Missing Values
        missingValues = df[column].isnull().sum()
        percentMissing = missingValues/len(df[column])
        
        
        profileDF = profileDF.append(pd.Series([tableName, columnName, columnType, inferredColumnType, columnMin, columnMax, stringLength, precision, distinctValues, columnMean, columnSD, missingValues, percentMissing], index=profileDF.columns),ignore_index = True)
    return(profileDF)
