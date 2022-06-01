import pymysql as sql
from time import *

class DB_manager:
    def __init__(self):
        self.DB = sql.connect(host = 'localhost', user = 'root', password = '1234', db='store')
        self.cursor = self.DB.cursor()
    
    def update_temp(self, temp, humi):
        time_data = localtime(time())
        time_str = str(time_data.tm_mon)+"/" + str(time_data.tm_mday) + " "+str(time_data.tm_hour)+":" + str(time_data.tm_min)
        self.cursor.execute(f"insert into temp values('{time_str}','{temp}','{humi}');")
        self.DB.commit()

    def read_last_temp(self):
        self.cursor.execute("select * from temp order by datetime desc")
        result = self.cursor.fetchall()
        print(result[0])
        
    def clear_temp(self):
        self.cursor.execute("delete from temp")
        self.DB.commit()
        
    def __del__(self):
        self.DB.close()
        
        
        
        
        
        