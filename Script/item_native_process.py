import json



def process_fu(data_item):
    data = data_item["籍貫"]
    si = data_item["司级"]
    fu = data[:2]
    jiguan = data[2:]

    if len(fu) > 0 and (fu[0] == "府" or fu[0] == "縣"):
        fu = fu[1:] + jiguan[0]
        jiguan = jiguan[1:]
    if len(jiguan) > 0 and jiguan[0] == "州":
        fu = fu + "州"
        jiguan = jiguan[1:]
    if len(jiguan) > 0 and jiguan[0] == "府":
        jiguan = jiguan[1:]

    if si == "北直隸":
        if fu == "北平":
            fu = "順天"
    elif si == "南直隸":
        if fu == "盧州":
            fu = "廬州"
        elif fu == "懷安":
            fu = "淮安"
        elif fu == "楊州":
            fu = "揚州"
        elif fu == "寍國":
            fu = "寧國"
    elif si == "陝西":
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
    elif si == "山西":
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
    elif si == "山東":
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
    elif si == "河南":
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
    elif si == "浙江":
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
    elif si == "江西":
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
    elif si == "湖廣":
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
    elif si == "四川":
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
    elif si == "廣東":
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
    elif si == "福建":
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
    elif si == "貴州":
        if fu in ["貴州", "宣慰"]:
            jiguan = fu + jiguan
            fu = "其他"
    elif si == "雲南":
        if fu == "太理":
            fu = "大理"
        elif fu in ["嵩明州", "安寧州"]:
            jiguan = fu + jiguan
            fu = "雲南"
        elif fu in ["□", "霑益州"]:
            jiguan = fu + jiguan
            fu = "其他"
    elif si == "交阯":
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
    elif si == "衛所":
        jiguan = fu + jiguan
        if jiguan[-1] == "衛":
            fu = "衛"
        elif jiguan[-1] == "所":
            fu = "所"
    elif si == "未知":
        jiguan = fu + jiguan
        fu = "未知"

    data_item["府级"] = fu
    data_item.pop("籍貫")


def process_si(data_item):
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

    data_item["司级"] = si
    data_item["籍貫"] = jiguan
    process_fu(data_item)



if __name__ == '__main__':
    file_name = "./Data/mingjinshi_processed.json"
    jsFile = open(file_name, "r", encoding='utf-8')
    data = json.load(jsFile)
    jsFile.close()
    native_data = data["children"]
    for data_item in native_data:
        process_si(data_item)
    processed_data = {"dataset":"mingjinshi", "dataitem": native_data}

    js = json.dumps(processed_data,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
    jsFile = open("./Data/processed_data.json", "w+", encoding='utf-8')
    jsFile.write(js)
    jsFile.close()