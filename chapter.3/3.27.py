# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
import json,re
with open("English.json", "rt", encoding='utf-8') as f:
    data = json.load(f)
text = data["text"]

for info in re.findall(r'\{\{基礎情報\s国\n(?:.*\n)+\}\}', text):
    # find all text of basic info.
    items = info

    # remove emphasizement
    items = re.sub(r'(?P<emp>\'{2,3}|\'{5})(?P<ctnt>[^\']+)(?P=emp)',r'\g<ctnt>',items)
    # remove link (added in 27)
    items = re.sub(r'\[\[(?P<ctnt>[^\[^\]]+)\]\]', r'\g<ctnt>', items)

    print(items)
