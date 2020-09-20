from googletrans import Translator
import json
from time import sleep
translator = Translator(service_urls=[
    'translate.google.cn',
])
a= input('Type the original text here...')
count = 0
num = 1
dict = {'ja', 'ko', 'ms','es','th','uk','vi','zh-CN','zh-TW','en','hi','id','ms','mn','my','ne','bg','ar','hy'}
stop = int(input('你想啥时候结束哦：'))
for key in dict:
    b = translator.translate(a,dest=key)
    count = 1
   
    if count == 1:
        if num == stop:
            break
        else:
            for i in range(1, stop):
                sleep(1)
                b = translator.translate(b.text,dest=key)
                num = num + 1

final = translator.translate(b.text,dest='zh-CN')
print(final.text)
