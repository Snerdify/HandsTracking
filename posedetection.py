import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

# Pose class - solutions.pose is a mediapipe pose class,and mp_pose is the variable that will hold the instance of that mediapipe pose detection
mp_pose=mp.solutions.pose 

# pose function for images
#static_image_mode= holds a boolean value
# gets initialized with False
# that means it is treated a a video until it is set to true
#min_detection_con= argument will set the threshold value of confidence level
# it ranges from 0.0 to 1.0 . by default the value is 0.5

pose_image = mp_pose.Pose(static_image_mode =True , min_detection_con =0.5)


#pose function for videos
#static_image_mode when set to false treats the input as video
#min_detection_con is set to 0.7
# min_tracking_confidence= detects whether a person is detected or not based on the confidence
#that we provide . this is to prevent problems of high robustness
# it is automatically ignored when static_image-mode is true


pose_video= mp_pose.Pose(static_image_mode=False,min_detection_con0.7,
                        min_tracking_con=0.7)



#initialize mediapipe drawing class to draw the landmarks

mp_drawing=mp.solutions.drawing_utils

#POSE DETECTION
# pose detection function that helps perform pose detection in a 
# modular way 

# this function will detect the person closely associated with the image
# then draw all the landmark points in the pose 

def detectPose(image_pose,pose,draw=False,display=False):


