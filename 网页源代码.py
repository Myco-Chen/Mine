import urllib.request
def read_pageHtml(url):
    file = urllib.request.urlopen(url)
    data = file.read()
    return data

url = input('请输入一个网址:')
data = read_pageHtml(url)
print(data)