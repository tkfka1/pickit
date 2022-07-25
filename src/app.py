from cv2 import imread
import cv2
from flask import Flask, render_template, jsonify, request ,Response , send_file
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
    return jsonify({'result': 'success', 'msg': '메이플 시작'})


# API 역할을 하는 부분
@app.route('/maple/api/stop', methods=['POST'])
def btn_stop():
    main.stop()
    return jsonify({'result': 'success', 'msg': '메이플 중지'})


# API 역할을 하는 부분
@app.route('/maple/api/screen', methods=['GET'])
def btn_screen():
    # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    screens = "{{ url_for('static', filename='img/temp.bmp') }}"
    return jsonify({'result': 'success', 'msg': screens})

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


@app.route("/image")
def image():
    return send_file('src/static/img/temp.bmp')

if __name__ == '__main__':
    img = open('src/static/img/temp.bmp', 'rb').read()
    app.run('0.0.0.0', port=5000, debug=True)