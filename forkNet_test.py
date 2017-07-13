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
#caffe_model='D:/txADs/models/embeddingfrom256/txads_model_embedding_iter_190000.caffemodel'  
caffe_model =  model_root + 'data/xxxxx.caffemodel'

caffe.set_mode_gpu()
caffe.set_device(0);
net = caffe.Net(net_file,caffe_model,caffe.TEST)

#读取数据，并让网络前向传播
#data:n*c*h*w


net.blobs['data'].data[...] = imagedata[...]
output = net.forward()
prob = output['prob'][...,0]






caffe.reset_all()




