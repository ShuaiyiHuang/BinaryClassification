# import cv2

# fileName = 'D:/Baidu/BaiduDownload/20170712/2017-07-12-105036.mov'
# cap = cv2.VideoCapture(fileName)

# # weight = cap.get(3) #weight
# # height = cap.get(4) #height
# # fps = cap.get(5) #fps
# # frame_count = cap.get(7) #frame count

# # print('weight,height:' + str(weight) + ',' + str(height))
# # print('fps:' +  str(fps))
# # print('frame_count:' + str(frame_count))

# ret,frame1 = cap.read()
# win = cv2.namedWindow('frame 1', flags=0) 
# cv2.imshow('frame 1', frame1) 

# cap.set(1,12000)
# ret,frame200 = cap.read()
# win = cv2.namedWindow('frame 8000', flags=0) 
# cv2.imshow('frame 8000', frame200) 

# ret,frame200 = cap.read()
# win = cv2.namedWindow('frame 8000', flags=0) 
# cv2.imshow('frame 8000', frame200) 


# # ret,frame = cap.read()

# # win = cv2.namedWindow('frame win', flags=0) 
# # cv2.imshow('frame win', frame) 

# # image = cv2.resize(frame,(600,400))
# # win = cv2.namedWindow('image win', flags=0) 
# # cv2.imshow('image win', image) 

# cv2.waitKey(0)

# cap.release()  
# cv2.destroyAllWindows()

###################################################

import os
import os.path
rootdir = 'D:/Baidu/BaiduDownload/20170712'                                   # 指明被遍历的文件夹

for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for dirname in dirnames:                       #输出文件夹信息
        print("parent is:" + parent)
        print("dirname is:" + dirname)

    for filename in filenames:                        #输出文件信息
        print("parent is:" + parent)
        print("filename is:" + filename)
        print("the full name of the file is:" + os.path.join(parent,filename)) #输出文件路径信息


from generator import *
videoName = 'D:/Baidu/BaiduDownload/2017-07-13/2017-07-13 151123.mov' 
saveRoot = 'D:/Baidu/BaiduDownload/20170712/data/2017-07-13-151123'
filePrefix = ''
generateData(videoName, saveRoot, filePrefix)

from generator import *
targetFileName = '2017-07-13-151123-test.txt'
rootDir = saveRoot
label = 1
generateTxt(targetFileName, rootDir, label)