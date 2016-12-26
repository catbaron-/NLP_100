# -*- coding: utf-8 -*-
# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ
from chapter4 import read_mecab
filename = "neco.txt.mecab"

def frequency():
    mors = read_mecab(filename)
    mors_dic = {}
    for mor in mors:
        if mor["pos"] == "記号":
            continue
        mors_dic[mor["surface"]] = mors_dic.get(mor["surface"], 0) + 1

    #sort
    return sorted(map(lambda t:(t[0], t[1]/float(len(mors_dic))), mors_dic.items()), key=lambda i:i[1], reverse=True)

def main():
    for item in frequency():
        print item[0],":", item[1]

if __name__ == '__main__':
    main()
