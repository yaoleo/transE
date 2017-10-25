# 作业一：计算实体距离

---

## 资料

算法原文：https://www.utc.fr/~bordesan/dokuwiki/_media/en/transe_nips13.pdf

算法翻译：http://blog.csdn.net/FFFNULL/article/list/2

算法理解：

+ https://xiangrongzeng.github.io/knowledge%20graph/transE.html
+ http://blog.csdn.net/fffnull/article/details/51130028

评估方法：https://xiangrongzeng.github.io/knowledge%20graph/transE-evaluation.html

算法开源：

+ https://github.com/thunlp/KB2E
+ https://github.com/wuxiyu/transE
        
---

## 项目

### 已有资源：

+ 基于开源的transE算法 https://github.com/wuxiyu/transE
+ 使用开源的数据集 http://openkg.cn/dataset/

### 工作流程：
1.1 算法读取train文件：

![算法读取文件样式][1]

1.2 算法读取实体-id对应文件（压缩计算量）
![此处输入图片的描述][2]

1.3 算法读取关系-id对应文件（压缩计算量）
![此处输入图片的描述][3]

2  算法执行计算输出结果文件
实体：[向量]

3  输入两个实体 返回结果
读取实体向量结果文件
计算余弦距离或者欧氏距离

### 任务执行

+ 执行fixFileForm.py预处理数据 核心参数

    源文件地址
    fname = "baike_triples.txt"
    文件读取的行数
    fnum = 10000
    测试时用的10000 太小 需要用大量数据进行计算

+ 执行transE.py 算法执行 得到实体向量
+ 执行calRelation 输入任意两个 输出实体的余弦相似度
