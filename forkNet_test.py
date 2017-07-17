import numpy as np
import scipy as sp
import sys
caffe_root = 'F:/DeepLearning/Caffe/caffe/'

sys.path.insert(0, caffe_root + 'python')

import caffe
import scipy.io


model_root = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/'
# 设置网络结构  
net_file = model_root + 'forklift_classification_deploy.prototxt'  
# 添加训练之后的参数  
caffe_model =  model_root + 'models/forknet_train_iter_1378.caffemodel'

caffe.set_mode_gpu()
caffe.set_device(0);
net = caffe.Net(net_file,caffe_model,caffe.TEST)

import cv2
#读取数据，并让网络前向传播
#data:n*c*h*w
# image_file = model_root+'test/Negtive_672.jpg'

#need modification
testTxt = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/negtive-test.txt'
probThreadhold = 0.99
middle_dir = 'negtive-test'

testFile = open(testTxt,'r')
lines = testFile.readlines()
lineNum = len(lines)
count = 0 # count for p>0.5, p is probility of correct classification

import os
import os.path
import datetime

reocrd_root = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/test/' + str(middle_dir) + '/'
recordTxt = reocrd_root + 'failLessThan' + str(probThreadhold) + '.txt'
if not os.path.exists(reocrd_root):
  os.makedirs(reocrd_root)
recordFile = open(recordTxt,'w')

recordIndxList = []

begin = datetime.datetime.now()

for line in lines:
  image_file = line.split(' ')[0]
  image = cv2.imread(image_file)
  imagedata = cv2.resize(image,(227,227))
  indx = int(image_file.split('_')[-1].split('.')[0])

  net.blobs['data'].data[0,0,...] = imagedata[...,0]
  net.blobs['data'].data[0,1,...] = imagedata[...,1]
  net.blobs['data'].data[0,2,...] = imagedata[...,2]

  output = net.forward()
  prob = output['prob'][0,0]
  if prob > probThreadhold:
    count += 1
  else:
    recordIndxList.append(indx)
    print('fail indx:' + str(indx))

end = datetime.datetime.now()
print('elapsed time: '+str(end - begin))

recordFile.write('sameple count: ' + str(lineNum) + '\n')
recordFile.write('rate: ' + str(count/lineNum) + '\n')
recordIndxList.sort()
for i in recordIndxList:
  recordFile.write('indx: ' + str(i) + '\n')

testFile.close()
recordFile.close()

print('rate:' + str(count/lineNum))



cv2.waitKey(0)


# caffe.reset_all()




