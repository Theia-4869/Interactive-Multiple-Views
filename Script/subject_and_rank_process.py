import json


subject = ["詩經", "書經", "禮記", "易經", "春秋"]

def process_subject_and_rank(data_items):
    subject_dict = {
        "詩經": {
            "科目": "詩經",
            "未知": 0,
            "第三甲": 0,
            "第二甲": 0,
            "第一甲": 0,
        },
        "書經": {
            "科目": "書經",
            "未知": 0,
            "第三甲": 0,
            "第二甲": 0,
            "第一甲": 0,
        },
        "禮記": {
            "科目": "禮記",
            "未知": 0,
            "第三甲": 0,
            "第二甲": 0,
            "第一甲": 0,
        },
        "易經": {
            "科目": "易經",
            "未知": 0,
            "第三甲": 0,
            "第二甲": 0,
            "第一甲": 0,
        },
        "春秋": {
            "科目": "春秋",
            "未知": 0,
            "第三甲": 0,
            "第二甲": 0,
            "第一甲": 0,
        },
        "其他": {
            "科目": "其他",
            "未知": 0,
            "第三甲": 0,
            "第二甲": 0,
            "第一甲": 0,
        }
    }
    processed_data_items = []
    
    for item in data_items:
        subject_dict[item["科目"]][item["甲次"]] += 1
    
    for key in subject_dict.keys():
        processed_data_items.append(subject_dict[key])
    return processed_data_items


if __name__ == '__main__':
    file_name = "./Data/processed_data.json"
    jsFile = open(file_name, "r", encoding='utf-8')
    data = json.load(jsFile)
    jsFile.close()
    data_items = data["数据项"]
    processed_data_items = process_subject_and_rank(data_items)
    data = {"dataset":"mingjinshi", "dataitem": processed_data_items}

    js = json.dumps(data,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
    jsFile = open("./Data/subject_and_rank_data.json", "w+", encoding='utf-8')
    jsFile.write(js)
    jsFile.close()
