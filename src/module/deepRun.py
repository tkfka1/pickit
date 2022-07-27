import os
#import sys
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

#기본 모델의 경로
model = load_model('src/run/RuneAuto.h5')
#기본 이미지 경로
img_dir = 'src/run/'
#룬저장
rn = ''

#룬 판독  룬사진=인푸토  결과값=리턴 0=아래 1=왼쪽 2=오른쪽 3=위
def runeDetec(*inputo):
    results = []
    for input in inputo:
        image1 = cv2.imread(input, cv2.IMREAD_COLOR)
        with tf.device('/cpu:0'):
            output = model.predict_classes(np.expand_dims(image1,axis=0))
        results.append(output[0])
    results = np.array(results)    
    return(results)

    # 룬 이미지  경로=img_dir 받고 룬 사진 찾아서 하나씩 룬판독하기
def runPath():
    i = 1
    rn = ''
    filenam = os.listdir(img_dir)
    png_nam = [file for file in filenam if file.endswith(".png")]
    for inimg in png_nam:
        x = runeDetec(img_dir+inimg)
        x = x[0]
        rn = (rn + str(x))       
        i = i+1        
    print(rn)
    with open("src/run/rn.txt", mode="w") as file:
        file.write(rn)

#실행되면 시작
if __name__ == "__main__":
    runPath()
#    sys.exit()



