# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
import json,re
with open("English.json", "rt", encoding='utf-8') as f:
    data = json.load(f)
text = data["text"]
for section in re.findall(r'=(=+)([^=]+)=+', text):
    print("%d:%s" % (len(section[0]),section[1]))