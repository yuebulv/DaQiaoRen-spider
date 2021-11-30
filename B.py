# -*- coding:utf-8 -*-
a = {'htmlAnalysis_question': [1, '（单选题）某高层建筑位于抗震设防烈度7度区，初勘覆盖层厚度为50.0m，据《岩土工程勘察规范》GB 50021-2001（2009年版）的规定，详勘时划分的场地类别布置钻孔深度合适的为下列哪个选项?\r\n'], 'htmlAnalysis_questionImg': '', 'htmlAnalysis_options': ['（A）20.0m\xa0', '（B）50.0m', '（C）55.0m\xa0', '（D）80.0m'], 'htmlAnalysis_answer': ['【答案】C', '\r\n【解析】根据《岩土工程勘察规范》GB 50021-2001（2009年版）页第5.7.2~5.7.4条文说明，勘察时应有一定的勘察孔满足计算土层等效剪切波速和覆盖层厚度，，并分层测定土的剪切波速，本题覆盖层在50m左右，且可能为中软土，故勘探孔不能只达到20m，应提供可靠的的剪切波速和覆盖层厚度值，故取55m最合适。\r\n']}
import re
import globalVar
from lxml import etree

# questionType = {'单选题': 0, '多选题': 1}
#
# question = '多选题'
# for type in questionType:
#     # print(type)
#     if question.find(type) >= 0:
#         name = type
#         temp = questionType[type]
#         print('name:', name)
#         print('temp:', temp)
#         break
# errorList = []
# res = {'questionDic': {}, 'error': errorList}
#
# for i in range(10):
#     errorList.append(i)
# print(res)
with open('test.html', 'r', encoding='utf-8') as fp:
    htmlText = fp.read()

tree = etree.HTML(htmlText)
htmlAnalysis_answerImg = tree.xpath("/html/body/div//div[@class='daanjiexi']/p/img/@src")
print(htmlAnalysis_answerImg)
try:
    htmlAnalysis_answerImg_new = htmlAnalysis_answerImg[0]
except IndexError:
    htmlAnalysis_answerImg_new = ''