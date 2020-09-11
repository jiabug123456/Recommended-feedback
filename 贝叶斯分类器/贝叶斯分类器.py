from numpy import * 
import os
#第一步、建立一个实验数据集
def loadDataSet():
    postingList=[['农林牧渔','土壤','畜牧业'],
                 ['医疗卫生','保健品','医疗机械',],
                 ['建筑建材','石油化工','新能源','小微企业'],
                 ['生物技术','食品','食品经营'],
                 ['信息产业','电子产品','计算机系统',],
                 ['交通运输','公路养护','信息咨询']]
    classVec=[0,1,2,3,4,5]
    return postingList,classVec
    
def createVocabList(dataSet):#创建一个包含所有文档中不重复出现的词列表
    vocabSet=set([])
    for docoment in dataSet:
        vocabSet=vocabSet|set(docoment)#添加新词到对象文档集中，|为求两个集合的并集
    return list(vocabSet)
#接下来我们需要用实际文档和标签集进行比较，并统计它的实际效果
def setOfwords2Vec(vocablist,inputSet):#一家公司的数据进来，对所属的词条在文档库中进行分类
    returnVec=[0]*len(vocablist)
    for word in inputSet:
        if word in vocablist:
            returnVec[vocablist.index(word)]=1
        else:
            print ("the world: %s is not in my Vocabulary!" % word )
    return returnVec
def classifyNB(vec2classify,p0Vec,p1Vec,p2Vec,p3Vec,p4Vec,p5Vec,pClass1):#朴素贝叶斯分类器
    p0=sum(vec2classify*p0Vec)+log(pClass1)
    p1=sum(vec2classify*p1Vec)+log(pClass1)
    p2=sum(vec2classify*p2Vec)+log(pClass1)
    p3=sum(vec2classify*p3Vec)+log(pClass1)
    p4=sum(vec2classify*p4Vec)+log(pClass1)
    p5=sum(vec2classify*p5Vec)+log(pClass1)
    fList=[p0,p1,p2,p3,p4,p5]
    fp=max(fList)
    return fList.index(fp)

def trainNB0(trainMatrix,trainCategory):#文档矩阵及类别标签向量
    numTrainDocs=len(trainMatrix)#文档矩阵的长度
    numWords=len(trainMatrix[0])#输入统计词条出现情况的列表，其实是不重复词的列表的长度
    pAbusive=float(1/6)#先验概率：即文档所属类别的概率
    p0Num=ones(numWords)
    p1Num=ones(numWords)
    p2Num=ones(numWords)
    p3Num=ones(numWords)
    p4Num=ones(numWords)
    p5Num=ones(numWords)
    p0Denom=2.0
    p1Denom=2.0
    p2Denom=2.0
    p3Denom=2.0
    p4Denom=2.0
    p5Denom=2.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            p1Num += trainMatrix[i]#将每一篇文档的单词出现列表相加
            p1Denom += sum(trainMatrix[i])#单词的总词数求和
        if trainCategory[i]==0:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
        if trainCategory[i]==2:
            p2Num += trainMatrix[i]
            p2Denom += sum(trainMatrix[i])
        if trainCategory[i]==3:
            p3Num += trainMatrix[i]
            p3Denom += sum(trainMatrix[i])
        if trainCategory[i]==4:
            p4Num += trainMatrix[i]
            p4Denom += sum(trainMatrix[i])
        if trainCategory[i]==5:
            p5Num += trainMatrix[i]
            p5Denom += sum(trainMatrix[i])
    p1Vect=log(p1Num/p1Denom)#求得每个单词在确定分类下，出现的概率
    p0Vect=log(p0Num/p0Denom)
    p2Vect=log(p2Num/p2Denom)
    p3Vect=log(p3Num/p3Denom)
    p4Vect=log(p4Num/p4Denom)
    p5Vect=log(p5Num/p5Denom)
    return p0Vect,p1Vect,p2Vect,p3Vect,p4Vect,p5Vect,pAbusive
def testingNB():
    listOPosts,listClasses=loadDataSet()#拿到实验训练集
    myVolcabList=createVocabList(listOPosts)#创建所有分词库
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfwords2Vec(myVolcabList,postinDoc))#生成训练集矩阵一个矩阵
    p0v,p1v,p2v,p3v,p4v,p5v,pAb=trainNB0(array(trainMat),array(listClasses))#导入训练集的概率
    testEntry=['建筑建材','石油化工','dalmation']
    thisDoc=array(setOfwords2Vec(myVolcabList,testEntry))#实际文档的在文本集中的标记
    print(testEntry ,'classified as: ',classifyNB(thisDoc,p0v,p1v,p2v,p3v,p4v,p5v,pAb))#做测试
    testEntry=['交通运输','土壤','建筑建材','食品']
    thisDoc=array(setOfwords2Vec(myVolcabList,testEntry))
    print(testEntry,' classified as: ',classifyNB(thisDoc,p0v,p1v,p2v,p3v,p4v,p5v,pAb))

    
testingNB()


