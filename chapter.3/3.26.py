# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
import json,re
with open("English.json", "rt", encoding='utf-8') as f:
    data = json.load(f)
text = data["text"]
for info in re.finditer(r'\{\{基礎情報\s国\n(.*\n)+\}\}', text):
    items = info.group(0)
    #remove emphasizement
    items = re.sub(r'(?P<emp>\'{2,3}|\'{5})(?P<ctnt>[^\']+)(?P=emp)',r'\g<ctnt>',items)

    for item in re.findall(r'\|(.+)\s=\s(.+)\n', items):
        print(item)
    print()