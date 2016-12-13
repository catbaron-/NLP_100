# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
def rev_str(s):
    return s[::-1]

def main():
    print(rev_str("stressed"))

if __name__ == '__main__':
    main()