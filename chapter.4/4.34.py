# -*- coding: utf-8 -*-
# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

from chapter4 import read_mecab
filename = "neco.txt.mecab"

def aandb():
    mors = read_mecab(filename)
    res = []
    for i in range(len(mors)-2):
        if mors[i]["pos"] != "名詞" or mors[i+1]["surface"] != "の" or mors[i+2]["pos"] != "名詞":
            continue
        res.append((mors[i]["surface"], mors[i+1]["surface"], mors[i+2]["surface"], ))
    return res

def main():
    aandbs = aandb()
    for item in aandbs:
        print item[0], item[1], item[2]

if __name__ == '__main__':
    main()
