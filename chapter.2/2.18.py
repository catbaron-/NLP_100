# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

import re

def sort_by_column(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return sorted(lines, key=lambda r:re.split(r'\s', r)[n], reverse=True)

def main():
    for line in sort_by_column("hightemp.txt", 2):
        print(line.strip())

if __name__ == '__main__':
    main()