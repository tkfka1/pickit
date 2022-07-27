import cv2
from flask import Flask, render_template, jsonify, request ,Response
import main
import time
from module.camera import Camera

app = Flask(__name__)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# HTML 화면 보여주기 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/maple')
def maple():
    return render_template('maple.html')

# API 역할을 하는 부분
@app.route('/maple/api/start', methods=['POST'])
def btn_start():
    main.start()
    return jsonify()

# API 역할을 하는 부분
@app.route('/maple/api/stop', methods=['POST'])
def btn_stop():
    main.stop()
    return jsonify({'result': 'success', 'msg': '메이플 중지'})

# API 역할을 하는 부분
@app.route('/maple/api/test1', methods=['POST'])
def btn_test1():
    main.test1()
    return jsonify({'result': 'success', 'msg': 't1'})

# API 역할을 하는 부분
@app.route('/maple/api/test2', methods=['POST'])
def btn_test2():
    main.test2()
    return jsonify({'result': 'success', 'msg': 't2'})

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



# # API 역할을 하는 부분
# @app.route('/api/list', methods=['GET'])
# def show_stars():
#     return jsonify({'result': 'success', 'msg': 'list 연결되었습니다!'})


# @app.route('/api/like', methods=['POST'])
# def like_star():
#     return jsonify({'result': 'success', 'msg': 'like 연결되었습니다!'})


# @app.route('/api/delete', methods=['POST'])
# def delete_star():
#     return jsonify({'result': 'success', 'msg': 'delete 연결되었습니다!'})



if __name__ == '__main__':

    app.run('0.0.0.0', port=5000, debug=True)