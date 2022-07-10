from this import d
from CCTVUtils.object_detection import realtime_detection
from DataBase.DB_manager import DB_manager

if __name__ == '__main__':
    db = DB_manager()
    table_name = None
    db.update(table_name,0)
    realtime_detection("192.168.0.4")
    db.update(table_name,15)