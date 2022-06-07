from cgitb import reset
import pyodbc
import unittest
import auth

class TestAuthMethod(unittest.TestCase):
    #Script created to verify authentication method.

    def test_valid_combination(self):
        conn_string = "driver={SQL SERVER}; server=DESKTOP-3RAD00Q; database=UserAuth; trusted_connection=YES;"
        connection = pyodbc.connect(conn_string)
        res = auth.authenticate(connection, 'bkeating', 'bkpass')
        self.assertTrue(res)

    def test_invalid_password(self):
        conn_string = "driver={SQL SERVER}; server=DESKTOP-3RAD00Q; database=UserAuth; trusted_connection=YES;"
        connection = pyodbc.connect(conn_string)
        res = auth.authenticate(connection, 'bkeating', 'invalpass')
        self.assertFalse(res)

    def test_invalid_combination(self):
        conn_string = "driver={SQL SERVER}; server=DESKTOP-3RAD00Q; database=UserAuth; trusted_connection=YES;"
        connection = pyodbc.connect(conn_string)
        res = auth.authenticate(connection, 'invaluser', 'invalpass')
        self.assertFalse(res)

    def test_no_credentials(self):
        conn_string = "driver={SQL SERVER}; server=DESKTOP-3RAD00Q; database=UserAuth; trusted_connection=YES;"
        connection = pyodbc.connect(conn_string)
        res = auth.authenticate(connection, '', '')
        self.assertFalse(res)
    
if __name__ == '__main__':
    unittest.main()