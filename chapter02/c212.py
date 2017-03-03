# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ

import re

def cut_columns():
    col1, col2 = [], []
    with open("hightemp.txt", "r", encoding="utf-8") as f:
        for line in f:
            cols = line.split("\t")
            col1.append(cols[0])
            col2.append(cols[1])

    with open("col1.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(col1))

    with open("col2.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(col2))

if __name__ == '__main__':
    cut_columns()
