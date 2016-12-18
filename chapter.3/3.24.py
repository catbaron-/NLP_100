# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

import json,re
with open("English.json", "rt", encoding='utf-8') as f:
    data = json.load(f)
text = data["text"]

for ref in re.findall(r'(ファイル|File|file):(.+\.\w+)\|', text):
    print(ref[1])
    print()