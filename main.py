import pyodbc

#Drivers Available:
#['SQL Server', 'Microsoft Access Driver (*.mdb, *.accdb)', 'Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)', 'Microsoft Access Text Driver (*.txt, *.csv)', 'SQL Server Native Client 11.0', 'SQL Server Native Client RDA 11.0', 'ODBC Driver 17 for SQL Server']

conn_string = "driver={SQL SERVER}; server=DESKTOP-3RAD00Q; database=UserAuth; trusted_connection=YES;"

connection = pyodbc.connect(conn_string)

print(connection)