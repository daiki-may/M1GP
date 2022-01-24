from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)
socketio = SocketIO(app)

# response_data = {"book": 3, "bottle": 2}

@app.route("/")
def hello():
    # response = yolo_video_func()
    json_open = open('/Users/daiki-may/Desktop/M1GP/newkeras-yolo3/test.json', 'r')
    json_data = json.load(json_open)
    print(json_data)
    return jsonify(json_data)

@app.route("/aroma_web")
def aroma():
    return render_template("aroma.html")

@app.route("/fatigue", methods=["POST"])
def fatigue():
    print(request.data)
    socketio.emit('from_server', 0, broadcast=True)
    return request.data

@socketio.on("from_ios")
def from_ios(data):
    print("---------------------------------from-ios---------------------------------------------------")
    print(data)
    socketio.emit("to_browser", data, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
