
"""
################################# Pose Estimation on JetsonNano with Python ##############################

# This part using on JetsonNano or similar kits (Rasperry Pi etc.).
# Using 1 webcam
# Connection with Flask HTTP Server and listen requests from there
# Function returns coordinates of frame according to command by client side

"""
import sys
import time
from sys import platform
import numpy as np
import cv2 as cv
import argparse as arg
import os
from flask import Flask, jsonify,request
from openpose import pyopenpose as op
import json

cap = cv.VideoCapture(0)   # Open Camera 

###### Paramaters for openpose ##########

params = dict()
params["model_folder"] = "../../../models/"
params["net_resolution"]= "128x128"
params["number_people_max"]= "1"
# params["image_dir"] = "/home/muaz/Desktop/images/"     # if you want to execute with image 
# params["write_images"]= "/home/muaz/Desktop/photos" 
params["process_real_time"]= "false"
params["scale_number"]= "1"
params["scale_gap"]= "0.3"
params["disable_multi_thread"]= "True"

# API Server and Control System
opWrapper = op.WrapperPython()   # Global variable to start OpenPose anywhere

app = Flask(__name__)  # Flask 

@app.route('/start', methods=['GET'])
def openpose_exe():
    opWrapper.configure(params)
    opWrapper.start()
    return " OpenPose started succesfully !!"

@app.route('/Coordinates', methods=['GET'])
def get_coo():
    start = time.time()
    ret , frame = cap.read()

    if ret==True:   # Shows the real frame 
        cv.imshow("a",frame)
        cv.waitKey(1)
   
    datum = op.Datum()
    #imageToProcess = cv.imread(args[0].image_path)
    datum.cvInputData = frame  
    opWrapper.emplaceAndPop([datum])
    print((datum.poseKeypoints).shape)

    #last_img = drawLine(datum.poseKeypoints,imageToProcess)   
   
    # Get Coordinates X,Y in Order
    
    coo = getCoordinates(datum.poseKeypoints)
    print(coo)
    print(frame.shape)
    # print(last_img.shape) # Correct size
    
    end = time.time()
    print("OpenPose demo successfully finished. Total time: " + str(end - start) + " seconds")
    
    return jsonify( str(coo)+ "," + str(frame.shape))
   
# 

def drawLine(arr,img): # Draw line to new image from keypoints and returns this new image ( if you want to execute with image ) 

    """ Keypoint Locations
    //     {0,  "Nose"},      // Burun
    //     {1,  "Neck"},      // Boyun
    //     {2,  "RShoulder"}, // Omuz
    //     {3,  "RElbow"},    // Dirsek
    //     {4,  "RWrist"},    // Bilek
    //     {5,  "LShoulder"},
    //     {6,  "LElbow"},
    //     {7,  "LWrist"},
    //     {8,  "MidHip"},    // Kalça
    //     {9,  "RHip"},
    //     {10, "RKnee"},
    //     {11, "RAnkle"},    // Ayak Bileği
    //     {12, "LHip"},
    //     {13, "LKnee"},
    //     {14, "LAnkle"},
    //     {15, "REye"},
    //     {16, "LEye"},
    //     {17, "REar"},
    //     {18, "LEar"},
    //     {19, "LBigToe"},
    //     {20, "LSmallToe"},
    //     {21, "LHeel"},
    //     {22, "RBigToe"},
    //     {23, "RSmallToe"},
    //     {24, "RHeel"},       // Topuk
    //     {25, "Background"}
    // };

    """
    blank_image = np.zeros(shape=img.shape, dtype=np.uint8)

    cv.line(blank_image,(arr[0][1][0],arr[0][1][1]),(arr[0][8][0],arr[0][8][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][1][0],arr[0][1][1]),(arr[0][2][0],arr[0][2][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][1][0],arr[0][1][1]),(arr[0][5][0],arr[0][5][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][2][0],arr[0][2][1]),(arr[0][3][0],arr[0][3][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][3][0],arr[0][3][1]),(arr[0][4][0],arr[0][4][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][5][0],arr[0][5][1]),(arr[0][6][0],arr[0][6][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][6][0],arr[0][6][1]),(arr[0][7][0],arr[0][7][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][8][0],arr[0][8][1]),(arr[0][9][0],arr[0][9][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][9][0],arr[0][9][1]),(arr[0][10][0],arr[0][10][1]),(255,255,255),3) 
    cv.line(blank_image,(arr[0][10][0],arr[0][10][1]),(arr[0][11][0],arr[0][11][1]),(255,255,255),3) 
    cv.line(blank_image,(arr[0][8][0],arr[0][8][1]),(arr[0][12][0],arr[0][12][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][12][0],arr[0][12][1]),(arr[0][13][0],arr[0][13][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][13][0],arr[0][13][1]),(arr[0][14][0],arr[0][14][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][1][0],arr[0][1][1]),(arr[0][0][0],arr[0][0][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][0][0],arr[0][0][1]),(arr[0][15][0],arr[0][15][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][15][0],arr[0][15][1]),(arr[0][17][0],arr[0][17][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][0][0],arr[0][0][1]),(arr[0][16][0],arr[0][16][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][16][0],arr[0][16][1]),(arr[0][18][0],arr[0][18][1]),(255,255,255),3)  
    cv.line(blank_image,(arr[0][14][0],arr[0][14][1]),(arr[0][19][0],arr[0][19][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][19][0],arr[0][19][1]),(arr[0][20][0],arr[0][20][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][14][0],arr[0][14][1]),(arr[0][21][0],arr[0][21][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][11][0],arr[0][11][1]),(arr[0][22][0],arr[0][22][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][22][0],arr[0][22][1]),(arr[0][23][0],arr[0][23][1]),(255,255,255),3)
    cv.line(blank_image,(arr[0][11][0],arr[0][11][1]),(arr[0][24][0],arr[0][24][1]),(255,255,255),3)

    # Draw circles to speesific areas 
    # Transparent Operation
    overlay = blank_image.copy() 

    for i in range(0,24) :

        if i==19 or i==20 or i==22 or i==23 :
            continue
        else :
            cv.circle(overlay,(arr[0][i][0] ,arr[0][i][1]),10,(0,255,255),-1)
  
    opacity = 0.7
    cv.addWeighted(overlay, opacity, blank_image, 1 - opacity, 0, blank_image)

    return blank_image

def getCoordinates(arr) : # Returns coordinates as splittable from Pose Keypoints

    crd = ""

    for i in range(0,25) :
        if arr.shape != (1,25,3) :
            for i in range(0,25):
                if i==24:
                    crd+= str(0) + "," + str(0)
                else:
                    crd+= str(0) + "," + str(0) + ","
            return crd  

        elif i == 24:
            crd+= str(arr[0][i][0]) + "," + str(arr[0][i][1]) 
        else:
            crd+= str(arr[0][i][0]) + "," + str(arr[0][i][1]) + ","    
       
    return crd         

def start_server(): # Start server Flask
    app.run(debug=False,host="10.1.22.28", port =5050)

if __name__ == "__main__":

    try:
        
        start_server()
        
        ## For Image Input ## 
        
        # Store image shape 
        #img_path = "/home/muaz/Desktop/images/rightposture.jpg"
        #img = cv.imread(img_path)
        # img = frame
        # (h, w, d)= img.shape

        # if h <= 640 or w <= 480:
        #     scale_percent = 150                     # percent of original size
        #     width = int( h * scale_percent / 100) 
        #     height = int( w * scale_percent / 100) 
        #     dimension = (height, width) 

        # elif 640 < h <= 1500 or 480 < w <= 1000:
        #     scale_percent = 70 
        #     width = int( h * scale_percent / 100) 
        #     height = int( w * scale_percent / 100) 
        #     dimension = (height, width) 

        # else:
        #     scale_percent = 40 
        #     width = int( h * scale_percent / 100) 
        #     height = int( w * scale_percent / 100) 
        #     dimension = (height, width)     

        # resized = cv.resize(img, dimension, interpolation = cv.INTER_AREA)

        # filename = '/home/muaz/Desktop/images/resizedImage.jpeg'
        # cv.imwrite(filename, resized)

        # Specify Path of Image
        #parser = arg.ArgumentParser()
        #parser.add_argument("--image_path", default = filename, help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
        #args = parser.parse_known_args()

        # ../../../examples/media/COCO_val2014_000000000459.jpg 
        #  default="/home/muaz/Desktop/photos/human.jpg"
        

        # If argument is not in path, add in path .
        # for i in range(0, len(args[1])):
        #     curr_item = args[1][i]
        #     if i != len(args[1])-1: next_item = args[1][i+1]
        #     else: next_item = "1"
        #     if "--" in curr_item and "--" in next_item:
        #         key = curr_item.replace('-','')
        #         if key not in params:  params[key] = "1"
        #     elif "--" in curr_item and "--" not in next_item:
        #         key = curr_item.replace('-','')
        #         if key not in params: params[key] = next_item
            
    except Exception as ex:
        print(ex)

cap.release() # Turn off the camera
sys.exit(-1)
