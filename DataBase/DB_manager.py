import pymysql as sql
from time import *

class DB_manager:
    def __init__(self,ip = 'localhost'):
        self.DB = sql.connect(host = ip, port = 3306, user = 'root', password = '1234', db='store')
        self.cursor = self.DB.cursor()
    
    #for temp table
    def update_temp(self, temp, humi):
        time_data = localtime(time())
        time_str = str(time_data.tm_mon)+"/" + str(time_data.tm_mday) + " "+str(time_data.tm_hour)+":" + str(time_data.tm_min) + ":" + str(time_data.tm_sec)
        self.cursor.execute(f"insert into temp values('{time_str}','{temp}','{humi}');")
        self.DB.commit()

    def read_last_temp(self):
        self.cursor.execute("select * from temp order by datetime desc")
        result = self.cursor.fetchall()
        print(result[0])
        
    def clear_temp(self):
        self.cursor.execute("delete from temp")
        self.DB.commit()

    #for camera table
    def update_camera(self, outcamera, incamera , val):
        """camera state must be boolean"""
        time_data = localtime(time())
        time_str = str(time_data.tm_mon)+"/" + str(time_data.tm_mday) + " "+str(time_data.tm_hour)+":" + str(time_data.tm_min) + ":" + str(time_data.tm_sec) + str(val)
        self.cursor.execute(f"insert into camera values('{time_str}','{outcamera}','{incamera}');")
        self.DB.commit()

    def read_last_camera(self):
        self.cursor.execute("select * from camera order by datetime desc")
        result = self.cursor.fetchall()
        return result[0][1],result[0][2]
        
    def clear_camera(self):
        self.cursor.execute("delete from camera")
        self.DB.commit()

    #for illu table
    def update_illu(self, outillu, inillu):
        time_data = localtime(time())
        time_str = str(time_data.tm_mon)+"/" + str(time_data.tm_mday) + " "+str(time_data.tm_hour)+":" + str(time_data.tm_min) + ":" + str(time_data.tm_sec)
        self.cursor.execute(f"insert into illuminance values('{time_str}','{outillu}','{inillu}');")
        self.DB.commit()

    def read_last_illu(self):
        self.cursor.execute("select * from illuminance order by datetime desc")
        result = self.cursor.fetchall()
        print(result[0])
        
    def clear_illu(self):
        self.cursor.execute("delete from illuminance")
        self.DB.commit()
        
        
        
        
        
        
        