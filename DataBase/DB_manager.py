import pymysql as sql
from time import *

class DB_manager:
    def __init__(self,ip = 'localhost'):
        self.DB = sql.connect(host = ip, port = 3306, user = 'root', password = '1234', db='store')
        self.cursor = self.DB.cursor()

    @staticmethod
    def time():
        time_data = localtime(time())
        milisec = f"{int(time()*100)%100:2}"
        time_str = str(time_data.tm_mon)+"/" + str(time_data.tm_mday) + " "+str(time_data.tm_hour)+":" + f"{time_data.tm_min:2}" + ":" + f"{time_data.tm_sec:2}" + "/"+ milisec
        return time_str

    def update(self, DB_name, *args):
        time_str = self.time()
        arg_string = ""
        for i in args:
            arg_string += "," + str(i)
        self.cursor.execute(f"insert into {DB_name} values('{time_str}'{arg_string});")
        self.DB.commit()

    def read_last(self,DB_name):
        self.cursor.execute(f"select * from {DB_name} order by datetime desc")
        result = self.cursor.fetchall()
        return result

    def clear(self, DB_name):
        self.cursor.execute(f"delete from {DB_name}")
        self.DB.commit()

    def command(self,command):
        self.cursor.execute(command)
        
        
        
        
        
        
        