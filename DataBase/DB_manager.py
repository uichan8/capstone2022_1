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
        self.cursor.execute("select * from temp order by time desc limit 1")
        data = self.cursor.fetchall()
        temp = None  #데이타 가공 해야됨
        humi = None
        return temp,humi

    def update_detection(self,val):
        #db만들것
        pass
        
    def __del__(self):
        self.DB.close()
        
        
        
        
        
        