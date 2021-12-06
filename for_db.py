

from db_obj.db import DataBase
from config import config


def db_version():
    """ """
    conn_db = DataBase()
    conn_db.what_version()


def create_table():
    """ Create tbale for database popeng """ 

    commands = (
        """
        CREATE TABLE resource(
            id serial,
            title varchar NOT NULL,
            discription varchar,
            url varchar NOT NULL, 
            PRIMARY KEY (id),
            UNIQUE (url)
            )
        """,
        """
        CREATE TABLE word(
            id serial,
            id_resource int,
            word varchar,
            count_word varchar, -- количество употреблений слова в документе 
            PRIMARY KEY(id_word), 
            FOREIGN KEY(id)
                REFERENCES resource(id),
            UNIQUE(id_resource, word, count_word)
           ) 
        """
        )
    
    
    conn_db = DataBase()
    conn_db.create_tables(commands)
   
if __name__ == '__main__':
    
    db_version()
    create_table()
