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
caffe_model =  model_root + 'models/forknet_train_iter_2800.caffemodel'

caffe.set_mode_gpu()
caffe.set_device(0);
net = caffe.Net(net_file,caffe_model,caffe.TEST)

import cv2
#读取数据，并让网络前向传播
#data:n*c*h*w
# image_file = model_root+'test/Negtive_672.jpg'
# image_file = 'C:/Users/Trainer/Desktop/Negtive_18276-2.jpg'
# image_file = 'D:/Baidu/BaiduDownload/20170712/data/positive-test/2017-07-13-151607_492.jpg'
image_file = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-17-074648/2017-07-17-074648_6450.jpg'
image = cv2.imread(image_file)
imagedata = cv2.resize(image,(227,227))

net.blobs['data'].data[0,0,...] = imagedata[...,0]
net.blobs['data'].data[0,1,...] = imagedata[...,1]
net.blobs['data'].data[0,2,...] = imagedata[...,2]

output = net.forward()
prob = output['prob'][0,0]
print(prob)
prob = output['prob'][0,1]
print(prob)


cv2.waitKey(0)


# caffe.reset_all()




