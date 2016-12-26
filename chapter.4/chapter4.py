def read_mecab(file_name):
    res = []
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line == "EOS\n":
                continue
            line = line.split("\t")
            surface = line[0]
            mors = line[1].split(",")
            pos = mors[0]
            pos1 = mors[1]
            base = mors[6]
            res.append({
                "base":base,
                "surface":surface,
                "pos":pos,
                "pos1":pos1
            })
    return res

def main():
    filename = "neco.txt.mecab"
    mecab = read_mecab(filename)
    for item in mecab:
        for k in item:
            print k+":"+item[k],
        print

if __name__ == '__main__':
    main()
