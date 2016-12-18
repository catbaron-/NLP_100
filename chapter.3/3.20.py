# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
# -*- coding: utf-8 -*-

import json,gzip
with gzip.open('./jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    text = f.readlines()
for line in text:
    data = json.loads(line)
    if data['title'] == u'イギリス':
        print(data)
        with open('English.json',"wt",encoding='utf-8') as f: json.dump(data, f)
        break
