#coding=utf-8

import requests
import json

app_version = "2.6.0"

link_base = "https://production.arisa-project.net/api/Master/"
data_alias = ["Version", "Music", "TitleAsset", "Criware", "Character", "Other", "OtherLowFrequency", "Event", "Scenario"]
client_headers = {
    "X-Chikuzen-Client-App-Platform": "Ios",
    "X-Chikuzen-Client-App-Version": "{}".format(app_version),
    "X-DeviceTime": "0"
}

for alias in data_alias:
    alias_web_data = requests.get(link_base+alias, headers=client_headers)
    alias_json_data = json.loads(alias_web_data.text)
    print(len(alias_json_data))
    with open(alias+".json", "w", encoding="utf-8") as json_file:
        json.dump(alias_json_data, json_file, indent=4, ensure_ascii=False)


# Below will cost 20-30 MB data
with open("catalog_"+app_version+".json", "w", encoding="utf-8") as json_file:
    catalog_web_data = requests.get("https://d1fsdx0i2ajtn2.cloudfront.net/hoh5eiWekohm9aik2EehaechaizaGaib/asset-bundle/"+app_version+"/iOS/catalog_"+app_version+".json", headers=client_headers)
    catalog_json_data = json.loads(catalog_web_data.text)
    print(len(alias_json_data))
    json.dump(catalog_json_data, json_file, indent=4, ensure_ascii=False)