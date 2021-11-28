import json


census = ["民籍", "軍籍", "官籍", "匠籍", "竈籍", "其他"]

def process_year_and_census(data_items):
    year_dict = {}
    processed_data_items = []
    
    for item in data_items:
        if item["年份"] == 1592:
            continue
        if not item["年份"] in year_dict:
            year_dict[item["年份"]] = {
                "年份": item["年份"],
                "其他": 0,
                "竈籍": 0,
                "匠籍": 0,
                "官籍": 0,
                "軍籍": 0,
                "民籍": 0,
            }
            year_dict[item["年份"]][item["戶籍"]] += 1
        else:
            year_dict[item["年份"]][item["戶籍"]] += 1
    
    for key in year_dict.keys():
        processed_data_items.append(year_dict[key])
    processed_data_items.sort(key=lambda x: x["年份"])
    return processed_data_items


if __name__ == '__main__':
    file_name = "./Data/processed_data.json"
    jsFile = open(file_name, "r", encoding='utf-8')
    data = json.load(jsFile)
    jsFile.close()
    data_items = data["数据项"]
    processed_data_items = process_year_and_census(data_items)
    data = {"dataset":"mingjinshi", "dataitem": processed_data_items}

    js = json.dumps(data,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
    jsFile = open("./Data/year_and_census_data.json", "w+", encoding='utf-8')
    jsFile.write(js)
    jsFile.close()
