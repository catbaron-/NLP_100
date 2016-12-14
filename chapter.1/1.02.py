# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

def add_strs(s1, s2):
    return s1+s2

def main():
    s1 = u"パトカー"
    s2 = u"タクシー"
    print(add_strs(s1, s2))

if __name__ == '__main__':
    main()