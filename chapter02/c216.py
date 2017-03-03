# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys,math
def split_file(filename, n=10):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    l = math.ceil(len(lines)/2) # ファイルの長さ
    file_number = 0 # 第　l　番目のファイルを作る
    for i in range(len(lines))[::l]:
        with open(filename+"."+str(file_number), 'w', encoding='utf-8') as f:
            for line in lines[i:i+l]:
                f.write(line)
        file_number = file_number+1

def main():
    split_file("hightemp.txt",int(sys.argv[1]))

if __name__ == '__main__':
    main()
