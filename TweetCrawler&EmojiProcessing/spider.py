import re
import codecs
from pyquery import PyQuery as pq
import json

jsonArray = []
jsonObject = {}
f = codecs.open('emoji.txt', 'r')
pattern = re.compile(r'<td class="code">(\\x.*?)</td>')
pattern_name = re.compile(r'<td class="name">(.*?)</td>')
f1 = codecs.open('emoji_set.txt', 'w')
# for line in f:
#     result = re.findall(pattern, line)
#     if len(result) > 0:
#         print str(result[0])
#         f1.writelines(result[0]+'\n')
#     result_name = re.findall(pattern_name,line)
#     if len(result_name)>0:
#         print str(result_name[0])
#         f1.writelines(result_name[0]+'\n')
pattern_url = re.compile(r'<a href="(/unicode.*?)">U')

for line in f:
    result = re.findall(pattern_url, line)
    # print result[0]
    if len(result) > 0:
        # print result[0]
        # print result[0]
        url = 'http://apps.timwhitlock.info' + result[0]
        source = pq(url=url)
        data = source('tbody').eq(0)
        str = data('tr').find('td').eq(2).find('code').eq(0).text()
        if len(str) == 5:
            uni = '\U'+'000'+str.lower()
            #uni = data('tr').find('td').eq(5).text()
            #array = uni.split(' ')
            #uni = '\u' + array[0].lower() + '\u' + array[1].lower()

            print uni
            jsonObject[uni] = data('tr').find('td').eq(6).text().lower()
        elif len(str) == 4:
            uni = '\u'+str.lower()
            print uni
            jsonObject[uni] = data('tr').find('td').eq(5).text().lower()

        # print len(str)
        # print '---'
        # for i in range(len(source(data).find('td'))):
        #     print source(data).find('td').eq(i).text()
json.dump(jsonObject,f1)
f1.close()
f.close()
