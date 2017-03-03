# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving 
# quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

import re

def split_string(s):
    return re.split(r'[\s\.,]\s*', s)

def count_sort(s):
    words = set(split_string(s))
    words_with_length = [(len(w),w) for w in words if len(w) > 0]
    words_sorted = sorted(words_with_length, key=lambda i:i[0], reverse=True)
    for word in words_sorted:
        print(word[0]," ",word[1])

def main():
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    count_sort(s)

if __name__ == '__main__':
    main()