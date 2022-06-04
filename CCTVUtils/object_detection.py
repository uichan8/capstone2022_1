from openvino.inference_engine import IECore
from time import time

import cv2
import numpy as np

from CCTVUtils.DetectionUtils.preprocess import preprocess
from CCTVUtils.DetectionUtils.demo_process import demo_process
from CCTVUtils.DetectionUtils.nms import multi_nms
from CCTVUtils.DetectionUtils.visualize import visualize

from DataBase.DB_manager import DB_manager

def realtime_detection():
    #camera setting
    cap = cv2.VideoCapture(0)
    et_val, frame = cap.read()
    cv2.imshow("img", frame)
    cv2.waitKey(0) == 24

    #DataBase setting
    db = DB_manager(ip = '192.168.75.20')
    db.clear_camera()
    db.update_camera('0', '0')

    #NCS2 setting
    ie = IECore()
    model      = ie.read_network(model='yolox_tiny.xml', weights = 'yolox_tiny.bin')
    network    = ie.load_network(network=model, device_name='MYRIAD')
    input_key  = list(network.input_info)[0]
    output_key = list(network.outputs.keys())[0]

    #input image args
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    image_shape = (width,height)
    input_shape = (416,416)

    #args
    classes = ["person", "bicycle", "car"]
    score_thr = 0.7
    nms_thr = 0.7
    past_state = 0
    val = 0
    count = 0
    wait = 5*5

    while True:
        start = time()
        #read image from camera
        ret_val, frame = cap.read()
        if ret_val == False:
            break

        #process image
        img,ratio = preprocess(frame,input_shape)
        img = img[np.newaxis, ...]

        #inference
        output = network.infer(inputs={input_key: img})
        output = output[output_key]
        
        #demo processing
        predict = demo_process(output,input_shape)[0]
        
        boxes = predict[:, :4]
        scores = predict[:, 4:5] * predict[:, 5:8]
        
        #xywh2xyxy
        boxes_xyxy = np.ones_like(boxes)
        boxes_xyxy[:, 0] = boxes[:, 0] - boxes[:, 2]/2.
        boxes_xyxy[:, 1] = boxes[:, 1] - boxes[:, 3]/2.
        boxes_xyxy[:, 2] = boxes[:, 0] + boxes[:, 2]/2.
        boxes_xyxy[:, 3] = boxes[:, 1] + boxes[:, 3]/2.
        boxes_xyxy /= ratio
        
        #NMS
        detection_result = multi_nms(boxes_xyxy, scores, nms_thr, score_thr)
        
        #bounding_box
        frame = visualize(frame, detection_result[:, :4], detection_result[:, 4], detection_result[:, 5], conf=score_thr, class_names=classes)
        
        #update state
        if np.max(detection_result[:, 4] >= score_thr):
            present_state = 1
            count = 0
        elif count < wait:
            count += 1
        else:
            present_state = 0
        
        #write DB
        if past_state != present_state:
            db.update_camera(f'{present_state}',f'{present_state}',f'{val}')
            
        past_state = present_state
        val += 1
        val %= 10

        #print_image
        cv2.imshow("img", frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
        
        end = time()
        print(1/(end-start))