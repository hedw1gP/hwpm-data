import json

f = open("catalog_2.6.0.json", "r")
f2 = open("20220816.txt", "w")
fjson = json.load(f)
for line in fjson["m_InternalIds"]:
    if "cloudfront.net" in line:
        f2.writelines(line)
        f2.write("\n")