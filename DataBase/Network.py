from flask import Flask
from DB_manager import DB_manager

data_manager = DB_manager()
app = Flask(__name__)

@app.route("/")
def help():
    return "온라인으로부터 카메라의 정보를 받아오는 역할을 합니다."

@app.route("/detected")
def detected():
    data_manager.update_detection("True")
    return "detected"
        
@app.route("/not_detected")
def not_detected():
    data_manager.update_detection("False")
    return "not_detected"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")