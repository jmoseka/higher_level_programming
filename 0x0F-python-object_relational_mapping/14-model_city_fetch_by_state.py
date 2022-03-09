#!/usr/bin/python3
"""lists all State objects from the database with ORM"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == '__main__':
    # required arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password,
                                   database_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    joins_bd = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)
    for city, state in joins_bd.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
