#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    # required arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # connecting to the database using 'connect()' method
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        database=database_name,
    )

    # creating an instance of 'cursor' class which is used to execute
    # the 'SQL'statements in Python
    cursor = db.cursor()

    # getting all the states which are present in database
    # 'execute()' method is used to compile a 'SQL' statement
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # it returns list of states present in the database
    all_states = cursor.fetchall()

    # showing all the states one by one
    for state in all_states:
        print(state)
    cursor.close()
    db.close()
