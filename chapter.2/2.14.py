# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

def head(f, n):
    for i in range(n):
        line = f.readline().strip()
        if not line:
            break
        print(line)

def main():
    with open("hightemp.txt", "r", encoding="utf-8") as f:
        head(f, 24)

if __name__ == '__main__':
    main()