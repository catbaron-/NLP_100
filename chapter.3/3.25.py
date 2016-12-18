# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import json,re
with open("English.json", "rt", encoding='utf-8') as f:
    data = json.load(f)
text = data["text"]
# print(text)
for info in re.finditer(r'\{\{基礎情報\s国\n(.*\n)+\}\}', text):
    items = info.group(0)
    # print(items)
    for item in re.findall(r'\|(.+)\s=\s(.+)\n', items):
        print("%s:%s" % (item[0], item[1]))
    print()