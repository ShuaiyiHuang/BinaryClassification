
1.运行genImage.py，解码视频生成640*360的图像，每6帧采样一张图像
2.运行genTxt.py，生成caffe定义训练集和验证机的txt文档。数据顺序以打乱

注意：两个文件中均需要按情况修改参数。
网络默认空车为负样本，有货物为正样本

3.把生成得到的train.txt，validate.txt复制到该目录下
4.训练命令
%caffe_root%/build/tools/Release/caffe.exe train --solver=F:/DeepLearning/Caffe/caffe/examples/forklift_classification/forklift_classification_solver.prototxt --weights=%caffe_root%/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel --log_dir=logs
5.forkNet_singletest.py 可以测试单张图片的分类结果