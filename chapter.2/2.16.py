# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys,math
def split_file(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    l = 0
    for i in range(len(lines))[::n]:
        with open(filename+"."+str(l), 'w', encoding='utf-8') as f:
            for line in lines[i:i+n]:
                f.write(line)
        l = l+1

def main():
    split_file("hightemp.txt",int(sys.argv[1]))

if __name__ == '__main__':
    main()