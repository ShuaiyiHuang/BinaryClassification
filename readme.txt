
1.����genImage.py��������Ƶ����640*360��ͼ��ÿ6֡����һ��ͼ��
2.����genTxt.py������caffe����ѵ��������֤����txt�ĵ�������˳���Դ���

ע�⣺�����ļ��о���Ҫ������޸Ĳ�����
����Ĭ�Ͽճ�Ϊ���������л���Ϊ������

3.�����ɵõ���train.txt��validate.txt���Ƶ���Ŀ¼��
4.ѵ������
%caffe_root%/build/tools/Release/caffe.exe train --solver=F:/DeepLearning/Caffe/caffe/examples/forklift_classification/forklift_classification_solver.prototxt --weights=%caffe_root%/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel --log_dir=logs
5.forkNet_singletest.py ���Բ��Ե���ͼƬ�ķ�����