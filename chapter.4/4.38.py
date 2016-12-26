# -*- coding: utf-8 -*-
# 38. ヒストグラム
# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
from chapter4 import read_mecab
import numpy as np
import matplotlib.pyplot as plt
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
    freqs = frequency()[:1000]
    v = map(lambda t:t[1], freqs)
    num_bins = 500

    n, bins, patches = plt.hist(v, num_bins)
    plt.ylim(0, 100)
    # plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
