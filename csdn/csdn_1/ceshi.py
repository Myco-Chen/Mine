import requests
import pdfkit
import parsel
url = 'https://blog.csdn.net/A728848944/article/details/108029892'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
html = response.text
selector = parsel.Selector(html)
title = selector.css('.title-article::text').get()
article = selector.css('article').get()

src_html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>

</head>
<body>
    {content}
</body>
</html>
'''
with open(title+'.html',mode='w+',encoding='utf-8') as f:
    f.write(src_html.format(content=article))
    print(title+'保存成功')

config = pdfkit.configuration(wkhtmltopdf=r'F:\wkhtmltopdf\bin\wkhtmltopdf.exe')
pdfkit.from_file(title+'.html',title+'.pdf',configuration=config)

print(title+'.pdf','保存成功')