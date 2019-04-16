#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/16 9:40
import re
text = b'GET /index.html HTTP/1.1\r\nHost:'

result = re.findall('GET (.*?) HTTP',text.decode('utf-8'))
print(result)