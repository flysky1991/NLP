# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 20:13:52 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
PYNLPIR 分词测试
"""

import pynlpir


#打开分词器
pynlpir.open()

text1 = "杭州西湖风景很好，是旅游胜地,每年吸引大量前来游玩的游客！" 

#分词，默认打开分词和词性标注功能
test1 = pynlpir.segment(text1)
#print(test1)
print('1.默认分词模式:\n' + str(test1))

#将词性标注语言变更为汉语
test2 = pynlpir.segment(text1,pos_english=False)
print('2.汉语标注模式:\n' + str(test2))


#关闭词性标注
test3 = pynlpir.segment(text1,pos_tagging=False)
print('3.无词性标注模式:\n' + str(test3))

