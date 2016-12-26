# -*- coding: utf-8 -*-
# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．
from chapter4 import read_mecab

def sa_verb():
    filename = "neco.txt.mecab"
    mors = read_mecab(filename)
    for mor in mors:
        if mor["pos"] == "名詞" and mor["pos1"] == "サ変接続":
            print mor["surface"],":",mor["pos1"]

def main():
    sa_verb()

if __name__ == '__main__':
    main()
