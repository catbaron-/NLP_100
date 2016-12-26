# -*- coding: utf-8 -*-
# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，
# 各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
# をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
# 第4章の残りの問題では，ここで作ったプログラムを活用せよ．

import re

def read_mecab(file_name):
    res = []
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line == "EOS\n":
                continue
            line = line.split("\t")
            surface = line[0]
            mors = line[1].split(",")
            pos = mors[0]
            pos1 = mors[1]
            base = mors[6]
            res.append({
                "base":base,
                "surface":surface,
                "pos":pos,
                "pos1":pos1
            })
    return res

def main():
    filename = "neco.txt.mecab"
    mecab = read_mecab(filename)
    for item in mecab:
        for k in item:
            print k+":"+item[k],
        print

if __name__ == '__main__':
    main()
