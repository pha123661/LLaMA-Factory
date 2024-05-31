import json

import opencc

converter = opencc.OpenCC('s2tw.json')

NAME = "OpenELM-zhtw"
AUTHOR = "Oscar Li"

with open("data/identity.json", "r", encoding="utf-8") as f:
  dataset = json.load(f)

for sample in dataset:
    sample["output"] = sample["output"].replace("{{"+ "name" + "}}", NAME).replace("{{"+ "author" + "}}", AUTHOR)
    for k, v in sample.items():
       # zhcn 2 zhtw
        sample[k] = converter.convert(v)

with open("data/identity.json", "w", encoding="utf-8") as f:
  json.dump(dataset, f, indent=2, ensure_ascii=False)