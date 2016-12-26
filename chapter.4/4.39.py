# -*- coding: utf-8 -*-
# 39. Zipfの法則
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
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
    freqs = frequency()
    x, y = range(1, len(freqs)+1), map(lambda t:t[1], freqs)

    plt.plot(x, y, "ro")
    plt.xscale("log")
    plt.yscale("log")
    # plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
