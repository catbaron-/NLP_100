# -*- coding: utf-8 -*-
# 32. 動詞の原形
# サ変接続の名詞をすべて抽出せよ．


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

def sa_verb():
    filename = "neco.txt.mecab"
    mors = read_mecab(filename)
    for mor in mors:
        if mor["pos"] == "動詞":
            print mor["surface"],":",mor["base"]

def main():
    sa_verb()

if __name__ == '__main__':
    main()
