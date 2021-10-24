import xlrd


def getAllData(self, excel_file_path):
    '''
   获取excel文件数据
   :return:
   '''
    data = xlrd.open_workbook(excel_file_path)
    table = data.sheets()[0]
    test_data = []

    for i in range(1, table.nrows):
        # 对应excel表格的类目
        category_name = table.row_values(i)[0]
        # 对应excel表格的尺码表类型
        sizechart = table.row_values(i)[1]
        # 对应excel表格的用例标题
        case_name = table.row_values(i)[2]
        # 对应excel表格的咨询问题
        answer = table.row_values(i)[4]
        answer_list = [answer]
        # 对应excel表格的预期回复结果
        expect = table.row_values(i)[5]
        expect_list = [expect]

        data = [category_name, sizechart, case_name, answer_list, expect_list]
        test_data.append(data)

    # 清洗数据格式，需要把数据组装成下列格式
    # ["类目标题", "尺码表类型", ["咨询问题1", "咨询问题2", "咨询问题3"],["预期回复结果1", "预期回复结果2","预期回复结果3"]]
    # 第一步清洗：将合并的单元格中为空的值进行补充
    for i in range(0, len(test_data)):

        category_name = test_data[i][0]
        sizechart_name = test_data[i][1]
        case_name = test_data[i][2]

        if category_name == "":

            test_data[i][0] = test_data[i - 1][0]

            if sizechart_name == "":

                test_data[i][1] = test_data[i - 1][1]

                if case_name == "":
                    test_data[i][2] = test_data[i - 1][2]

    # 第二步清洗：将每一行的答案和预期结果组装成答案列表和预期回复列表
    for i in range(0, len(test_data)):

        if i < len(test_data) - 1:

            if test_data[i][0] == test_data[i + 1][0] and test_data[i][1] == test_data[i + 1][1] and test_data[i][2] == \
                    test_data[i + 1][2]:
                test_data[i][3].extend(test_data[i + 1][3])
                test_data[i + 1][3] = test_data[i][3]
                test_data[i][4].extend(test_data[i + 1][4])
                test_data[i + 1][4] = test_data[i][4]

                test_data[i] = ""

    while "" in test_data:
        test_data.remove("")

    return test_data