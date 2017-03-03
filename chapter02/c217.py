# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

import re

def uniq_in_column(filename, n):
    column_n = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        column_n.append(re.split(r'\s', line)[n])
    return column_n

def main():
    print(len(set(uniq_in_column("hightemp.txt", 0))))

if __name__ == '__main__':
    main()