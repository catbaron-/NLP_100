# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

def replace_tab(f):
    res = []
    for line in f:
        res.append(line.replace("\t", " "))
    return ''.join(res)

def main():
    with open("hightemp.txt", "r", encoding="utf-8") as f:
        new_ctnt = replace_tab(f)
    with open("hightemp_space.txt", "w", encoding="utf-8") as f:
        f.write(new_ctnt)

if __name__ == '__main__':
    main()