# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 20:07:34 2017

@author: Administrator

THULAC 分词测试
"""

import thulac   

#默认模式，分词的同时进行词性标注
test1 = thulac.thulac()
text1 = test1.cut("杭州西湖风景很好，是旅游胜地！")
print(text1)


#只进行分词
test2 = thulac.thulac(seg_only=True)
text2 = test2.cut("杭州西湖风景很好，是旅游胜地！")
print(text2)

