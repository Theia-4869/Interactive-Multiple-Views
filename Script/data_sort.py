import json

def sort_json(data):
    if "children" in data:
        v = 0
        for item in data["children"]:
            sort_json(item)
            v += item["value"]
        data["value"] = v
        data["children"].sort(key=lambda x:x["value"], reverse=True)

    return data

if __name__ == '__main__':
    file_name = "Data/xian_data.json"
    jsFile = open(file_name, "r", encoding='utf-8')
    data = json.load(jsFile)
    jsFile.close()

    data = sort_json(data)

    js = json.dumps(data,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
    jsFile = open("Data/xian_data.json", "w+", encoding='utf-8')
    jsFile.write(js)
    jsFile.close()