# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

with open("./hightemp.txt",'r', encoding='utf-8') as f:
    data = f.readlines()
print(len(data))