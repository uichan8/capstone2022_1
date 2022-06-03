from DataBase.DB_manager import DB_manager
from LightUtil.Ceilling import Ceilling
from LightUtil.Sign import Sign

def check_db():
    db = DB_manager(ip = '192.168.75.20')
    db.update_camera('1','1')
    print(db.read_last_camera())
    db.clear_camera()
    print(db.read_last_camera())

def check_light():
    ceilling = Ceilling([18],[23],[25])
    sign = Sign([16],[20])
    objects = [ceilling, sign]

    [object.on_mode() for object in objects]
    input()
    [object.off_mode() for object in objects]
    input()
    [object.eco_mode() for object in objects]

def check_sendor():
    pass


if __name__ == '__main__':
    check_db()
