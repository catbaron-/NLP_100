# -*- coding: utf-8 -*-
# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
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
    res = sorted(map(lambda t:(t[0], t[1]/float(len(mors_dic))), mors_dic.items()), key=lambda i:i[1], reverse=True)
    print res
    return res

def main():
    freqs = frequency()[:10]
    n_groups = len(freqs)

    index = np.arange(n_groups)
    v_freqs = tuple(map(lambda i:i[1], freqs))
    bar_width = 0.5
    rects = plt.bar(index, v_freqs, bar_width)

    plt.xlabel(u"word")
    plt.ylabel("frequency")

    plt.xticks(index+bar_width/2.0, map(lambda t:t[0].decode("utf-8"),freqs))
    plt.legend()

    # plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
