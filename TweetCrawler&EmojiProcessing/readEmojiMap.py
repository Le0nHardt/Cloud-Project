#coding=utf-8
import  codecs
import json
from pprint import pprint
f = codecs.open('~/Desktop/emoji_set.txt', 'r')
for i in f:
    print i
f.close()
