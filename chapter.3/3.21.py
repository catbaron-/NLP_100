import json,re

with open("English.json", "rt", encoding='utf-8') as f:
    data = json.load(f)
text = data["text"]

lines = re.findall(r'.*Category.*', text)
for line in lines:
    print(line)