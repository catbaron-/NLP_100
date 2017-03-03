# 07. テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

def gen_sentence(x, y, z):
    template = "x時のyはz"
    return template.replace("x",x).replace("y", y).replace("z", z)

def main():
    x, y, z = "12", "気温", "22.4"
    print(gen_sentence(x, y, z))

if __name__ == '__main__':
    main()