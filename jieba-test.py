# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 20:01:23 2017

@author: Administrator

jieba分词测试
"""

import jieba


#全模式
test1 = jieba.cut("杭州西湖风景很好，是旅游胜地！", cut_all=True)
print("全模式: " + "| ".join(test1))

#精确模式
test2 = jieba.cut("杭州西湖风景很好，是旅游胜地！", cut_all=False)
print("精确模式: " + "| ".join(test2))

#搜索引擎模式
test3= jieba.cut_for_search("杭州西湖风景很好，是旅游胜地,每年吸引大量前来游玩的游客！")  
print("搜索引擎模式:" + "| ".join(test3))