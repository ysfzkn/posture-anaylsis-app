# Description 
A program OpenPose based for posture analysis.

Program provide to watch patient's movement until the right position and save the new outline of body and angle values using Jetson Nano.

The 'server.py' can be used on any Developer Kit. And at least 1 camera must be integrated to the Kit.

The 'client.py' is for your personal computer, you can remote here all of operations on Kit.

# On Nvidia Developer Forum 
* https://forums.developer.nvidia.com/t/posture-analysis-application-using-jetson-nano/197678?u=ysfzkn58

# Demo 
Interface : 
![posture_demo](https://user-images.githubusercontent.com/58569590/113511234-89bd8080-9567-11eb-8f77-f8bfb8b6c155.jpg)

Results:
![posture_demo2](https://user-images.githubusercontent.com/58569590/113511313-ede04480-9567-11eb-95f5-af97c9c0a4aa.jpg)

Introduction Video:
* [Video Link](https://www.youtube.com/watch?v=bQAjxHcxU6A)



# Dependencies

The following are required:

* Jetson Nano with integrated camera
* python3
* [OpenPose API](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
* OpenCV (min version 2)

# Cloning and Installing Dependencies
 $ `git clone https://github.com/ysfzkn/posture-anaylsis-app/`
 
 $ `cd posture-anaylsis-app`
 
 $ `pip3 install -r requirements.txt`

# Run

* After activate the server program in Jetson Nano,
* It's just enough run this command on your PC:
* $ `python3 client.py` 
