# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, 
# XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def n_gram(s_list, n):
    res = []
    if len(s_list) < n:
        return [s_list]
    gram = s_list[:n]
    for i in range(n, len(s_list)):
        res.append(tuple(gram))
        gram = gram[1:]
        gram.append(s_list[i])
    res.append(tuple(gram))
    return tuple(res)
def main():
    sx = "paraparaparadise"
    sy = "paragraph"
    X = set(n_gram(list(sx), 2))
    Y = set(n_gram(list(sy), 2))

    print("X:", X)
    print("Y:", Y)

    print("X and Y:",X&Y)
    print("X or Y:", X|Y)
    print("X complement Y:", X-Y)

if __name__ == '__main__':
    main()