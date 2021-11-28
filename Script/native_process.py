import json



def process_xian_data(fu_data):
    xian_data = []
    num_xian = {}

    zhou_xian_dict = {}
    for data_item in fu_data["children"]:
        if len(data_item) >= 4 and data_item[1] == "州" and data_item[-1] == "縣":
            zhou = data_item[:2]
            xian = data_item[2:-1]
            zhou_xian_dict[xian] = zhou
        if len(data_item) >= 4 and data_item[2] == "州" and data_item[-1] == "縣":
            zhou = data_item[:3]
            xian = data_item[3:-1]
            zhou_xian_dict[xian] = zhou

    for data_item in fu_data["children"]:
        if len(data_item) == 3:
            xian = data_item[:2]
        elif len(data_item) > 2 and data_item[2] == "（":
            xian = data_item[:2]
        elif len(data_item) > 3 and data_item[3] == "（":
            xian = data_item[:3]
        elif len(data_item) >= 2 and data_item[1] == "縣":
            xian = data_item[:2]
        elif len(data_item) >= 3 and data_item[2] == "縣":
            xian = data_item[:2]
        elif len(data_item) >= 4 and data_item[1] == "州" and data_item[-1] == "縣":
            xian = data_item[:2]
        elif len(data_item) >= 4 and data_item[2] == "州" and data_item[-1] == "縣":
            xian = data_item[:3]
        else:
            xian = data_item

        if xian == "縣":
            xian = fu_data["name"]
        if fu_data["name"] == "其他":
            xian = "其他"
        if xian == "" or xian == "　" or xian[0] == "□":
            xian = "其他"

        if xian in zhou_xian_dict:
            xian = zhou_xian_dict[xian]

        if fu_data["name"] == "撫州":
            if xian == "臨川新喻縣":
                xian = xian[:2]
        elif fu_data["name"] == "吉安":
            if xian == "盧陵" or xian == "廬陵縣":
                xian = "廬陵"
        elif fu_data["name"] == "南昌":
            if xian == "豐誠":
                xian = "豐城"
            elif xian == "寍州":
                xian = "寧州"
            elif xian == "進贒":
                xian = "進賢"
            elif xian == "南昌府進賢縣":
                xian = "進賢"
        elif fu_data["name"] == "建昌":
            if xian == "南城縣":
                xian = "南城"
            elif xian == "建昌":
                xian = "其他"
        elif fu_data["name"] == "南安":
            if xian == "大臾":
                xian = "大庾"
        elif fu_data["name"] == "潞安":
            if xian == "":
                xian = "其他"
        elif fu_data["name"] == "平陽":
            if xian == "趙珹":
                xian = "趙城"
        elif fu_data["name"] == "太原":
            if xian == "撫平定州":
                xian = "平定州"
            elif xian[:2] == "岢嵐":
                xian = "岢嵐"
            elif xian == "代州四關一廂" or xian == "代州王里一都" or xian == "代縣":
                xian = "代州"
        elif fu_data["name"] == "紹興":
            if xian == "諸暨西安鄉六十五都" or xian == "諸暨縣":
                xian = "諸暨"
        elif fu_data["name"] == "台州":
            if xian == "大台":
                xian = "天台"
        elif fu_data["name"] == "嘉興":
            if xian == "海塩":
                xian = "海鹽"
            elif xian == "撫平湖縣":
                xian = "平湖"
        elif fu_data["name"] == "湖州":
            if xian == "安吉州":
                xian = "安吉"
        elif fu_data["name"] == "福州":
            if xian == "閔縣":
                xian = "閩縣"
            elif xian == "官府長樂縣":
                xian = "長樂"
        elif fu_data["name"] == "興化":
            if xian == "浦田" or xian == "圃田" or xian == "蒲田":
                xian = "莆田"
            elif xian == "遷遊" or xian == "仙游":
                xian = "仙遊"
        elif fu_data["name"] == "泉州":
            if xian == "普江":
                xian = "晉江"
        elif fu_data["name"] == "漳州":
            if xian == "漳蒲" or xian == "彰浦":
                xian = "漳浦"
        elif fu_data["name"] == "桂林":
            if xian == "金州":
                xian = "全州"
        elif fu_data["name"] == "梧州":
            if xian == "欎林州南廂第一圖":
                xian = "鬱林"
        elif fu_data["name"] == "南陽":
            if xian == "鄧州內鄉縣上白亭保":
                xian = "鄧州"
            elif xian == "汝川壽永鄉西八里保":
                xian = "汝州"
        elif fu_data["name"] == "開封":
            if xian[:2] == "歸德":
                xian = "歸德"
            elif xian == "許州襄城":
                xian = "許州"
            elif xian == "祥府":
                xian = "祥符"
            elif xian == "雎州":
                xian = "睢州"
            elif xian == "":
                xian = ""
        elif fu_data["name"] == "河南":
            if xian == "陜州":
                xian = "陝州"
            elif xian == "永寍":
                xian = "永寧"
        elif fu_data["name"] == "汝寧":
            if xian == "信陽州":
                xian = "信陽"
        elif fu_data["name"] == "廣州":
            if xian == "東菀" or xian == "東筦":
                xian = "東莞"
        elif fu_data["name"] == "惠州":
            if xian == "衛軍":
                xian = "其他"
            elif xian == "慱羅":
                xian = "博羅"
        elif fu_data["name"] == "西安":
            if xian == "華洲渭南縣":
                xian = "華州"
            elif xian == "盩屋":
                xian = "盩厔"
            elif xian[:2] == "乾州" or xian[:2] == "乾洲":
                xian = "乾州"
        elif fu_data["name"] == "延安":
            if xian[:2] == "綏德":
                xian = "綏德"
        elif fu_data["name"] == "河州":
            if xian == "衛軍民指揮司":
                xian = "其他"
        elif fu_data["name"] == "鳳翔":
            if xian == "寶鷄":
                xian = "寶雞"
        elif fu_data["name"] == "鞏昌":
            if xian == "會寍":
                xian = "會寧"
            elif xian == "縣隴西縣":
                xian = "隴西"
        elif fu_data["name"] == "常州":
            if xian == "江府陰縣" or xian == "江隂":
                xian = "江陰"
        elif fu_data["name"] == "蘇州":
            if xian == "崐山":
                xian = "崑山"
            elif xian == "太倉州":
                xian = "太倉"
            elif xian == "長熟":
                xian = "常熟"
            elif xian == "常州":
                xian = "長洲"
            elif xian == "大倉":
                xian = "太倉"
            elif xian == "嘉定榮縣":
                xian = "嘉定"
        elif fu_data["name"] == "池州":
            if xian == "石碌":
                xian = "石埭"
        elif fu_data["name"] == "應天":
            if xian == "漂陽":
                xian = "溧陽"
        elif fu_data["name"] == "淮安":
            if xian == "沐陽":
                xian = "沭陽"
        elif fu_data["name"] == "廬州":
            if xian == "無為州":
                xian = "無為"
        elif fu_data["name"] == "鳳陽":
            if xian == "宿州靈璧":
                xian = "宿州"
            elif xian == "潁州":
                xian = "頴州"
            elif xian == "亳州":
                xian = "毫州"
        elif fu_data["name"] == "揚州":
            if xian == "高郵州":
                xian = "高郵"
            elif xian == "":
                xian = ""
        elif fu_data["name"] == "徽州":
            if xian == "休寍":
                xian = "休寧"
        elif fu_data["name"] == "寧國":
            if xian == "大平":
                xian = "太平"
        elif fu_data["name"] == "和州":
            if xian == "在城第六里" or xian == "在城第九里":
                xian = "其他"
        elif fu_data["name"] == "保定":
            if xian == "蠡州" or xian == "縣蠡":
                xian = "蠡縣"
            elif xian == "愽野":
                xian = "博野"
        elif fu_data["name"] == "大名":
            if xian == "渭縣":
                xian = "魏縣"
            elif xian == "開封長垣縣":
                xian = "其他"
        elif fu_data["name"] == "真定":
            if xian == "藳城" or xian == "藁縣":
                xian = "藁城"
            elif xian == "":
                xian = ""
        elif fu_data["name"] == "順天":
            if xian == "昌平州":
                xian = "昌平"
            elif xian == "州寶坻縣":
                xian = "寶坻"
            elif xian == "薊□" or xian[:2] == "錦衣":
                xian = "其他"
        elif fu_data["name"] == "永平":
            if xian == "廬龍":
                xian = "盧龍"
            elif xian == "欒州":
                xian = "灤州"
        elif fu_data["name"] == "兖州":
            if xian[:2] == "東平":
                xian = "東平"
            elif xian[:2] == "濟寧":
                xian = "濟寧"
            elif xian[:2] == "泰安":
                xian = "泰安"
        elif fu_data["name"] == "濟南":
            if xian == "武定州":
                xian = "武定"
            elif xian == "濟東":
                xian = "齊東"
            elif xian == "泰安州":
                xian = "泰安"
        elif fu_data["name"] == "青州":
            if xian == "菖州":
                xian = "莒州"
            elif xian == "臨胊":
                xian = "臨朐"
        elif fu_data["name"] == "登州":
            if xian == "寧海州":
                xian = "寧海"
            elif xian == "菜陽":
                xian = "萊陽"
        elif fu_data["name"] == "萊州":
            if xian == "平度州":
                xian = "平度"
        elif fu_data["name"] == "東昌":
            if xian[:2] == "臨清":
                xian = "臨清"
            elif xian == "唐邑" or xian == "堂巴":
                xian = "堂邑"
            elif xian == "高唐州":
                xian = "高唐"
            elif xian == "荏平":
                xian = "茌平"
            elif xian == "愽平":
                xian = "博平"
        elif fu_data["name"] == "重慶":
            if xian == "江律":
                xian = "江津"
        elif fu_data["name"] == "成都":
            if xian == "温江":
                xian = "溫江"
            elif xian == "重慶州" or xian == "崇慶州四安鄉":
                xian = "崇慶"
            elif xian == "漢川":
                xian = "漢州"
            elif xian == "後衛新都驛":
                xian = "新都"
        elif fu_data["name"] == "順慶":
            if xian == "廣安州":
                xian = "廣安"
            elif xian == "南𠑽":
                xian = "南充"
        elif fu_data["name"] == "馬湖":
            if xian == "平夷長官司":
                xian = "平夷"
        elif fu_data["name"] == "保寧":
            if xian == "劔州" or xian == "劒州":
                xian = "劍州"
            elif xian == "巴州":
                xian = "巴縣"
        elif fu_data["name"] == "荊州":
            if xian == "夷陵州":
                xian = "夷陵"
            elif xian == "石守":
                xian = "石首"
        elif fu_data["name"] == "郴州":
            if xian == "桂楊":
                xian = "桂陽"
            elif xian == "秀才鄉 ":
                xian = "其他"
        elif fu_data["name"] == "承天":
            if xian == "安陸州":
                xian = "安陸"
            elif xian[:2] == "沔陽":
                xian = "沔陽"
            elif xian == "潜江":
                xian = "潛江"
        elif fu_data["name"] == "岳州":
            if xian == "華密":
                xian = "華容"
        elif fu_data["name"] == "德安":
            if xian == "随州":
                xian = "隨州"
        elif fu_data["name"] == "武昌":
            if xian == "興國州":
                xian = "興國"
            elif xian == "蒲沂":
                xian = "蒲圻"
            elif xian == "縣嘉魚縣":
                xian = "嘉魚"
            elif xian == "咸寍":
                xian = "咸寧"
        elif fu_data["name"] == "衡州":
            if xian == "桂陽州":
                xian = "桂陽"
        elif fu_data["name"] == "黃州":
            if xian == "蘄州第三坊" or xian == "蔪州" or xian == "靳州":
                xian = "蘄州"
            elif xian == "鄿水":
                xian = "蘄水"
            elif xian == "黃崗":
                xian = "黃岡"
        elif fu_data["name"] == "衛":
            xian = "衛"
        elif fu_data["name"] == "所":
            xian = "所"
        elif fu_data["name"] == "大理":
            if xian == "寺太和縣":
                xian = "太和"
        elif fu_data["name"] == "未知":
            xian = "未知"

        if xian not in num_xian:
            num_xian[xian] = 1
            xian_data.append(
                (
                    {
                        "name": xian,
                        "value": 1
                    }
                )
            )
        else:
            num_xian[xian] += 1
            for xian_item in xian_data:
                if xian_item["name"] == xian:
                    xian_item["value"] += 1
                    break
    
    return xian_data


def process_fu_data(si_data):
    fu_data = []
    num_fu = {}
    for data_item in si_data["children"]:
        fu = data_item[:2]
        jiguan = data_item[2:]

        if len(fu) > 0 and (fu[0] == "府" or fu[0] == "縣"):
            fu = fu[1:] + jiguan[0]
            jiguan = jiguan[1:]
        if len(jiguan) > 0 and jiguan[0] == "州":
            fu = fu + "州"
            jiguan = jiguan[1:]
        if len(jiguan) > 0 and jiguan[0] == "府":
            jiguan = jiguan[1:]

        if si_data["name"] == "北直隸":
            if fu == "北平":
                fu = "順天"
        elif si_data["name"] == "南直隸":
            if fu == "盧州":
                fu = "廬州"
            elif fu == "懷安":
                fu = "淮安"
            elif fu == "楊州":
                fu = "揚州"
            elif fu == "寍國":
                fu = "寧國"
        elif si_data["name"] == "陝西":
            if fu in ["同州", "盩厔", "長安", "醴泉", "華陰", "涇陽", "藍田", "咸寧", "臨潼", "商州", "朝邑"]:
                jiguan = fu + jiguan
                fu = "西安"
            elif fu == "郃陽" or fu == "澄城":
                jiguan = "同州" + fu + jiguan
                fu = "西安"
            elif jiguan == "涇陽縣":
                fu = "西安"
            elif fu == "平凉":
                fu = "平涼"
            elif fu == "岐山":
                jiguan = fu + jiguan
                fu = "鳳翔"
            elif fu == "宜川":
                jiguan = fu + jiguan
                fu = "延安"
            elif fu == "狄道":
                jiguan = fu + jiguan
                fu = "臨洮"
            elif fu in ["神木", "寧州", "行都"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "山西":
            if fu == "潞州":
                fu = "潞安"
            elif fu == "澤洲":
                fu = "澤州"
            elif fu == "汾洲":
                fu = "汾州"
            elif fu in ["平定州", "陽曲", "榆次", "代州", "文水", "清源", "石州", "太谷", "忻州"]:
                jiguan = fu + jiguan
                fu = "太原"
            elif fu in ["太平", "臨汾", "稷山", "猗氏", "蒲州", "萬泉", "襄陵", "安邑", "洪洞", "絳州", "平陸", "夏縣", "趙城", "臨晉"]:
                jiguan = fu + jiguan
                fu = "平陽"
            elif fu in ["陵川", "黎城", "潞城", "襄垣"]:
                jiguan = fu + jiguan
                fu = "潞安"
            elif fu in ["蔚州", "渾源州", "懷仁", "應州", "馬邑"]:
                jiguan = fu + jiguan
                fu = "大同"
            elif fu in ["孝義"]:
                jiguan = fu + jiguan
                fu = "汾州"
            elif fu in ["靈川"]:
                jiguan = fu + jiguan
                fu = "澤州"
            elif fu in ["榆社"]:
                jiguan = fu + jiguan
                fu = "遼州"
            elif fu in ["都司", "臨縣", "望成", "壼關", "廣靈", "隰州", "文山", "儀衛"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "山東":
            if fu == "兗州" or fu == "兊州" or fu == "袞州":
                fu = "兖州"
            elif fu == "暨州":
                fu = "登州"
            elif fu == "青洲":
                fu = "青州"
            elif fu == "菜州":
                fu = "萊州"
            elif fu in ["東平", "濟寧州", "單縣", "滕縣", "汶上", "曹縣", "東平州", "泰安", "曹州"]:
                jiguan = fu + jiguan
                fu = "兖州"
            elif fu in ["日照", "沂水", "莒州", "高苑", "諸城", "臨朐", "益都", "安丘"]:
                jiguan = fu + jiguan
                fu = "青州"
            elif fu in ["武定州", "歷城", "齊河", "濱州", "德州", "平原", "長山", "禹城", "淄川", "齊東"]:
                jiguan = fu + jiguan
                fu = "濟南"
            elif fu in ["館陶", "恩縣", "濮州"]:
                jiguan = fu + jiguan
                fu = "東昌"
            elif fu in ["昌邑", "掖縣", "膠州", "平度州"]:
                jiguan = fu + jiguan
                fu = "萊州"
            elif fu in ["蓬萊", "萊陽", "黃縣", "招遠", "文登"]:
                jiguan = fu + jiguan
                fu = "登州"
            elif fu in ["□"]:
                jiguan = fu + jiguan
                fu = "其他"
            elif fu == "貴州":
                fu = "青州"
                jiguan == "日照縣"
        elif si_data["name"] == "河南":
            if fu == "汝寕" or fu == "汝寍":
                fu = "汝寧"
            elif fu == "懷德":
                fu = "懷慶"
            elif fu == "開州" or fu == "開府":
                fu = "開封"
            elif fu in ["陝州", "洛陽", "孟津", "靈寶", "偃師", "嵩縣"]:
                jiguan = fu + jiguan
                fu = "河南"
            elif fu in ["光州", "信陽州", "息縣", "固始", "上蔡"]:
                jiguan = fu + jiguan
                fu = "汝寧"
            elif fu in ["祥符", "郾城" ,"夏邑", "扶溝", "太康", "歸德", "歸德州", "陳留", "鹿邑", "項城", "蘭陽", "封丘"]:
                jiguan = fu + jiguan
                fu = "開封"
            elif fu in ["汝州", "郟縣", "裕州", "唐縣"]:
                jiguan = fu + jiguan
                fu = "南陽"
            elif fu in ["獲嘉", "汲縣"]:
                jiguan = fu + jiguan
                fu = "衛輝"
            elif fu in ["□", "信陽", "□□"]:
                jiguan = fu + jiguan
                fu = "其他"
            elif fu == "南陽" and jiguan == "洛陽縣":
                fu = "河南"
        elif si_data["name"] == "浙江":
            if fu == "明州" or fu == "寍波" or fu == "寧江":
                fu = "寧波"
            elif fu == "温州" or fu == "知州":
                fu = "溫州"
            elif fu == "巖州":
                fu = "嚴州"
            elif fu == "照興":
                fu = "紹興"
            elif fu == "今華":
                fu = "金華"
            elif fu in ["仁和", "錢塘", "臨安", "海寧"]:
                jiguan = fu + jiguan
                fu = "杭州"
            elif fu in ["西安", "開化", "常山", "龍游"]:
                jiguan = fu + jiguan
                fu = "衢州"
            elif fu in ["鄞縣", "定海", "慈谿"]:
                jiguan = fu + jiguan
                fu = "寧波"
            elif fu in ["山陰", "餘姚", "蕭山", "會稽", "上虞", "嵊縣", "餘杭", "諸暨"]:
                jiguan = fu + jiguan
                fu = "紹興"
            elif fu in ["景寧", "麗水", "遂昌"]:
                jiguan = fu + jiguan
                fu = "處州"
            elif fu in ["海鹽", "崇德", "秀水", "平湖", "桐鄉"]:
                jiguan = fu + jiguan
                fu = "嘉興"
            elif fu in ["天台", "臨海", "黃巖", "寧海"]:
                jiguan = fu + jiguan
                fu = "台州"
            elif fu in ["安吉", "長興", "烏程", "德清"]:
                jiguan = fu + jiguan
                fu = "湖州"
            elif fu in ["建德"]:
                jiguan = fu + jiguan
                fu = "嚴州"
            elif fu in ["蘭谿", "義烏", "東陽"]:
                jiguan = fu + jiguan
                fu = "金華"
            elif fu in ["瑞安", "永嘉"]:
                jiguan = fu + jiguan
                fu = "溫州"
            elif fu in ["新城", "□縣", "□□", "慶元", "黃岩"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "江西":
            if fu == "康定":
                fu = "南康"
            elif fu == "臨州":
                fu = "瑞州"
            elif fu == "隴江" or fu == "臨安":
                fu = "臨江"
            elif fu == "廣州":
                fu = "廣信"
            elif fu == "饒洲":
                fu = "饒州"
            elif fu in ["吉水", "廬陵", "龍泉", "安福", "泰和", "永豐", "萬安", "吉永"]:
                jiguan = fu + jiguan
                fu = "吉安"
            elif fu in ["興國", "贛縣"]:
                jiguan = fu + jiguan
                fu = "贛州"
            elif fu in ["鄱陽", "安仁", "樂平", "餘干", "浮梁"]:
                jiguan = fu + jiguan
                fu = "饒州"
            elif fu in ["新淦", "新喻", "清江", "峽江"]:
                jiguan = fu + jiguan
                fu = "臨江"
            elif fu in ["新建", "進賢", "豐城", "武寧"]:
                jiguan = fu + jiguan
                fu = "南昌"
            elif fu in ["臨川", "樂安", "崇仁", "金谿"]:
                jiguan = fu + jiguan
                fu = "撫州"
            elif fu in ["宜春", "萍鄉"]:
                jiguan = fu + jiguan
                fu = "袁州"
            elif fu in ["南豐"]:
                jiguan = fu + jiguan
                fu = "建昌"
            elif fu in ["貴溪"]:
                jiguan = fu + jiguan
                fu = "廣信"
            elif fu in ["高安"]:
                jiguan = fu + jiguan
                fu = "瑞州"
            elif fu in ["大庾", "大臾"]:
                jiguan = fu + jiguan
                fu = "南安"
            elif fu in ["德化"]:
                jiguan = fu + jiguan
                fu = "九江"
            elif fu in ["□", "眉州", "□縣", "□□", "上猶"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "湖廣":
            if fu == "溪州":
                fu = "衡州"
            elif fu == "民昌":
                fu = "武昌"
            elif fu == "黄州" or fu == "黃洲":
                fu = "黃州"
            elif fu == "寶應":
                fu = "寶慶"
            elif fu in ["安陸州", "沔陽州", "京山", "安陸"]:
                jiguan = fu + jiguan
                fu = "承天"
            elif fu in ["茶陵", "攸縣", "湘陰", "湘鄉", "茶陵州"]:
                jiguan = fu + jiguan
                fu = "長沙"
            elif fu in ["桂陽", "衡山", "酃縣"]:
                jiguan = fu + jiguan
                fu = "衡州"
            elif fu in ["漢川"]:
                jiguan = fu + jiguan
                fu = "漢陽"
            elif fu in ["桃源", "龍陽"]:
                jiguan = fu + jiguan
                fu = "常德"
            elif fu in ["盧溪", "湘潭"]:
                jiguan = fu + jiguan
                fu = "辰州"
            elif fu in ["蒲圻" ,"嘉魚", "大冶", "江夏"]:
                jiguan = fu + jiguan
                fu = "武昌"
            elif fu in ["巴陵"]:
                jiguan = fu + jiguan
                fu = "岳州"
            elif fu in ["黃岡", "黃梅", "羅田", "麻城", "黃崗", "黃陂", "蘄州"]:
                jiguan = fu + jiguan
                fu = "黃州"
            elif fu in ["夷陵州", "江陵", "監利", "公安"]:
                jiguan = fu + jiguan
                fu = "荊州"
            elif fu in ["零陵"]:
                jiguan = fu + jiguan
                fu = "永州"
            elif fu in ["雲夢"]:
                jiguan = fu + jiguan
                fu = "德安"
            elif fu in ["□州", "鄖陽"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "四川":
            if fu == "嘉定州":
                fu = "嘉定"
            elif fu == "叙州":
                fu = "敘州"
            elif fu == "虁州":
                fu = "夔州"
            elif fu == "潼川州" or fu == "潼州州":
                fu = "潼川"
            elif fu == "":
                fu = ""
            elif fu in ["眉州"]:
                jiguan = fu + jiguan
                fu = "嘉定"
            elif fu in ["巴縣"]:
                jiguan = fu + jiguan
                fu = "重慶"
            elif fu in ["安岳"]:
                jiguan = fu + jiguan
                fu = "潼川"
            elif fu in ["閬中"]:
                jiguan = fu + jiguan
                fu = "保寧"
            elif fu in ["綿州", "內江", "德陽"]:
                jiguan = fu + jiguan
                fu = "成都"
            elif fu in ["富順"]:
                jiguan = fu + jiguan
                fu = "敘州"
            elif fu in ["合江"]:
                jiguan = fu + jiguan
                fu = "瀘州"
            elif fu in ["永寧", "卭州", "雅州"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "廣東":
            if fu == "廣東":
                fu = "廣州"
            elif fu in ["吳川", "茂名"]:
                jiguan = fu + jiguan
                fu = "高州"
            elif fu in ["番禺", "東莞", "新會"]:
                jiguan = fu + jiguan
                fu = "廣州"
            elif fu in ["高要", "四會"]:
                jiguan = fu + jiguan
                fu = "肇慶"
            elif fu in ["□", "□□", "恩平"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "福建":
            if fu == "汀洲":
                fu = "汀州"
            elif fu == "廷平":
                fu = "延平"
            elif fu in ["莆田"]:
                jiguan = fu + jiguan
                fu = "興化"
            elif fu in ["沙縣", "尤溪", "永安"]:
                jiguan = fu + jiguan
                fu = "延平"
            elif fu in ["閩縣", "懷安", "福清", "連江", "長樂"]:
                jiguan = fu + jiguan
                fu = "福州"
            elif fu in ["建安", "崇安"]:
                jiguan = fu + jiguan
                fu = "建寧"
            elif fu in ["同安", "晉江", "惠安"]:
                jiguan = fu + jiguan
                fu = "泉州"
            elif fu in ["□□", "□州", "□", "", "政和", "清縣"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "貴州":
            if fu in ["貴州", "宣慰"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "雲南":
            if fu == "太理":
                fu = "大理"
            elif fu in ["嵩明州", "安寧州"]:
                jiguan = fu + jiguan
                fu = "雲南"
            elif fu in ["□", "霑益州"]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "交阯":
            if fu == "交阯":
                fu = "交州"
            elif fu in ["多翼"]:
                jiguan = fu + jiguan
                fu = "新安"
            elif fu in ["扶寧"]:
                jiguan = fu + jiguan
                fu = "交州"
            elif fu in [""]:
                jiguan = fu + jiguan
                fu = "其他"
        elif si_data["name"] == "衛所":
            jiguan = fu + jiguan
            if jiguan[-1] == "衛":
                fu = "衛"
            elif jiguan[-1] == "所":
                fu = "所"
        elif si_data["name"] == "未知":
            jiguan = fu + jiguan
            fu = "未知"

        if fu not in num_fu:
            num_fu[fu] = 1
            fu_data.append(
                (
                    {
                        "name": fu,
                        "children": [jiguan],
                        "value": 1
                    }
                )
            )
        else:
            num_fu[fu] += 1
            for fu_item in fu_data:
                if fu_item["name"] == fu:
                    fu_item["children"].append(jiguan)
                    fu_item["value"] += 1
                    break
    
    for fu_item in fu_data:
        fu_item["children"] = process_xian_data(fu_item)
        fu_item["children"].sort(key=lambda x:x["value"], reverse=True)
    
    return fu_data


def process_si_data(native_data):
    si_data = []
    num_si = {}
    for data_item in native_data:
        jiguan = data_item["籍貫"]
        if len(jiguan) > 1 and (jiguan[-1] == "人" or jiguan[-1] == "籍"):
            jiguan = jiguan[:-1]
        if len(jiguan) > 1 and (jiguan[-1] == "衛" or jiguan[-1] == "所"):
            si = "衛所"
        else:
            si = jiguan[:2]
            jiguan = jiguan[2:]
        if len(jiguan) > 1 and (jiguan[0] == "州" or jiguan[0] == "省"):
            jiguan = jiguan[1:]
        
        if si == "高麗" or si == "□府" or si == "□" or si == "" or si == "宿松":
            si = "未知"
        elif si == "交趾":
            si = "交阯"
        elif si == "福見":
            si = "福建"
        elif si == "西川":
            si = "四川"
        elif si == "北平" or si == "平燕":
            si = "北直隸"
        elif si == "湖南":
            si = "河南"
        elif si == "南京":
            si == "應天"
            jiguan = si + jiguan
            si = "南直隸"
        elif si == "順天" or si == "大寧":
            jiguan = si + jiguan
            si = "北直隸"
        elif si == "徐州" or si == "應天":
            jiguan = si + jiguan
            si = "南直隸"
        elif si == "直隸":
            if jiguan[:2] in ["保定", "大名", "永平", "河間", "真定", "順德", "廣平", "順天"]:
                si = "北直隸"
            elif jiguan[:2] in ["常州", "松江", "池州", "蘇州", "淮安", "太平", "廬州", "鳳陽", "揚州", "安慶", "徽州", "應天", "寧國", "鎮江", "廣德", "滁州", "徐州", "懷安", "盧州", "和州", "楊州", "寍國"]:
                si = "南直隸"
        elif si == "陜西":
            si = "陝西"

        if si in ["□功", "驍騎", "永清", "彭城", "義勇", "武功", "浙杭", "遼陽", "萬全", "燕山", "南息", "東□", "本州", "金吾", "□光", "□□", "□山", "□惠", "□南", "保安", "□縣", "桂陽", "榆林", "青浦", "山陰", "上林", "定邊", "榮德", "納谿", "愽羅", "郫縣", "晉守", "撫山", "廣武", "鎮西"]:
            jiguan = si + jiguan
            si = "未知"
        elif si in ["衡州", "常德", "武昌", "沔陽", "承天", "黃州", "長沙", "安陸", "荊州"]:
            jiguan = si + jiguan
            si = "湖廣"
        elif si in ["廣德", "蘇州", "揚州", "安慶", "松江", "常州", "徽州", "鳳陽", "鎮江", "廬州"]:
            jiguan = si + jiguan
            si = "南直隸"
        elif si in ["太原", "大同", "平陽"]:
            jiguan = si + jiguan
            si = "山西"
        elif si in ["西安", "延安", "鞏昌"]:
            jiguan = si + jiguan
            si = "陝西"
        elif si in ["潯州", "柳州"]:
            jiguan = si + jiguan
            si = "廣西"
        elif si in ["大理"]:
            jiguan = si + jiguan
            si = "雲南"
        elif si in ["成都", "順慶", "敘州", "重慶"]:
            jiguan = si + jiguan
            si = "四川"
        elif si in ["開封", "南陽"]:
            jiguan = si + jiguan
            si = "河南"
        elif si in ["保定", "河間"]:
            jiguan = si + jiguan
            si = "北直隸"
        elif si in ["杭州", "嘉興", "紹興", "寧波", "處州"]:
            jiguan = si + jiguan
            si = "浙江"
        elif si in ["興化", "福州", "泉州", "漳州"]:
            jiguan = si + jiguan
            si = "福建"
        elif si in ["濟南", "登州", "萊州", "青州"]:
            jiguan = si + jiguan
            si = "山東"
        elif si in ["建昌"]:
            jiguan = si + jiguan
            si = "江西"
        
        elif si == "當塗" or si == "蕪湖":
            jiguan = "太平府" + si + jiguan
            si = "南直隸"
        elif si == "錦衣" or si == "宛平" or si == "大興":
            jiguan = "順天府" + si + jiguan
            si = "北直隸"
        elif si == "遼東" or si == "諸城":
            jiguan = "青州府" + si + jiguan
            si = "山東"
        elif si == "宜賓" or si == "富順":
            jiguan = "敘州府" + si + jiguan
            si = "四川"
        elif si == "盩厔" or si == "咸寧" or si == "涇陽" or si == "興平":
            jiguan = "西安府" + si + jiguan
            si = "陝西"
        elif si == "海鹽" or si == "嘉善" or si == "平湖" or si == "秀水" or si == "桐鄉":
            jiguan = "嘉興府" + si + jiguan
            si = "浙江"
        elif si == "南海" or si == "番禺":
            jiguan = "廣州府" + si + jiguan
            si = "廣東"
        elif si == "閩縣" or si == "懷安" or si == "侯官" or si == "福清" or si == "候官":
            jiguan = "福州府" + si + jiguan
            si = "福建"
        elif si == "仁和" or si == "錢塘" or si == "臨安":
            jiguan = "杭州府" + si + jiguan
            si = "浙江"
        elif si == "仁壽" or si == "雙流" or si == "華陽" or si == "温江":
            jiguan = "成都府" + si + jiguan
            si = "四川"
        elif si == "長洲" or si == "崑山" or si == "常熟" or si == "吳江" or si == "吳縣" or si == "太倉" or si == "嘉定":
            jiguan = "蘇州府" + si + jiguan
            si = "南直隸"
        elif si == "保昌":
            jiguan = "南雄府" + si + jiguan
            si = "廣東"
        elif si == "餘姚" or si == "上虞":
            jiguan = "紹興府" + si + jiguan
            si = "浙江"
        elif si == "平涼":
            jiguan = "平涼府" + si + jiguan
            si = "陝西"
        elif si == "江都" or si == "泰州" or si == "儀真" or si == "高郵":
            jiguan = "揚州府" + si + jiguan
            si = "南直隸"
        elif si == "婺源" or si == "休寧" or si == "祁門":
            jiguan = "徽州府" + si + jiguan
            si = "南直隸"
        elif si == "代州" or si == "榆次" or si == "岢嵐":
            jiguan = "太原府" + si + jiguan
            si = "山西"
        elif si == "臨清":
            jiguan = "東昌府" + si + jiguan
            si = "山東"
        elif si == "遂寧":
            jiguan = "潼川" + si + jiguan
            si = "四川"
        elif si == "寧海":
            jiguan = "台州府" + si + jiguan
            si = "浙江"
        elif si == "廣濟":
            jiguan = "黄州府" + si + jiguan
            si = "湖廣"
        elif si == "新昌" or si == "高縣":
            jiguan = "瑞州府" + si + jiguan
            si = "江西"
        elif si == "巢縣":
            jiguan = "廬州府無為州" + si + jiguan
            si = "南直隸"
        elif si == "句容" or si == "江浦":
            jiguan = "應天府" + si + jiguan
            si = "南直隸"
        elif si == "攸縣":
            jiguan = "長沙府" + si + jiguan
            si = "湖廣"
        elif si == "臨桂":
            jiguan = "桂林府" + si + jiguan
            si = "廣西"
        elif si == "武鄉":
            jiguan = "沁州" + si + jiguan
            si = "山西"
        elif si == "盧龍":
            jiguan = "永平府" + si + jiguan
            si = "北直隸"
        elif si == "博羅":
            jiguan = "惠州府" + si + jiguan
            si = "廣東"
        elif si == "白水":
            jiguan = "西安府同州" + si + jiguan
            si = "陝西"
        elif si == "南昌" or si == "進賢" or si == "新建":
            jiguan = "南昌府" + si + jiguan
            si = "江西"
        elif si == "丹陽":
            jiguan = "鎮江府" + si + jiguan
            si = "南直隸"
        elif si == "定遠" or si == "泗州":
            jiguan = "鳳陽府" + si + jiguan
            si = "南直隸"
        elif si == "祁陽":
            jiguan = "永州府" + si + jiguan
            si = "湖廣"
        elif si == "岐山":
            jiguan = "鳳翔府" + si + jiguan
            si = "陝西"
        elif si == "歸德" or si == "襄城" or si == "杞縣":
            jiguan = "開封府" + si + jiguan
            si = "河南"
        elif si == "西充" or si == "南充":
            jiguan = "順慶府" + si + jiguan
            si = "四川"
        elif si == "建德":
            jiguan = "嚴州府" + si + jiguan
            si = "浙江"
        elif si == "無錫" or si == "江陰" or si == "江隂" or si == "宜興":
            jiguan = "常州府" + si + jiguan
            si = "南直隸"
        elif si == "京山":
            jiguan = "安陸州" + si + jiguan
            si = "湖廣"
        elif si == "上海" or si == "華亭":
            jiguan = "松江府" + si + jiguan
            si = "南直隸"
        elif si == "順德":
            jiguan = "廣州府" + si + jiguan
            si = "廣東"
        elif si == "晉江" or si == "同安":
            jiguan = "泉州府" + si + jiguan
            si = "福建"
        elif si == "濬縣" or si == "滑縣":
            jiguan = "大名府" + si + jiguan
            si = "北直隸"
        elif si == "閬中":
            jiguan = "保寧府" + si + jiguan
            si = "四川"
        elif si == "高陽" or si == "定興" or si == "完縣":
            jiguan = "保定府" + si + jiguan
            si = "北直隸"
        elif si == "安福":
            jiguan = "吉安府" + si + jiguan
            si = "江西"
        elif si == "麗水":
            jiguan = "處州府" + si + jiguan
            si = "浙江"
        elif si == "德州" or si == "武定":
            jiguan = "濟南府" + si + jiguan
            si = "山東"
        elif si == "招遠" or si == "萊陽":
            jiguan = "登州府" + si + jiguan
            si = "山東"
        elif si == "清江" or si == "新喻":
            jiguan = "臨江府" + si + jiguan
            si = "江西"
        elif si == "龍溪" or si == "漳浦":
            jiguan = "漳州府" + si + jiguan
            si = "福建"
        elif si == "德清" or si == "烏程" or si == "歸安" or si == "廬陵" or si == "安吉" or si == "武康":
            jiguan = "湖州府" + si + jiguan
            si = "浙江"
        elif si == "鍾祥":
            jiguan = "承天府" + si + jiguan
            si = "湖廣"
        elif si == "臨川":
            jiguan = "撫州府" + si + jiguan
            si = "江西"
        elif si == "馬平" or si == "賓州":
            jiguan = "柳州府" + si + jiguan
            si = "廣西"
        elif si == "通山" or si == "江夏":
            jiguan = "武昌府" + si + jiguan
            si = "湖廣"
        elif si == "襄陽":
            jiguan = "襄陽府" + si + jiguan
            si = "湖廣"
        elif si == "天津":
            jiguan = "河間府" + si + jiguan
            si = "北直隸"
        elif si == "西汾":
            si = "汾州"
            jiguan = si + jiguan
            si = "山西"
        elif si == "光山" or si == "汝陽" or si == "新蔡":
            jiguan = "汝寧府" + si + jiguan
            si = "河南"
        elif si == "臨汾" or si == "蒲州":
            jiguan = "平陽府" + si + jiguan
            si = "山西"
        elif si == "安仁":
            jiguan = "饒州府" + si + jiguan
            si = "江西"
        elif si == "洛陽" or si == "孟津":
            jiguan = "河南府" + si + jiguan
            si = "河南"
        elif si == "永年":
            jiguan = "廣平府" + si + jiguan
            si = "北直隸"
        elif si == "慈谿":
            jiguan = "寧波府" + si + jiguan
            si = "浙江"
        elif si == "麻城" or si == "蘄水":
            jiguan = "黃州府" + si + jiguan
            si = "湖廣"
        elif si == "潛山" or si == "桐城":
            jiguan = "安慶府" + si + jiguan
            si = "南直隸"
        elif si == "米脂":
            jiguan = "延安府" + si + jiguan
            si = "陝西"
        elif si == "太和":
            jiguan = "大理府" + si + jiguan
            si = "雲南"
        elif si == "莆田" or si == "仙遊":
            jiguan = "興化府" + si + jiguan
            si = "福建"
        elif si == "汲縣":
            jiguan = "衛輝府" + si + jiguan
            si = "河南"
        elif si == "山陽" or si == "海州":
            jiguan = "淮安府" + si + jiguan
            si = "南直隸"
        elif si == "河陰":
            jiguan = "開封府鄭州" + si + jiguan
            si = "河南"
        elif si == "應元":
            si = "應天"
            jiguan = si + jiguan
            si = "南直隸"
        elif si == "潼川":
            jiguan = "潼川" + jiguan
            si = "四川"
        elif si == "永嘉":
            jiguan = "溫州府" + si + jiguan
            si = "浙江"
        elif si == "鄞縣":
            jiguan = "明州府" + si + jiguan
            si = "浙江"
        elif si == "瀋陽" or si == "廣寧":
            jiguan = "青州府遼東" + si + jiguan
            si = "山東"
        elif si == "夏邑":
            jiguan = "開封府歸德州" + si + jiguan
            si = "河南"

        elif si == " 山":
            jiguan = jiguan[1:]
            si = "山西"
        elif si == "廣州":
            si = "廣東"
        elif si == "山西":
            if jiguan[:2] == "濟南" or jiguan[:2] == "兖州":
                si = "山東"
        elif si == "山東":
            if jiguan[:2] == "太原" or jiguan[:2] == "潞安":
                si = "山西"
        elif si == "河南":
            if jiguan[:2] == "臨潼":
                si = "陝西"
            elif jiguan[:2] == "武寧":
                si = "江西"
        elif si == "浙江":
            if jiguan[:2] == "龍泉":
                si = "江西"
        elif si == "江西":
            if jiguan[:2] == "澤州":
                si = "山西"
        
        elif si == "直隸":
            if jiguan == "崑山縣" or jiguan == "崐山縣":
                si = "南直隸"
                jiguan = "蘇州府崑山縣"
            elif jiguan == "隆慶州":
                si = "北直隸"
                jiguan = "延慶州"
            elif jiguan == "長洲縣" or jiguan == "吳縣" or jiguan == "吳江" or jiguan == "崇明縣" or jiguan == "太倉州":
                si = "南直隸"
                jiguan = "蘇州府" + jiguan
            elif jiguan == "潛山縣" or jiguan == "懷寧縣" or jiguan == "桐城縣" or jiguan == "望江縣":
                si = "南直隸"
                jiguan = "安慶府" + jiguan
            elif jiguan == "上海縣" or jiguan == "華亭縣" or jiguan == "華亭":
                si = "南直隸"
                jiguan = "松江府" + jiguan
            elif jiguan == "開州" or jiguan == "滑縣" or jiguan == "東明縣" or jiguan == "濬縣" or jiguan == "長垣縣":
                si = "北直隸"
                jiguan = "大名府" + jiguan
            elif jiguan == "巢縣":
                si = "南直隸"
                jiguan = "廬州府無為州" + jiguan
            elif jiguan == "丹徒縣" or jiguan == "金壇縣" or jiguan == "丹陽縣":
                si = "南直隸"
                jiguan = "鎮江府" + jiguan
            elif jiguan == "江都縣" or jiguan == "高郵州" or jiguan == "興化縣" or jiguan == "通州" or jiguan == "儀真縣":
                si = "南直隸"
                jiguan = "揚州府" + jiguan
            elif jiguan == "天名府開州長垣縣":
                si = "北直隸"
                jiguan = "大名府開州長垣縣"
            elif jiguan == "海門縣":
                si = "南直隸"
                jiguan = "揚州府通州" + jiguan
            elif jiguan == "嘉定縣" or jiguan == "嘉定府嘉定縣":
                si = "南直隸"
                jiguan = "蘇州府嘉定縣"
            elif jiguan == "武進縣" or jiguan == "無錫縣" or jiguan == "江陰縣":
                si = "南直隸"
                jiguan = "常州府" + jiguan
            elif jiguan == "青陽縣":
                si = "南直隸"
                jiguan = "池州府" + jiguan
            elif jiguan == "廬洲府六安州":
                si = "南直隸"
                jiguan = "廬州府六安州"
            elif jiguan == "含山縣":
                si = "南直隸"
                jiguan = "和州" + jiguan
            elif jiguan == "交河縣":
                si = "北直隸"
                jiguan = "河間府" + jiguan
            elif len(jiguan) > 3 and jiguan[:3] == "保定府":
                si = "北直隸"
            elif jiguan == "沭陽縣" or jiguan == "山陽縣" or jiguan == "鹽城縣" or jiguan == "贛榆縣" or jiguan == "桃源縣" or jiguan == "清河縣" or jiguan == "安東縣":
                si = "南直隸"
                jiguan = "淮安府" + jiguan
            elif jiguan == "南昌府豐城縣":
                si = "江西"
            elif jiguan == "吳江縣" or jiguan == "常熟縣":
                si = "南直隸"
                jiguan = "蘇州府" + jiguan
            elif jiguan == "臨淮縣" or jiguan == "壽州" or jiguan == "定遠縣" or jiguan == "虹縣" or jiguan == "盱眙縣" or jiguan == "毫州" or jiguan == "頴上縣" or jiguan == "宿州" or jiguan == "頴州" or jiguan == "五河縣" or jiguan == "靈壁縣" or jiguan == "泗州":
                si = "南直隸"
                jiguan = "鳳陽府" + jiguan
            elif jiguan == "寶應縣":
                si = "南直隸"
                jiguan = "揚州府高郵州" + jiguan
            elif jiguan == "合肥縣" or jiguan == "舒城縣" or jiguan == "無為州":
                si = "南直隸"
                jiguan = "廬州府" + jiguan
            elif jiguan == "冀州" or jiguan == "舒城" or jiguan == "合肥":
                si = "南直隸"
                jiguan = "廬州府" + jiguan
            elif jiguan == "灤州" or jiguan == "盧龍縣" or jiguan == "遷安縣":
                si = "北直隸"
                jiguan = "永平府" + jiguan
            elif jiguan == "當塗縣":
                si = "南直隸"
                jiguan = "太平府" + jiguan
            elif jiguan == "邢臺縣":
                si = "北直隸"
                jiguan = "順德府" + jiguan
            elif jiguan == "如臯縣":
                si = "南直隸"
                jiguan = "揚州府泰州" + jiguan
            elif jiguan == "深州":
                si = "北直隸"
                jiguan = "真定府" + jiguan
            elif jiguan == "新城縣":
                si = "江西"
                jiguan = "建昌府" + jiguan
            elif jiguan == "淶水縣":
                si = "北直隸"
                jiguan = "保定府易州" + jiguan
            elif jiguan == "蠡縣":
                si = "北直隸"
                jiguan = "保定府" + jiguan
            elif jiguan == "揚洲府通州海門縣":
                si = "南直隸"
                jiguan = "揚州府通州海門縣"
            elif jiguan == "休寧縣" or jiguan == "歙縣" or jiguan == "祁門縣":
                si = "南直隸"
                jiguan = "徽州府" + jiguan
            elif jiguan == "饒陽縣":
                si = "北直隸"
                jiguan = "真定府普州" + jiguan
            elif jiguan == "永年縣":
                si = "北直隸"
                jiguan = "廣平府" + jiguan
            elif jiguan == "曲陽縣":
                si = "山西"
                jiguan = "太原府" + jiguan
            elif jiguan == "宣城縣":
                si = "南直隸"
                jiguan = "寧國府" + jiguan
            elif jiguan == "天長縣":
                si = "南直隸"
                jiguan = "鳳陽府泗州" + jiguan
            elif jiguan == "永清縣":
                si = "北直隸"
                jiguan = "順天府" + jiguan
            elif jiguan == "長州府無錫縣":
                si = "南直隸"
                jiguan = "常州府無錫縣"
            elif jiguan == "臨城縣":
                si = "北直隸"
                jiguan = "真定府趙州" + jiguan
            elif jiguan == "𣾢州":
                si = "南直隸"
                jiguan = "鳳陽府頴州"
            elif jiguan == "蒙城縣":
                si = "南直隸"
                jiguan = "鳳陽府壽州" + jiguan
            elif jiguan == "寍圖府太平縣":
                si = "南直隸"
                jiguan = "寧國府太平縣"
            elif jiguan == "來安縣":
                si = "南直隸"
                jiguan = "滁州" + jiguan
            elif jiguan == "延慶州":
                si = "北直隸"
            elif jiguan == "徽川府休寧縣":
                si = "南直隸"
                jiguan = "徽州府休寧縣"
            else:
                si = "未知"

        if si not in num_si:
            num_si[si] = 1
            si_data.append(
                (
                    {
                        "name": si,
                        "children": [jiguan],
                        "value": 1
                    }
                )
            )
        else:
            num_si[si] += 1
            for si_item in si_data:
                if si_item["name"] == si:
                    si_item["children"].append(jiguan)
                    si_item["value"] += 1
                    break
    
    for si_item in si_data:
        si_item["children"] = process_fu_data(si_item)
        si_item["children"].sort(key=lambda x:x["value"], reverse=True)

    return si_data



if __name__ == '__main__':
    file_name = "./Data/ming_jinshilu_52y_release.json"
    jsFile = open(file_name, "r", encoding='utf-8')
    data = json.load(jsFile)
    jsFile.close()
    native_data = data["children"]
    si_data = process_si_data(native_data)
    si_data.sort(key=lambda x:x["value"], reverse=True)
    data = {"name":"mingjinshi", "children": si_data, "value": 14116}

    js = json.dumps(data,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
    jsFile = open("./Treemap/data/xian_data.json", "w+", encoding='utf-8')
    jsFile.write(js)
    jsFile.close()