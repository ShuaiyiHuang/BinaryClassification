from generator import *

import os
import os.path

targetFileName = 'collection-14.txt'
#delete targetFileName file first
if os.path.exists(targetFileName):
    os.remove(targetFileName)

rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/negtive'
label = 0
generateTxt(targetFileName, rootDir, label)

rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/positive'
label = 1
generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-12-103818'
# label = 0
# generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-12-105036'
# label = 1
# generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-13-153954'
# label = 1
# generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-13-153610'
# label = 1
# generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-13-153241'
# label = 1
# generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-13-152931'
# label = 1
# generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-13-152538'
# label = 1
# generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-13-151959'
# label = 1
# generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-13-151607'
# label = 1
# generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-13-151123'
# label = 1
# generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-13-150728'
# label = 1
# generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-13-150301'
# label = 1
# generateTxt(targetFileName, rootDir, label)

# rootDir = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-13-145738'
# label = 1
# generateTxt(targetFileName, rootDir, label)


divideTxtContent(targetFileName,'train.txt','validate.txt')