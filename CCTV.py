from CCTVUtils.object_detection import realtime_detection
from DataBase.DB_manager import DB_manager

if __name__ == '__main__':
    db = DB_manager("192.168.0.11")
    table_name = 'camera_power'
    db.update(table_name,15)
    realtime_detection("192.168.0.11")
    db.update(table_name,0)