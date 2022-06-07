import colorama
from colorama import Fore
import pyodbc

#Drivers Available:
#['SQL Server', 'Microsoft Access Driver (*.mdb, *.accdb)', 'Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)', 'Microsoft Access Text Driver (*.txt, *.csv)', 'SQL Server Native Client 11.0', 'SQL Server Native Client RDA 11.0', 'ODBC Driver 17 for SQL Server']


def authenticate(conn, username, password):
    query = f"SELECT Password FROM Authentication WHERE Username='{username}';"
    cursor = conn.cursor()
    cursor.execute(query)
    authpass = "null"
    for row in cursor:
        authpass = row[0]
    return authpass == password

conn_string = "driver={SQL SERVER}; server=DESKTOP-3RAD00Q; database=UserAuth; trusted_connection=YES;"

connection = pyodbc.connect(conn_string)

print('User Authentication- ')
username = input("Username: ")
password = input("Password: ")

print("Please await authentication.")

res = authenticate(connection, username, password)

if res: 
    print(Fore.GREEN + "Authentication Successful")
else:
    print(Fore.RED + "Authentication Unsuccessful")
    
print(Fore.WHITE)
connection.close()