
import psycopg2
from config import config


class DataBase:
    
    params = config()

    def __init__(self):
        self.conn = psycopg2.connect(**self.params)
        self.cur = self.conn.cursor()

    def what_version(self):
        """ """
        
        sql = ''' SELECT version() '''
        try:
            self.cur.execute(sql)
            res = self.cur.fetchone()
            print(res)
            self.cur.close()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def create_tables(self, commands):
        """ """

        try:
            for command in commands:
                self.cur.execute(command)
            self.cur.close()
            self.conn.commit()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
    
    def select_id_resource(self):
        """ """
        
        sql = """SELECT id FROM resource""" 
        try:
            self.cur.execute(sql)
            res = self.cur.fetchone()[0]
            self.cur.close()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
        return res
    # доделать
    
    def insert_world(self, data_word):
        """ """
        
        sql = """INSERT INTO word(id_resource, word, count_word) VALUES(%s, %s, %s) ON CONFLICT (id_resource, word, count_word) DO NOTHING; """
        try:
            self.cur.executemany(sql, data_word)
            self.conn.commit()
            self.cur.close() 
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()


#conn = DataBase()
#conn.what_version()

        
     

