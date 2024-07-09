import mysql.connector
from mysql.connector import Error
import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET


try:
    myconn = mysql.connector.connect(host="127.0.0.1", user="phpmyadmin", passwd="dbconfig123", database="bda_assignments")

    if myconn.is_connected():
        db_Info = myconn.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = myconn.cursor()

        select_query = "select * from pokemondata"
        cursor.execute(select_query)
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row\n")
        my_dic = []
        for row in records:
            temp = {
                'name': row[0],
                'move1': row[1],
                'move2': row[2]
            }
            my_dic.append(temp)

        with open("pokemondata.json", "w") as final:
            json.dump(my_dic, final)

            
        root = ET.Element("pokemons")

        for item in my_dic:
            pokemon = ET.SubElement(root, "pokemon")
            for key, value in item.items():
                child = ET.SubElement(pokemon, key)
                child.text = value

        tree = ET.ElementTree(root)
        tree.write("pokemondata.xml", encoding="utf-8", xml_declaration=True)


except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if myconn.is_connected():
        cursor.close()
        myconn.close()
        print("MySQL connection is closed")

