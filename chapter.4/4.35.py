# -*- coding: utf-8 -*-
# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

from chapter4 import read_mecab
filename = "neco.txt.mecab"

def nouns():
    mors = read_mecab(filename)
    res = []
    i = 0
    sentence = ""
    for mor in mors:
        if not mor["pos"] == "名詞":
            if sentence:
                res.append(sentence)
                sentence = ""
        else:
            sentence =sentence + " " + mor["surface"]
    return res

def main():
    ns = nouns()
    for n in ns:
        print n

if __name__ == '__main__':
    main()
