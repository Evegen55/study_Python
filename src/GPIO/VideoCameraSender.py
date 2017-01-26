'''
Created on Jan 26, 2017

@author: Evgenii_Lartcev
'''
from gpiozero import MotionSensor
import cv2
import telepot
import time

def Telegram_send(input_file):
 import glob
 import os
 file=max(glob.iglob(input_file+'*.jpg'),key=os.path.getctime)
 bot = telepot.Bot('*************************************')
 bot.sendMessage(*********, 'Motion detected!')
 bot.sendPhoto(*********, open(file,'rb'))

def main():
 file='/home/pi/alarms/'
 counter=0
 threshhold=10
 pir=MotionSensor(4)
 try:
  camera=cv2.VideoCapture(0)
  while counter<=threshhold:
   if pir.motion_detected:
    print("Motion detected at "+str(time.strftime("%Y%m%d-%H%M%S")))
    if not camera.isOpened():
     camera.open(0)
     result,image=camera.read()
    else:
     result,image=camera.read()
    cv2.imwrite(file+str(time.strftime("%Y%m%d-%H%M%S"))+'.jpg',image)
    counter+=1
  if counter >=threshhold: Telegram_send(file)
 except Exception as e:
  print('Something is wrong.',e)
  camera.release()

if __name__=="__main__":
 main()