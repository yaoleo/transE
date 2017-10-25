# -*- coding:utf-8 -*-
import sys
from numpy import *
import numpy as np
from math import *
reload(sys)
sys.setdefaultencoding("utf-8")
EntityVectorName = "entityVector.txt"
EntityVectorDic  = {}
def scan2entity():
    entity1 = raw_input("Enter your entity1: ");

    entity2 = raw_input("Enter your entity1: ");

    return entity1, entity2

def readEntityVector(fname):
    fEntity = open(fname,"r")
    for line in fEntity:
        entity = line.split("\t")[0]
        vector = line.split("\t")[1]
        EntityVectorDic[entity] = vector
        print entity

def calRelation(e):
    e1 = e[0]
    e2 = e[1]
    if EntityVectorDic.get(e1) and EntityVectorDic.get(e2):
        print "e1",EntityVectorDic[e1],"e2",EntityVectorDic[e2]
        e1vec = [float(t) for t in EntityVectorDic[e1][1:-2].split(",")]
        e2vec = [float(t) for t in EntityVectorDic[e2][1:-2].split(",")]

        #print e1vec1

        print (cos(e1vec,e2vec)+1)/2.0
    else:
        print "不存在的实体 请重新输入"

def cos(vector1, vector2):
    vector1 = tuple(vector1)
    vector2 = tuple(vector2)
    dot_product = 0.0;
    normA = 0.0;
    normB = 0.0;
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return dot_product / ((normA * normB) ** 0.5)


readEntityVector(EntityVectorName)
while(True):
    calRelation(scan2entity())
