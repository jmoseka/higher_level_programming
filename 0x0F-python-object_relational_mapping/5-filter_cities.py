#!/usr/bin/python3
"""
takes the name of a state as an argument and lists all cities of that state
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    # required arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    name = argv[4]

    # connecting to the database using 'connect()' method
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        database=database_name
    )

    # creating an instance of 'cursor' class which is used to execute
    # the 'SQL' statements in Python
    cursor = db.cursor()

    # getting all the states which are present in database
    # 'execute()' method is used to compile a 'SQL' statement
    cursor.execute("""SELECT cities.name
    FROM cities INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC""", (name,))

    # it returns list of cities present in the database
    all_cities = cursor.fetchall()

    # showing all the states one by one
    result = []
    for city in all_cities:
        result.append(city[0])
    print(", ".join(result))
    cursor.close()
    db.close()
