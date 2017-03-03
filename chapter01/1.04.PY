# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New 
# Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目
# の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

import re

def main():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations \
        Might Also Sign Peace Security Clause. Arthur King Can."
    targets = {1:"1", 5:"1", 6:"1", 7:"1", 8:"1", 9:"1", 15:"1", 16:"1", 19:"1"}
    words = re.split(r'[\s\.]\s*', s)[:-1]
    res = {}
    for i in range(len(words)):
        rng = 1 if i in targets else 2
        letter = words[i][:rng]
        res[letter] = res.get(letter, []) + [i]
    print(res)

if __name__ == '__main__':
    main()