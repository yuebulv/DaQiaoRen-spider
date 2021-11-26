import requests
import json
import time
from lxml import etree


def getHtml_DaQiaoRen(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'Cookie': 'PHPSESSID=2v9vgarlcr4v548jutpm7hoo71; BdXlz_auth=72fcx39rm9PWLzHuPkmVGGXyyIFBIyPeFRNuC439s2vjPwYE8HQI2qtc-444iWXMCcv6KQhBNK2o57kR_I-0ESMIhJJ_c0u1dOHvdDBBEXgVdOXbb_aHX5CYrljFXMabClgulns1g1tFgL4D5wVRA6WgmHe-; BdXlz__userid=4120wofNOdiQra-Jsysz2lIo8NzxKQo2PqiMfkBf9tYU; BdXlz__username=3d778wTBLkaquEzT7ClQc1cxtyPdj3CF0rxz5b-Yw6SydA; BdXlz__groupid=73cbgKhSXlxR-NHYVIWzx3lI4KHNfw3CWP29B21K; BdXlz__nickname=74d6B6ViHuGpBIiAXHgiQ3VKowhgMZ-hWeni2lF3G10gTTDRKBMSfKpVgfvXXC4A',
        'Referer': 'http: // www.daqiaoren.com / index.php?m = content & c = index & a = lists & catid = 124'
    }

    # url = "http://www.daqiaoren.com/index.php?m=member&c=index&a=login"
    # url = "http://www.daqiaoren.com//index.php?m=content&c=index&a=lists&catid=15"
    # exam_url_1st = "http://www.daqiaoren.com//index.php?m=content&c=index&a=lists&catid=9"

    # exam_url_A = 'http://www.daqiaoren.com/index.php?m=content&c=index&a=show&catid=125&id=3409'
    exam_url_A = url
    html_exam_url_A = requests.get(exam_url_A, headers=headers)
    # print(html_exam_url_A.text)
    return html_exam_url_A.text


def htmlAnalysis_DaQiaoRenQusetionBank(htmlText):
    resDic = {}
    # parser = etree.HTMLParser(encoding='utf-8')
    # tree = etree.parse(htmlPath, parser=parser)

    tree = etree.HTML(htmlText)
    htmlAnalysis_question = tree.xpath("/html/body/div//h1/span/text()")

    print('htmlAnalysis_question:', htmlAnalysis_question)

    htmlAnalysis_questionImg = tree.xpath("/html/body/div//div[@class='tiimg']/img/@src")
    print('htmlAnalysis_questionImg:', htmlAnalysis_questionImg)

    htmlAnalysis_options = tree.xpath("/html/body/div//ul[@id='ul_answers']/label/text()")
    print('htmlAnalysis_options:', htmlAnalysis_options)
    htmlAnalysis_answer = tree.xpath("/html/body/div//div[@class='daanjiexi']/p/text()")
    print('htmlAnalysis_answer:', htmlAnalysis_answer)

    htmlAnalysis_questionUrl = tree.xpath("/html/body/header//div[@class='div3']//a/@href")
    print('htmlAnalysis_questionUrl:', htmlAnalysis_questionUrl)

    resDic['htmlAnalysis_question'] = htmlAnalysis_question
    resDic['htmlAnalysis_questionImg'] = htmlAnalysis_questionImg
    resDic['htmlAnalysis_options'] = htmlAnalysis_options
    resDic['htmlAnalysis_answer'] = htmlAnalysis_answer
    print(resDic)
    return resDic


def saveAsJson(name, question, answer: list, detail, index: int):
    # answer=['contentA', 'contentB', 'contentC']
    global dic
    dic = {
        "type": 0,
        "id": 0,
        "name": name,
        "content": question,
        "answer": [
            {
                "name": "A",
                "content": "二便失禁",
                "isanswer": False
            },
        ],
        'detail': '解析',
        'index': index
    }

    json.dump(dic, open('data/data.json', 'w'), indent=4)
if __name__=="__main__":
    # with open('test.html', 'r', encoding='utf-8') as htmlFile:
    #     htmlText = htmlFile.read()
    # htmlPath = 'test.html'
    # htmlAnalysis_DaQiaoRenQusetionBank(htmlPath)


    # exam_url_A = 'http://www.daqiaoren.com/index.php?m=content&c=index&a=show&catid=125&id=3409'
    # temp1 = getHtml_DaQiaoRen(exam_url_A)
    # temp2 = htmlAnalysis_DaQiaoRenQusetionBank(temp1)

    global dic
    saveAsJson()
    dic['content'] = 'temp'
    print(dic)
