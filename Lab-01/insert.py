import json
import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="phpmyadmin",
        passwd="dbconfig123",
        database="bda_assignments"
    )

    if mydb.is_connected():
        cursor = mydb.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS animes (
          id INT AUTO_INCREMENT PRIMARY KEY,
          Name VARCHAR(255),
          Author VARCHAR(255),
          Since VARCHAR(255)
        )
        """
        cursor.execute(create_table_query)
        mydb.commit()

        with open("animedata.json", "r") as json_file:
            data = json.load(json_file)

        insert_stmt = """INSERT INTO animes (Name, Author, Since) VALUES (%s, %s, %s)"""

        for item in data:
            name = item.get("Name")
            author = item.get("Author")
            since = item.get("Since")
            cursor.execute(insert_stmt, (name, author, since))

        mydb.commit()

        print("Data imported successfully!")

except Error as e:
    print("Error while connecting to MySQL", e)
    
finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection is closed")
