''' 
This part using on Personal Computer for remote the server with an interface.

'''
import requests
import os
import json
import cv2 as cv
import time 
import numpy as np
from tkinter import *
from math import atan2,degrees
import math

count_front = 0
count_back = 0
count_right = 0
count_left = 0

root = Tk()
root.title('Fizyosoft Pose Estimation')
photo = PhotoImage(file = 'C:/Users/10/Desktop/icon/iconn.png')
root.iconphoto(False,photo) 
root.geometry('640x320') 
  
Label(root, text = 'Postür uygulamasına HOŞGELDİNİZ!').pack(side = TOP, pady = 10) 
  
# Allowing root window to change 
# it's size according to user's need 
root.resizable(True, True) 

def angle(p1, p2):
   
    xDiff = p2[0] - p1[0]
    yDiff = p2[1]- p1[1]
    degrees_temp = atan2(xDiff, yDiff)/math.pi*180

    if degrees_temp > 90:
        degrees_final = degrees_temp-180

    else:
        degrees_final = degrees_temp

    return degrees_final

postur = ""

def drawLine(arr,x,y,z,postur): # Draw line to new image from keypoints and returns this new image

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
    blank_image = np.zeros((x,y,z), dtype=np.uint8)

    # Draw circles to speesific areas 
    # Transparent Operation
    overlay = blank_image.copy() 

    if (postur == "on"):
        cv.line(blank_image,(int(arr[2]),int(arr[3])),(int(arr[0]),int(arr[1])),(255,255,255),3)
        cv.line(blank_image,(int(arr[4]),int(arr[5])),(int(arr[10]),int(arr[11])),(255,255,255),3)
        cv.line(blank_image,(int(arr[18]),int(arr[19])),(int(arr[24]),int(arr[25])),(255,255,255),3)
        cv.line(blank_image,(int(arr[8]),int(arr[9])),(int(arr[14]),int(arr[15])),(255,255,255),3)
        cv.line(blank_image,(int(arr[20]),int(arr[22])),(int(arr[26]),int(arr[27])),(255,255,255),3)

        cv.circle(overlay,(int(arr[0*2]) ,int(arr[0*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[1*2]) ,int(arr[1*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[2*2]) ,int(arr[2*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[5*2]) ,int(arr[5*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[7*2]) ,int(arr[7*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[9*2]) ,int(arr[9*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[12*2]) ,int(arr[12*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[10*2]) ,int(arr[10*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[13*2]) ,int(arr[13*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[19*2]) ,int(arr[19*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[22*2]) ,int(arr[22*2+1])),10,(0,255,255),-1)

        position = (int(arr[5*2]-45) ,int(arr[5*2+1])+5)
        cv.putText(blank_image,"Sol Omuz",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[12*2]-45) ,int(arr[12*2+1])+5)
        cv.putText(blank_image,"Sol Kalça",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[13*2]-45) ,int(arr[13*2+1])+5)
        cv.putText(blank_image,"Sol Diz",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[14*2]-65) ,int(arr[14*2+1])+5)
        cv.putText(blank_image,"Sol Ayak Bilegi",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[0*2]-45) ,int(arr[0*2+1])+5)
        cv.putText(blank_image,"Burun",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[19*2]-65) ,int(arr[19*2+1])+5)
        cv.putText(blank_image,"Sol Ayak Parmagi",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[1*2]-5) ,int(arr[1*2+1])+5)
        cv.putText(blank_image,"Boyun",position,cv.FONT_HERSHEY_SIMPLEX,0.5,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[2*2]+18) ,int(arr[2*2+1])+5)
        cv.putText(blank_image,"Sag Omuz",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[7*2]-45) ,int(arr[7*2+1])+5)
        cv.putText(blank_image,"Sol El Bilegi",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[10*2]+18) ,int(arr[10*2+1])+5)
        cv.putText(blank_image,"Sag Diz",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[22*2]+18) ,int(arr[22*2+1])+5)
        cv.putText(blank_image,"Sag Ayak Parmagi",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[19*2]-65) ,int(arr[19*2+1])+5)
        cv.putText(blank_image,"Sol Ayak Parmagi",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)

    elif(postur == "arka"):
        cv.line(blank_image,(int(arr[4]),int(arr[5])),(int(arr[10]),int(arr[11])),(255,255,255),3)
        cv.line(blank_image,(int(arr[18]),int(arr[19])),(int(arr[24]),int(arr[25])),(255,255,255),3)
        cv.line(blank_image,(int(arr[20]),int(arr[22])),(int(arr[26]),int(arr[27])),(255,255,255),3)

        cv.circle(overlay,(int(arr[2*2]) ,int(arr[2*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[5*2]) ,int(arr[5*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[11*2]) ,int(arr[11*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[9*2]) ,int(arr[9*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[12*2]) ,int(arr[12*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[10*2]) ,int(arr[10*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[13*2]) ,int(arr[13*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[14*2]) ,int(arr[14*2+1])),10,(0,255,255),-1)

        position = (int(arr[5*2]-45) ,int(arr[5*2+1])+5)
        cv.putText(blank_image,"Sol Omuz",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[12*2]-45) ,int(arr[12*2+1])+5)
        cv.putText(blank_image,"Sol Kalça",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[13*2]-45) ,int(arr[13*2+1])+5)
        cv.putText(blank_image,"Sol Diz",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[14*2]-65) ,int(arr[14*2+1])+5)
        cv.putText(blank_image,"Sol Ayak Bilegi",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[2*2]+18) ,int(arr[2*2+1])+5)
        cv.putText(blank_image,"Sag Omuz",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[10*2]+18) ,int(arr[10*2+1])+5)
        cv.putText(blank_image,"Sag Diz",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[11*2]+18) ,int(arr[11*2+1])+5)
        cv.putText(blank_image,"Sag Ayak Bilegi",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[9*2]+18) ,int(arr[9*2+1])+5)
        cv.putText(blank_image,"Sag Kalca",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)

    elif(postur == "sag"):
        cv.line(blank_image,(int(arr[4]),int(arr[5])),(int(arr[34]),int(arr[35])),(255,255,255),3)
        cv.line(blank_image,(int(arr[4]),int(arr[5])),(int(arr[18]),int(arr[19])),(255,255,255),3)
        cv.line(blank_image,(int(arr[18]),int(arr[19])),(int(arr[20]),int(arr[21])),(255,255,255),3)
        cv.line(blank_image,(int(arr[20]),int(arr[21])),(int(arr[22]),int(arr[23])),(255,255,255),3)

        cv.circle(overlay,(int(arr[2*2]) ,int(arr[2*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[17*2]) ,int(arr[17*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[11*2]) ,int(arr[11*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[9*2]) ,int(arr[9*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[10*2]) ,int(arr[10*2+1])),10,(0,255,255),-1)

        position = (int(arr[2*2]+18) ,int(arr[2*2+1])+5)
        cv.putText(blank_image,"Sag Omuz",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[17*2]+18) ,int(arr[17*2+1])+5)
        cv.putText(blank_image,"Sag Kulak",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[11*2]+18) ,int(arr[11*2+1])+5)
        cv.putText(blank_image,"Sag Ayak Bilegi",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[9*2]+18) ,int(arr[9*2+1])+5)
        cv.putText(blank_image,"Sag Kalca",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[10*2]+18) ,int(arr[10*2+1])+5)
        cv.putText(blank_image,"Sag Diz",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)

    elif(postur == "sol"):
        cv.line(blank_image,(int(arr[10]),int(arr[11])),(int(arr[36]),int(arr[37])),(255,255,255),3)
        cv.line(blank_image,(int(arr[10]),int(arr[11])),(int(arr[24]),int(arr[25])),(255,255,255),3)
        cv.line(blank_image,(int(arr[24]),int(arr[25])),(int(arr[26]),int(arr[27])),(255,255,255),3)
        cv.line(blank_image,(int(arr[26]),int(arr[27])),(int(arr[28]),int(arr[29])),(255,255,255),3)

        cv.circle(overlay,(int(arr[18*2]) ,int(arr[18*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[5*2]) ,int(arr[5*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[19*2]) ,int(arr[19*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[13*2]) ,int(arr[13*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[12*2]) ,int(arr[12*2+1])),10,(0,255,255),-1)
        cv.circle(overlay,(int(arr[14*2]) ,int(arr[14*2+1])),10,(0,255,255),-1)

        position = (int(arr[5*2]+18) ,int(arr[5*2+1])+5)
        cv.putText(blank_image,"Sol Omuz",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[12*2]+18) ,int(arr[12*2+1])+5)
        cv.putText(blank_image,"Sol Kalça",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[13*2]+18) ,int(arr[13*2+1])+5)
        cv.putText(blank_image,"Sol Diz",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[14*2]+18) ,int(arr[14*2+1])+5)
        cv.putText(blank_image,"Sol Ayak Bilegi",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[18*2]+18) ,int(arr[18*2+1])+5)
        cv.putText(blank_image,"Sol Kulak",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)
        position = (int(arr[19*2]+18) ,int(arr[19*2+1])+5)
        cv.putText(blank_image,"Sol Ayak Parmagi",position,cv.FONT_HERSHEY_SIMPLEX,0.8,(255, 255, 255),1, cv.LINE_AA)

    opacity = 0.7

    cv.addWeighted(overlay, opacity, blank_image, 1 - opacity, 0, blank_image)
    
    return blank_image



def start_button():

    response1 = requests.get("http://10.1.22.28:5000/start")
    myLabel= Label(root, text = "PROGRAM BAŞLATILDI,BİR KERE BAŞLATMANIZ YETERLİDİR. POSTÜR SEÇİNİZ.",fg = "purple")
    myLabel.pack()

button1 = Button(root, text="PROGRAMI BAŞLAT",command= start_button,fg = "black", bg = "green")
button1.pack()

def img_button(position):
    response2 = requests.get("http://10.1.22.28:5000/Coordinates")

    print(response2)
    print("TEPKI--------------------------")

    todos = json.loads(response2.text)
    
    splitted = todos.split(",",50)
    shape = splitted[50]
    shape =  shape[1:(len(shape)-1)]
    shape = shape.split(",")
    splitted.remove(splitted[50])

    print("Shape of photo :")
    print(shape)
    
    one = int(shape[0])
    two = int(shape[1])
    three = int(shape[2])
 
    print("...Coordinates...")

    for i in range (len(splitted)) :
        splitted[i] = float(splitted[i])
        splitted[i] = int(splitted[i])

        print(str(i) + ": %d" % splitted[i] )

    anterior_list = []
    back_list = []
    right_list = []
    left_list = []

    if (position == "on"):
        headValue = angle((int(splitted[2]),int(splitted[3])),(int(splitted[0]),int(splitted[1])))
        shoulderValue = angle((int(splitted[4]),int(splitted[5])),(int(splitted[10]),int(splitted[11])))
        pelvisValue = angle((int(splitted[18]),int(splitted[19])),(int(splitted[24]),int(splitted[25])))
        handsValue = angle((int(splitted[8]),int(splitted[9])),(int(splitted[14]),int(splitted[15])))
        kneeValue = angle((int(splitted[20]),int(splitted[22])),(int(splitted[26]),int(splitted[27])))
        anterior_list = [headValue,shoulderValue,pelvisValue,handsValue,kneeValue] 

    elif(position == "arka"):
        shoulderValueBack = angle((int(splitted[4]),int(splitted[5])),(int(splitted[10]),int(splitted[11])))
        pelvisValueBack = angle((int(splitted[18]),int(splitted[19])),(int(splitted[24]),int(splitted[25])))
        kneeValueBack = angle((int(splitted[20]),int(splitted[22])),(int(splitted[26]),int(splitted[27])))
        back_list = [shoulderValueBack,pelvisValueBack,kneeValueBack]

    elif(position == "sag"):
        headValueRight = angle((int(splitted[4]),int(splitted[5])),(int(splitted[34]),int(splitted[35])))
        shoulderValueRight = angle((int(splitted[4]),int(splitted[5])),(int(splitted[18]),int(splitted[19])))
        pelvisValueRight = angle((int(splitted[18]),int(splitted[19])),(int(splitted[20]),int(splitted[21])))
        kneeValueRight = angle((int(splitted[20]),int(splitted[21])),(int(splitted[22]),int(splitted[23])))
        right_list = [headValueRight,shoulderValueRight,pelvisValueRight,kneeValueRight]

    elif(position == "sol"):
        headValueLeft = angle((int(splitted[10]),int(splitted[11])),(int(splitted[36]),int(splitted[37])))
        shoulderValueLeft = angle((int(splitted[10]),int(splitted[11])),(int(splitted[24]),int(splitted[25])))
        pelvisValueLeft = angle((int(splitted[24]),int(splitted[25])),(int(splitted[26]),int(splitted[27])))
        kneeValueLeft = angle((int(splitted[26]),int(splitted[27])),(int(splitted[28]),int(splitted[29])))
        left_list = [headValueLeft,shoulderValueLeft,pelvisValueLeft,kneeValueLeft]
    
    #######

    anterior_list_names = ["headValue","shoulderValue","pelvisValue","handsValue","kneeValue"]
    back_list_names = ["shoulderValueBack","pelvisValueBack","kneeValueBack"]
    right_list_names = ["headValueRight","shoulderValueRight","pelvisValueRight","kneeValueRight"]
    left_list_names = ["headValueLeft","shoulderValueLeft","pelvisValueLeft","kneeValueLeft"]
   
    #######

    ####### Writing angles to TXT 

    image = drawLine(splitted,one,two,three,postur)
    desktop = os.path.expanduser("~/Desktop")
    file = ""

    if not os.path.exists(desktop + "\\images"):
        os.mkdir(desktop + "\\images")

    if (position == "on"):
        path = desktop + "\\image\\foto_on_"+str(count_front)+".jpeg"
        file = "acilar_on_"+str(count_front)+".txt"
    elif (position == "arka"):
        path = desktop + "\\image\\foto_arka_"+str(count_back)+".jpeg"
        file = "acilar_arka_"+str(count_back)+".txt"
    elif (position == "sag"):
        path = desktop + "\\image\\foto_sag_"+str(count_right)+".jpeg"
        file = "acilar_sag_"+str(count_right)+".txt"
    elif (position == "sol"):
        path = desktop + "\\image\\foto_sol_"+str(count_left)+".jpeg"
        file = "acilar_sol_"+str(count_left)+".txt"

    if not os.path.exists(desktop + "\\angles"):
        os.mkdir(desktop + "\\angles")

    ang_path = desktop + "\\angles\\"
  
    with open(os.path.join(ang_path, file), 'w') as fp: 
        
        if (position == "on"): 
            for i in range(len(anterior_list)):
                if (anterior_list[i] > 0) :
                    fp.write(" '%25s' : %5.5f derece sola egik" % ((anterior_list_names[i]),(anterior_list[i])))
                    fp.write("\n ------------------------------------------------------------\n")
                elif (anterior_list[i] < 0) :
                    fp.write(" '%25s' : %5.5f derece saga egik" % ((anterior_list_names[i]),(anterior_list[i])))
                    fp.write("\n ------------------------------------------------------------\n")

        elif (position == "arka"):
            for i in range(len(back_list)):
                if (back_list[i] > 0 ):
                    fp.write(" '%25s' : %5.5f derece sola egik" % ((back_list_names[i]) , (back_list[i])))
                    fp.write("\n ------------------------------------------------------------ \n")
                elif (back_list[i] < 0 ):
                    fp.write(" '%25s' : %5.5f derece saga egik" % ((back_list_names[i]) , (back_list[i])))
                    fp.write("\n ------------------------------------------------------------ \n")

        elif (position == "sag"):
             for i in range(len(right_list)):
                if (right_list[i] > 0 ):
                    fp.write(" '%25s' : %5.5f derece sola egik" % ((right_list_names[i]) , (right_list[i]) ))
                    fp.write("\n ------------------------------------------------------------ \n")
                elif (right_list[i] < 0 ):
                    fp.write(" '%25s' : %5.5f derece saga egik" % ((right_list_names[i]) , (right_list[i]) ))
                    fp.write("\n ------------------------------------------------------------ \n")

        elif (position == "sol"):
             for i in range(len(left_list)):
                if (left_list[i] > 0 ):
                    fp.write(" '%25s' : %5.5f derece sola egik" % ((left_list_names[i]) , (left_list[i]) ))
                    fp.write("\n ------------------------------------------------------------ \n")
                elif (left_list[i] < 0 ):
                    fp.write(" '%25s' : %5.5f derece saga egik" % ((left_list_names[i]) , (left_list[i]) ))
                    fp.write("\n ------------------------------------------------------------ \n")


        fp.close()

    
    cv.imwrite(path,image)
    width = int(image.shape[1] * 50 / 100)
    height = int(image.shape[0] * 50 / 100)
    dim = (width, height)

    # Resize image
    image = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    
    cv.imshow("Onizleme",image)

    cv.waitKey(1)

    myLabel= Label(root, text = "Postür başarıyla analiz edildi.Fotoğraf Masaüstü/image klasörüne kaydedildi.",fg="purple")
    myLabel.pack()

## Counter Functions

def front():
    global postur
    postur = "on"

    global count_front
    count_front += 1

    print("ON calıstı")
    img_button(postur)

def back():
    global postur
    postur = "arka"

    global count_back
    count_back += 1

    print("ARKA calıstı")
    img_button(postur)

def right():
    global postur
    postur = "sag"

    global count_right
    count_right += 1

    print("SAG calıstı")
    while 1 :
        img_button(postur)

def left():
    global postur
    postur = "sol"

    global count_left
    count_left += 1

    print("SOL calıstı")
    img_button(postur)

##### Buttons ########

button2 = Button(root, text="ÖN POSTÜR",command= front,fg = "blue", bg ="yellow")
button2.pack()

button3 = Button(root, text="ARKA POSTÜR",command= back,fg = "blue", bg ="yellow")
button3.pack()

button4 = Button(root, text="SAĞ POSTÜR",command= right,fg = "blue", bg ="yellow")
button4.pack()

button5 = Button(root, text="SOL POSTÜR",command= left,fg = "blue", bg ="yellow")
button5.pack()

button_quit = Button(root,text = "ÇIKIŞ",command = root.quit,fg = "black",bg ="purple")
button_quit.pack()


root.mainloop()
