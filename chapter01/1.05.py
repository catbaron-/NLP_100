# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

import re

def n_gram(s_list, n):
    res = []
    if len(s_list) < n:
        return [s_list]
    gram = s_list[:n]
    for i in range(n, len(s_list)):
        res.append(tuple(gram))
        gram = gram[1:]
        gram.append(s_list[i])
    res.append(tuple(gram))
    return tuple(res)

def main():
    s = "I am an NLPer"
    print(n_gram(list(s), 2))

    words = re.split(r'[\s,\.]', s)
    print(n_gram(words, 2))

if __name__ == '__main__':
    main()