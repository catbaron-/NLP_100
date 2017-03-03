# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

def tail(f, n):
    return f.readlines()[-n:]

def show_tail_n(n):
    with open("hightemp.txt", "r", encoding="utf-8") as f:
        lines = tail(f, n)
        for line in lines:
            print(line.strip())

if __name__ == '__main__':
    show_tail_n(10)
