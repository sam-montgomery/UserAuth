import pyodbc
#Script created to provide 5 username and password combinations to the database.
conn_string = "driver={SQL SERVER}; server=DESKTOP-3RAD00Q; database=UserAuth; trusted_connection=YES;"

connection = pyodbc.connect(conn_string)

user_names = ['jsmith', 'phalford', 'bkeating', 'jlee', 'rsands']
pass_words = ['jspass', 'phpass', 'bkpass', 'jlpass', 'rspass']

def create_account(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Authentication(Username, Password) values(?,?);", (username, password))
    conn.commit()
    
    
for i in range(0, 5):
    create_account(connection, user_names[i], pass_words[i])
    
connection.close()