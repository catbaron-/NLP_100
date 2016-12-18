# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import json,re

with open("English.json", "rt", encoding='utf-8') as f:
    data = json.load(f)
text = data["text"]
patern = re.compile(r'.*Category:(.*)]].*')
lines = patern.findall(text)
for line in lines:
    print(line)