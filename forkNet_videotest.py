import numpy as np
import sys
caffe_root = 'F:/DeepLearning/Caffe/caffe/'

sys.path.insert(0, caffe_root + 'python')

import caffe


model_root = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/'

net_file = model_root + 'forklift_classification_deploy.prototxt'  

caffe_model =  model_root + 'models/forknet_train_iter_1378.caffemodel'

caffe.set_mode_gpu()
caffe.set_device(0);
net = caffe.Net(net_file,caffe_model,caffe.TEST)

import cv2
import math
import matplotlib.pyplot as plt

#need modification
video_file = 'D:/Baidu/BaiduDownload/2017-07-13/2017-07-13 151607.mov'
probThreadhold = 0.9


cap = cv2.VideoCapture(video_file)
fps = cap.get(5) #fps
lastFrameId = cap.get(7) #frame count

isMoothing = True
smoothRange = 3  #actual range is 3*2+1
sampleRate = math.ceil(fps/2)
frameCount = 0

sampleWeight = 227
sampleHeight = 227

frameRecList = []
probRecList = []
workingFrameCount = 0

import datetime
begin = datetime.datetime.now()

while cap.isOpened():
  ret,frame = cap.read()

  frameCount += 1
  if frameCount <= lastFrameId:
    if frameCount % sampleRate == 0:
      imagedata = cv2.resize(frame,(sampleWeight,sampleHeight))
      net.blobs['data'].data[0,0,...] = imagedata[...,0]
      net.blobs['data'].data[0,1,...] = imagedata[...,1]
      net.blobs['data'].data[0,2,...] = imagedata[...,2]
      output = net.forward()
      prob0 = output['prob'][0,1]

      frameRecList.append(frameCount/fps)
      probRecList.append(prob0)

      print('process frame: ' + str(frameCount))
      
      if prob0 > probThreadhold:
        workingFrameCount += sampleRate
  else:
    break

end = datetime.datetime.now()
print('elapsed time: '+str(end - begin))

recFrameNum = len(frameRecList)

#smoothing
if isMoothing:
  indx = smoothRange
  probRecArray = np.array(probRecList)
  while indx < recFrameNum-smoothRange:
    meanVal = np.mean(probRecArray[indx-smoothRange:indx+smoothRange])
    if meanVal > 0.5:
      if probRecList[indx] <= probThreadhold:
        workingFrameCount += sampleRate

      probRecList[indx] = np.max((0.9,probRecList[indx]))

    indx += 1


workingTime = workingFrameCount/fps
totalTime = lastFrameId/fps

plt.figure(1)
plt.plot(frameRecList, probRecList, color="blue")
plt.axhline(0.9)
cotent = 'work ' + str(round(workingTime,2)) + ' s, ' \
 + 'working rate: ' + str(round(workingTime/totalTime*100,2)) + '%'
plt.text(0, 1.1, '' + cotent, fontsize = 15)
plt.show()

print('working rate:' + str(workingTime/totalTime))


# recFrameNum = len(frameRecList)
recordFile = open('recordFile.txt','w+')
indx = 0
while indx < recFrameNum:
    recordFile.write('frame: ' + str(math.ceil(frameRecList[indx]*fps)) + ' ' + str(round(probRecList[indx],4)) + '\n')
    indx += 1

recordFile.close()


