"""
In this file we will create a database connection with the ms-sql database

DB Type: Microsoft sql
Database name: Assignment3_Flask

"""


import pyodbc
import logging
logging.basicConfig(filename='C:/Users/imtah/Documents/ai_in_es/Final_project_chatbot/logs/dbconnection.log', encoding='utf-8', level=logging.INFO)


def connection():

    try:
        connection_string = "DRIVER={SQL Server}; SERVER=TAHSEEN; DATABASE=final_project;"
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        logging.info("Connection successful")
        print("Connection completed!")
        return cursor

    except Exception as error:
        print(error)



