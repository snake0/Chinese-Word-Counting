#coding=utf-8
import jieba
import re
from collections import Counter
import sys

txt = open(sys.argv[1], "r", encoding="utf-8").read()

excludes = {"，", "。", "\n", "-", "“", "”", "：", "；", "？", "（", "）", "！", "…", "!", "?", ".",
            "\"", "/", "\\", "{", "}", "(", ")"}

words = jieba.lcut(txt)

counts = {}

for word in words:
    counts[word] = counts.get(word,0)+1

for word in excludes:
    if counts.__contains__(word):
        del counts[word]

items = list(counts.items())

items.sort(key=lambda x: x[1], reverse=True)

file = open(sys.argv[1] + "_词频", mode='w', encoding='utf-8')

for i in range(len(items)):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

    new_context = word + "\t" + str(count) + '\n'
    file.write(new_context)

file.close()


