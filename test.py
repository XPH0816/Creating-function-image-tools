import json

with open("./data.json") as f:
    data = json.load(f)

print(json.dumps(data["%s" % 1]["%s" % 1], indent=4, sort_keys=True))
print(data["image-size"])