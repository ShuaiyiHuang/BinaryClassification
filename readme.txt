1.把生成得到的train.txt，validate.txt复制到该目录下
2.训练命令
%caffe_root%/build/tools/Release/caffe.exe train --solver=F:/DeepLearning/Caffe/caffe/examples/forklift_classification/forklift_classification_solver.prototxt --weights=%caffe_root%/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel --log_dir=logs