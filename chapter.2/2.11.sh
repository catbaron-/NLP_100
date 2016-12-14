# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

sed 's/\t/ /' hightemp.txt
tr '\t' ' ' < hightemp.txt
expand hightemp.txt