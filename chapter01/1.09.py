# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually 
# understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

from random import random

def typoglycemia(s):
    words = s.split()
    
    word = words[2]
    return " ".join([word if len(word)<4 else word[0:1]+"".join(sorted(word[1:-1], key=lambda x: random()))+word[-1:] for word in words])

def main():
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(typoglycemia(s))

if __name__ == '__main__':
    main()