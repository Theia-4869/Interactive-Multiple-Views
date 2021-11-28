import json


def process_item(data_items):
    jiaci_dict = {}
    mingci_dict = {}
    census_dict = {}
    subject_dict = {}
    
    for item in data_items:
        if item["甲次"] in ["", "第仕至二甲", "第乙未殿試二甲"]:
            item["甲次"] = "未知"
        
        if item["甲次"] not in jiaci_dict:
            jiaci_dict[item["甲次"]] = 1
        else:
            jiaci_dict[item["甲次"]] += 1

        if item["名次"] == "第一百十九名":
            item["名次"] = "第一百一十九名"
        elif item["名次"] == "第二百八名":
            item["名次"] = "第二百零八名"
        elif item["名次"] == "第一百八名":
            item["名次"] = "第一百零八名"
        elif item["名次"] == "第二百十八名":
            item["名次"] = "第二百一十八名"
        elif item["名次"] == "第一百十一名":
            item["名次"] = "第一百一十一名"
        elif item["名次"] == "第二百三名":
            item["名次"] = "第二百零三名"
        elif item["名次"] == "第二百十一名":
            item["名次"] = "第二百一十一名"
        elif item["名次"] == "第二百九名":
            item["名次"] = "第二百零九名"
        elif item["名次"] == "第一百五名":
            item["名次"] = "第一百零五名"
        elif item["名次"] == "第一百七名":
            item["名次"] = "第一百零七名"
        elif item["名次"] == "第二百十四名":
            item["名次"] = "第二百一十四名"
        elif item["名次"] == "第一百二名":
            item["名次"] = "第一百零二名"
        elif item["名次"] == "第二百四名":
            item["名次"] = "第二百零四名"
        elif item["名次"] == "第二百十名":
            item["名次"] = "第二百一十名"
        elif item["名次"] == "第二百十七名":
            item["名次"] = "第二百一十七名"
        elif item["名次"] == "第一百三名":
            item["名次"] = "第一百零三名"
        elif item["名次"] == "第一百九名":
            item["名次"] = "第一百零九名"
        elif item["名次"] == "第一百十六名":
            item["名次"] = "第一百一十六名"
        elif item["名次"] == "第一百十五名":
            item["名次"] = "第一百一十五名"
        elif item["名次"] == "第二百六名":
            item["名次"] = "第二百零六名"
        elif item["名次"] == "第二百十五名":
            item["名次"] = "第二百一十五名"
        elif item["名次"] == "第一百六名":
            item["名次"] = "第一百零六名"
        elif item["名次"] == "第二百一名":
            item["名次"] = "第二百零一名"
        elif item["名次"] == "第二百十三名":
            item["名次"] = "第二百一十三名"
        elif item["名次"] == "第一百十四名":
            item["名次"] = "第一百一十四名"
        elif item["名次"] == "第一百一名":
            item["名次"] = "第一百零一名"
        elif item["名次"] == "第二百十六名":
            item["名次"] = "第二百一十六名"
        elif item["名次"] == "第二百二名":
            item["名次"] = "第二百零二名"
        elif item["名次"] == "第二百十九名":
            item["名次"] = "第二百一十九名"
        elif item["名次"] == "第二百七名":
            item["名次"] = "第二百零七名"
        elif item["名次"] == "第二百十二名":
            item["名次"] = "第二百一十二名"
        elif item["名次"] == "第二百五名":
            item["名次"] = "第二百零五名"
        elif item["名次"] == "第一百十三名":
            item["名次"] = "第一百一十三名"
        elif item["名次"] == "第一百四名":
            item["名次"] = "第一百零四名"
        elif item["名次"] == "第一百十八名":
            item["名次"] = "第一百一十八名"
        elif item["名次"] == "第一百十名":
            item["名次"] = "第一百一十名"
        elif item["名次"] == "第一百十七名":
            item["名次"] = "第一百一十七名"
        elif item["名次"] == "第士一名":
            item["名次"] = "第十一名"
        elif item["名次"] == "第一百十二名":
            item["名次"] = "第一百一十二名"
        elif item["名次"] == "第第一名":
            item["名次"] = "第一名"
        elif item["名次"] == "第一十三名":
            item["名次"] = "第十三名"
        elif item["名次"] == "第二            名":
            item["名次"] = "第二名"
        elif item["名次"] in ["", "第□名", "第一百□名", "第二百二十□名", "第名"]:
            item["名次"] = "未知"

        if item["名次"] not in mingci_dict:
            mingci_dict[item["名次"]] = 1
        else:
            mingci_dict[item["名次"]] += 1

        if len(item["戶籍"]) > 1 and item["戶籍"][-1] == "藉":
            item["戶籍"] = item["戶籍"][:-1] + "籍"
        if len(item["戶籍"]) > 1 and item["戶籍"][-1] == "\u3000":
            item["戶籍"] = item["戶籍"][:-1]
        if len(item["戶籍"]) > 1 and item["戶籍"][-1] == "人":
            item["戶籍"] = "民籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "儒籍":
            item["戶籍"] = "儒籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "民籍":
            item["戶籍"] = "民籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "府籍":
            item["戶籍"] = "民籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "州籍":
            item["戶籍"] = "民籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "州府":
            item["戶籍"] = "民籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "縣籍":
            item["戶籍"] = "民籍"
        elif len(item["戶籍"]) > 1 and item["戶籍"][-1] == "縣":
            item["戶籍"] = "民籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "富戶":
            item["戶籍"] = "民籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "軍籍":
            item["戶籍"] = "軍籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "旗籍":
            item["戶籍"] = "軍籍"
        elif len(item["戶籍"]) > 1 and item["戶籍"][-1] == "旗":
            item["戶籍"] = "軍籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "衛籍":
            item["戶籍"] = "軍籍"
        elif len(item["戶籍"]) > 1 and item["戶籍"][-1] == "衛":
            item["戶籍"] = "軍籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "所籍":
            item["戶籍"] = "軍籍"
        elif len(item["戶籍"]) > 1 and item["戶籍"][-1] == "所":
            item["戶籍"] = "軍籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "軍餘":
            item["戶籍"] = "軍籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "站籍":
            item["戶籍"] = "站籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "官籍":
            item["戶籍"] = "官籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "校籍":
            item["戶籍"] = "官籍"
        elif len(item["戶籍"]) > 3 and item["戶籍"][-3:] == "校尉籍":
            item["戶籍"] = "官籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "匠籍":
            item["戶籍"] = "匠籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "醫籍":
            item["戶籍"] = "醫籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "竈籍":
            item["戶籍"] = "灶籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "廚籍":
            item["戶籍"] = "廚籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "戶籍":
            item["戶籍"] = "民籍"
        elif len(item["戶籍"]) > 2 and item["戶籍"][-2:] == "鹽籍":
            item["戶籍"] = "鹽籍"
        elif len(item["戶籍"]) > 3 and item["戶籍"][-3:] == "力士籍":
            item["戶籍"] = "力士籍"
        elif len(item["戶籍"]) > 3 and item["戶籍"][-3:] == "勇士籍":
            item["戶籍"] = "勇士籍"
        if item["戶籍"] in ["竈籍", "竃籍", "竈縣"]:
            item["戶籍"] = "灶籍"
        elif item["戶籍"] in ["軍餘", "旗籍", "衛籍", "衛舍籍"]:
            item["戶籍"] = "軍籍"
        elif item["戶籍"] in ["校籍", "校尉籍", "南京欽天監籍"]:
            item["戶籍"] = "官籍"
        elif item["戶籍"] in ["富戶", "直隸河間府任丘縣□籍", "浙江嘉興府秀水籍"]:
            item["戶籍"] = "民籍"
        elif item["戶籍"] in ["鹽縣", "塩籍"]:
            item["戶籍"] = "鹽籍"
        elif item["戶籍"] in ["太醫院籍"]:
            item["戶籍"] = "醫籍"
        elif item["戶籍"] in ["馬船夫籍"]:
            item["戶籍"] = "馬船籍"
        elif item["戶籍"] in ["", "□", "□籍", "□□", "站籍", "占籍", "□□□□□□□"]:
            item["戶籍"] = "其他"
        elif len(item["戶籍"]) > 3:
            item["戶籍"] = "軍籍"
        
        #清修《明史》：“曰民，曰军，曰匠。民有儒，有医，有阴阳。军有校尉，有力士，弓、铺兵。匠有厨役、裁缝、马船之类。濒海有盐灶。寺有僧，观有道士。毕以其业著籍。”
        #《后湖志》：“夫洪武旧本，由木之根、水之源也。木有千条万干，总出一根；水有千支万派，总出一源。人有千门万户，总出于军、民、匠、灶之一籍。”
        if item["戶籍"] in ["力士籍", "勇士籍", "弓兵籍"]:
            item["戶籍"] = "軍籍"
        elif item["戶籍"] in ["儒籍", "陰陽籍", "生員籍"]:
            item["戶籍"] = "民籍"
        elif item["戶籍"] in ["醫籍", "廚籍", "馬船籍"]:
            item["戶籍"] = "匠籍"
        elif item["戶籍"] in ["鹽籍", "灶籍"]:
            item["戶籍"] = "竈籍"

        if item["戶籍"] not in census_dict:
            census_dict[item["戶籍"]] = 1
        else:
            census_dict[item["戶籍"]] += 1

        #《扬子法言》：说天者莫辩乎《易》，说事者莫辩乎《书》，说体者莫辩乎《礼》，说志者莫辩乎《诗》，说理者莫辩乎《春秋》。
        if item["科目"] == "禮紀":
            item["科目"] = "禮記"
        elif len(item["科目"]) > 2:
            if item["科目"][0] == "詩":
                item["科目"] = "詩經"
            elif item["科目"][0] == "書":
                item["科目"] = "書經"
            elif item["科目"][0] == "禮":
                item["科目"] = "禮記"
            elif item["科目"][0] == "易":
                item["科目"] = "易經"
            elif item["科目"][:2] == "春秋":
                item["科目"] = "春秋"
        elif item["科目"] in ["", "□", "□經", "□□"]:
            item["科目"] = "其他"
        
        if item["科目"] not in subject_dict:
            subject_dict[item["科目"]] = 1
        else:
            subject_dict[item["科目"]] += 1

    # print(jiaci_dict)
    # print(mingci_dict)
    # print(census_dict)
    # print(subject_dict)
    
    census_dict = {
        "民籍": census_dict["民籍"],
        "軍籍": census_dict["軍籍"],
        "官籍": census_dict["官籍"],
        "匠籍": census_dict["匠籍"],
        "竈籍": census_dict["竈籍"],
        "其他": census_dict["其他"],
    }
    
    subject_dict = {
        "詩經": subject_dict["詩經"],
        "書經": subject_dict["書經"],
        "禮記": subject_dict["禮記"],
        "易經": subject_dict["易經"],
        "春秋": subject_dict["春秋"],
        "其他": subject_dict["其他"],
    }

    dicts = [
        {
            "name": "jiaci_dict",
            "children": [jiaci_dict],
        },
        {
            "name": "mingci_dict",
            "children": [mingci_dict],
        },
        {
            "name": "census_dict",
            "children": [census_dict],
        },
        {
            "name": "subject_dict",
            "children": [subject_dict],
        },
    ]

    return data_items, dicts


if __name__ == '__main__':
    file_name = "./Data/ming_jinshilu_52y_release.json"
    jsFile = open(file_name, "r", encoding='utf-8')
    data = json.load(jsFile)
    jsFile.close()
    data_items = data["children"]
    data_items_processed, dicts = process_item(data_items)
    data = {"name":"mingjinshi", "children": data_items_processed}
    dic = {"name":"mingjinshi_dict", "children": dicts}

    js = json.dumps(data,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
    jsFile = open("./Data/mingjinshi_processed.json", "w+", encoding='utf-8')
    jsFile.write(js)
    jsFile.close()

    js = json.dumps(dic,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
    jsFile = open("./Data/mingjinshi_dict.json", "w+", encoding='utf-8')
    jsFile.write(js)
    jsFile.close()
