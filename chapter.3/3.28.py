# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
import json,re
with open("English.json", "rt", encoding='utf-8') as f:
    data = json.load(f)
text = data["text"]

for info in re.findall(r'\{\{基礎情報\s国\n(?:.*\n)+\}\}', text):
    # find all text of basic info.

    items = info#.group(0)
    # remove emphasizement (added in 26)
    items = re.sub(r'(?P<emp>\'{2,3}|\'{5})(?P<ctnt>[^\']+)(?P=emp)',r'\g<ctnt>',items)
    # remove link (added in 27)
    items = re.sub(r'\[\[(?P<ctnt>[^\[^\]]+)\]\]', r'\g<ctnt>', items)
    #remove MediaWiki (added in 28)
    items = re.sub(r'\<.+\>|\{\{|\}\}',r'',items)
    print(items)
