import xlrd
import json


def read_xlsx_file(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)
    rows = table.nrows
    data = []
    title = table.row_values(0, start_colx=1, end_colx=12)
    for i in range(1, rows):
        values = table.row_values(i, start_colx=1, end_colx=12)
        data.append(
            (
                {
                    title[2][2:]: int(values[2]),
                    title[3]: values[3],
                    title[6]: values[6],
                    title[7]: values[7],
                    title[8]: values[8], 
                    title[9]: values[9],
                    title[10]: values[10], 
                }
            )
        )
    return data

if __name__ == '__main__':
    file_name = "./Data/ming_jinshilu_52y_release.xlsx"
    data = read_xlsx_file(file_name)
    data = {"name":"mingjinshi", "children": data}
    js = json.dumps(data,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
    jsFile = open("./Data/ming_jinshilu_52y_release.json", "w+", encoding='utf-8')
    jsFile.write(js)
    jsFile.close()