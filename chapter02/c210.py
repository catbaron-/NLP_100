# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

def line_count():
    with open("./hightemp.txt",'r', encoding='utf-8') as f:
        data = f.readlines()
    return len(data)

if __name__=='__main__':
    print(line_count())