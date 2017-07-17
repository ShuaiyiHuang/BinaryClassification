import cv2
import os
import os.path
import random

def generateData(videoName, saveRoot, filePrefix = '', sampleRate = 6):
    cap = cv2.VideoCapture(videoName)

    frameCount = 0
    lastFrameId = cap.get(7)-1  #frames count
    # sampleRate = 6 #every 6 frame one sample
    sampleWeight = 640
    sampleHeight = 360

    if not os.path.exists(saveRoot):
        os.makedirs(saveRoot)

    while cap.isOpened():
        ret,frame = cap.read()
        image = cv2.resize(frame,(sampleWeight,sampleHeight))

        frameCount += 1
        if frameCount <= lastFrameId:
            if frameCount % sampleRate == 0:
                temp = str(frameCount)
                print('save frame:' + temp)
                cv2.imwrite(saveRoot + '/' + filePrefix + '_' + temp + '.jpg',image)
        else:
            break

    # cv2.waitKey(0)
    cap.release()  
    cv2.destroyAllWindows()

def generateTxt(targetFileName, rootDir, label):
    #should check whether targetFile exists
    targetFile = open(targetFileName, 'a')

    for parent, dirNames, fileNames in os.walk(rootDir):  
        for fileName in fileNames:
            fullName = parent + '/' + fileName
            targetFile.write(fullName + ' ')
            targetFile.write(str(label) + '\n')

    targetFile.close()

def divideTxtContent(oriFileName, trainFileName='train.txt', valFileName='validate.txt'):
    oriFile = open(oriFileName, 'r')
    trainFile = open(trainFileName, 'w+')
    valFile = open(valFileName, 'w+')
    
    lines = oriFile.readlines()
    count = len(lines)
    random.shuffle(lines) #shuffle data
    for line in lines:
        randVal = random.randint(0,9)
        if randVal == 9:
            valFile.write(line)
        else:
            trainFile.write(line)

    oriFile.close()
    trainFile.close()
    valFile.close()