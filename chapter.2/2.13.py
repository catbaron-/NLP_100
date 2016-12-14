# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

f1 = open("col1.txt", "r", encoding="utf-8")
f2 = open("col2.txt", "r", encoding="utf-8")
f = open("merge.txt", "w", encoding="utf-8")

col1 = f1.readline()
col2 = f2.readline()
while col1 and col2:
    f.write(col1.strip()+"\t"+col2)
    col1 = f1.readline()
    col2 = f2.readline()

f1.close()
f2.close()
f.close()