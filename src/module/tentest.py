from unittest import result
import tensorflow as tf
import numpy as np
import cv2
import os
import sys
import time





def inference_from_model(model, image, threshold=None):
    img = image.copy()
    input_tensor = tf.convert_to_tensor(img)
    input_tensor = input_tensor[tf.newaxis,...]
    model_fn = model.signatures['serving_default']
    output_dict = model_fn(input_tensor)
    num_detections = int(output_dict.pop('num_detections'))
    output_dict = {key:value[0, :num_detections].numpy()
                    for key,value in output_dict.items()}
    output_dict['num_detections'] = num_detections
    output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
    if threshold is not None:
        detect_class = np.array([value for index, value in enumerate(output_dict['detection_classes'])
                                    if output_dict['detection_scores'][index] > threshold])
        detect_coord = np.array([value for index, value in enumerate(output_dict['detection_boxes'])
                                    if output_dict['detection_scores'][index] > threshold])
        if len(detect_class) == 0:
            return np.array([])
    else:
        detect_class = output_dict['detection_classes'][:4]
        detect_coord = output_dict['detection_boxes'][:4]
    return detect_class[np.argsort(detect_coord[:,1])[::-1]]

# bbox_screen = Camera.getRaw()
# image_array = np.array(bbox_screen)
image = cv2.imread("src/static/img/test.jpg")
image_array = np.array(image)
img2 = cv2.cvtColor(image_array, cv2.COLOR_BGRA2RGB)
# monitoring_screen = cv2.cvtColor(image_array, cv2.COLOR_BGRA2BGR)
# cv2.imwrite(f"src/static/img/{int(time.time())}.jpg", monitoring_screen)

pb_path = "src/Rune/saved_model"
model = tf.saved_model.load(pb_path)



with tf.device('/gpu:0'):
    results = inference_from_model(model, img2)
print("1번",results)

image = cv2.imread("src/static/img/1659009002.jpg")
image_array = np.array(image)
img2 = cv2.cvtColor(image_array, cv2.COLOR_BGRA2RGB)
# monitoring_screen = cv2.cvtColor(image_array, cv2.COLOR_BGRA2BGR)
# cv2.imwrite(f"src/static/img/{int(time.time())}.jpg", monitoring_screen)
with tf.device('/gpu:0'):
    results = inference_from_model(model, img2)
print("2번",results)
