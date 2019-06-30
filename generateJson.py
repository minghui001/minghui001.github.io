import os
import json

# 单个产品的信息


class testProduct:
    types = ''
    fileName = ''
    title = ''
    keyWords = ''
    description = ''
    specifications = ''
    options = ''
    questionAndAnswer = ''
    dataDownload = ''

    def __init__(self, t, f):
        self.types = 'type'+t
        self.fileName = 'product'+f
        self.title = '产品'+f+'标题'
        self.keyWords = '产品'+f + 'keyword'
        self.description = '产品'+f+'description'
        temp = '这是一段关于产品的简介，主要是为了演示使用，内容为'
        self.specifications = temp+"叙述"
        self.options = temp+"选项"
        self.questionAndAnswer = temp+"问答"
        self.dataDownload = temp+"文件下载"

    def show(self):
        print(self.types)
        print(self.fileName)
        print(self.title)
        print(self.keyWords)
        print(self.description)
        print(self.specifications)
        print(self.options)
        print(self.questionAndAnswer)
        print(self.dataDownload)

    def obj_2_json(self):
        return {
            "types": self.types,
            "fileName": self.fileName,
            "title": self.title,
            "keyWords": self.keyWords,
            "description": self.description,
            "specifications": self.specifications,
            "options": self.options,
            "questionAndAnswer": self.questionAndAnswer,
            "dataDownload": self.dataDownload
        }



file=open("test.json",'w',encoding='utf-8')
file.write('{\n')

types=0
prod=0

while types<6:
    file.write('"types'+str(types)+'":[\n')
    while prod<5:
        tp=testProduct(str(types),str(prod))
        tpj=tp.obj_2_json()
        json_str=json.dumps(tpj,ensure_ascii=False,indent=4)
        file.write(json_str)
        prod=prod+1
        if prod<5:
            file.write(',\n')
    file.write('\n]')
    types=types+1
    if types<6:
        file.write(',\n')
    prod=0

file.write('}')
file.close()