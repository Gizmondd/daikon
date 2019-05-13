import codecs
import os

with codecs.open("test.bpe.de", mode="r", encoding="utf-8") as source:
    with codecs.open("test.bpe.reversed", mode="w", encoding="utf-8") as target:
        for line in source:
            reversed_list = line.split()[::-1]
            target.write(" ".join(reversed_list) + "\n")