# -*- coding:utf-8 -*-
import re
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()
# 源文件地址
fname = "baike_triples.txt"
# 文件读取的行数
fnum = 10000
# 实体字典
Enty = {}
# 关系字典
Relation = {}

# 读取文件 fname: 文件地址
def fixFileForm(fname, fnum):

    file = open(fname)
    # entyId
    EntyId = 0
    # relationId
    RelationId = 0
    # 读取文件行数count
    count = 0
    # 写入文件
    trainOut = open("data/train.txt", "a")
    entyIdOut = open("data/enty2Id.txt", "a")
    relationIdOut = open("data/relation2Id.txt", "a")
    # 第一次要清空文件之前的内容
    trainOut.truncate()
    entyIdOut.truncate()
    relationIdOut.truncate()
    # 按行读取 同时 按行写入
    for line in file:
        #print line.split("\t")[0],line.split("\t")[1],line.split("\t")[2]
        split_line = line.split("\t")
        # 去除非中文 构造实体
        enty0 = "".join(re.findall(ur"[\u4e00-\u9fa5]+", split_line[0].decode("utf-8")))
        enty1 = "".join(re.findall(ur"[\u4e00-\u9fa5]+", split_line[2].decode("utf-8")))
        relation = "".join(re.findall(ur"[\u4e00-\u9fa5]+", split_line[1].decode("utf-8")))
        #print "0:",enty0,"1:",enty1,"re:",relation

        if len(enty0) <= 4 and len(enty0) > 0 and len(enty1) <= 2 and len(enty1) > 0 and len(relation) > 0:

            if enty0 not in Enty and len(enty0) <= 4 and len(enty0) > 0:
                Enty[enty0] = EntyId
                entyIdOut.write(str(enty0) + "\t" + str(EntyId) + "\n")
                print str(enty0) + "\t" + str(EntyId) + "\n"
                EntyId = EntyId+1


            if enty1 not in Enty and len(enty1) <= 2 and len(enty1) > 0:
                Enty[enty1] = EntyId
                print str(enty1) + "\t" + str(EntyId) + "\n"
                entyIdOut.write(str(enty1) + "\t" + str(EntyId) + "\n")
                EntyId = EntyId + 1

            if relation not in Relation and len(relation) > 0:
                Relation[relation] = RelationId
                relationIdOut.write(str(relation) + "\t" + str(RelationId) + "\n")
                RelationId = RelationId + 1
        else:
            continue


        if Enty[enty0] and Enty[enty1] and Relation[relation]:
            #print "0:", enty0, "1:", enty1, "re:", relation
            #print Enty[enty0], Enty[enty1], Relation[relation]
            trainOut.write(enty0 + "\t" + enty1 + "\t" + relation + "\n")
            #trainOut.write(str(Enty[enty1]) + "\t" + str(Enty[enty0]) + "\t" + relation + "\n")
        # 读取足够行数跳出循环停止读取文件
        if count == fnum:
            break
        count += 1

    print "RelationId:", RelationId, "EntyId", EntyId

# 调用
fixFileForm(fname, fnum)