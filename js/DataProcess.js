year_dict = [1371, 1400, 1412, 1430, 1433, 1439, 1442, 1445, 1448, 1451, 1454, 1457, 1460, 1464, 1466, 1469, 1472, 1475, 1478, 1481, 1487, 1490, 1493, 1496, 1502, 1505, 1511, 1517, 1521, 1529, 1532, 1535, 1538, 1541, 1544, 1547, 1550, 1553, 1556, 1559, 1562, 1565, 1568, 1571, 1574, 1577, 1580, 1583, 1586, 1610];
census_dict = ["其他", "竈籍", "匠籍", "官籍", "軍籍", "民籍"];
subject_dict = ["詩經", "書經", "禮記", "易經", "春秋", "其他"];
rank_dict = ["未知", "第三甲", "第二甲", "第一甲"];

function processYear (data) {
	processed_data = {
		dataset: "mingjinshi_year",
		dataitem: [],
	}
	for (var i = 0;i < year_dict.length;i++) {
		processed_data.dataitem[i] = {};
		processed_data.dataitem[i]["年份"] = year_dict[i];
		for (var j = 0;j < census_dict.length;j++) {
			processed_data.dataitem[i][census_dict[j]] = 0;
		}
	}
	for (var i = 0;i < data.dataitem.length;i++) {
		if (option.subject) {
			if (data.dataitem[i]["科目"] != option.subject) {
				continue;
			}
		}
		if (option.native_level) {
			if (option.native_level == 1) {
				if (data.dataitem[i]["司级"] != option.native) {
					continue;
				}
			}
			else if (option.native_level == 2) {
				if (data.dataitem[i]["府级"] != option.native) {
					continue;
				}
			}
		}
		for (var j = 0;j < year_dict.length;j++) {
			if (data.dataitem[i]["年份"] == processed_data.dataitem[j]["年份"]) {
				processed_data.dataitem[j][data.dataitem[i]["戶籍"]] += 1;
				continue;
			}
		}
	}
	return processed_data;
}


function processSubject (data) {
	processed_data = {
		dataset: "mingjinshi_subject",
		dataitem: [],
	}
	for (var i = 0;i < subject_dict.length;i++) {
		processed_data.dataitem[i] = {};
		processed_data.dataitem[i]["科目"] = subject_dict[i];
		for (var j = 0;j < rank_dict.length;j++) {
			processed_data.dataitem[i][rank_dict[j]] = 0;
		}
	}
	for (var i = 0;i < data.dataitem.length;i++) {
		if (option.year) {
			if (data.dataitem[i]["年份"] != option.year) {
				continue;
			}
		}
		if (option.census) {
			if (data.dataitem[i]["戶籍"] != option.census) {
				continue;
			}
		}
		if (option.native_level) {
			if (option.native_level == 1) {
				if (data.dataitem[i]["司级"] != option.native) {
					continue;
				}
			}
			else if (option.native_level == 2) {
				if (data.dataitem[i]["府级"] != option.native) {
					continue;
				}
			}
		}
		for (var j = 0;j < subject_dict.length;j++) {
			if (data.dataitem[i]["科目"] == processed_data.dataitem[j]["科目"]) {
				processed_data.dataitem[j][data.dataitem[i]["甲次"]] += 1;
				continue;
			}
		}
	}
	return processed_data;
}