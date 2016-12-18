# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
import re

with open("hightemp.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()

freq = {}
for line in lines:
    column = re.split(r'\s', line)[0]
    freq[column] = freq.get(column, 0) + 1

for c in sorted(freq.items(), key = lambda i:i[1], reverse=True):
    print("%s %.4f" % (c[0], c[1]/len(lines)))