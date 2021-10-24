# import requests
# import pprint
# import json
#
# data = {
#     "requestId": "303fe1ca-9d76-45e3-ac3e-41f6aa35a994",
#     "createTime": 0,
#     "generator": 1,
#     "type": 1,
#     "fromUser": {
#         "nickName": "在于自己",
#         "role": 1,
#         "openId": "Vb2oGFTksn5jWZZQiM8zqEl7Ox3pValH3Jw878iDQab"
#     },
#     "toUser": {
#         "nickName": "我是卖家呀呀呀呀呀！！！！！",
#         "role": 2
#     },
#     # "transferList": None,
#     "context": {
#         "sellerId": 1901625824,
#         "itemId": 0,
#         "orderId": 0,
#         "orderStatus": 0,
#         "assistantOnlineStatus": 0
#     },
#     "message": {
#         "contentType": 1,
#         "content": "{\"text\":\"我考虑一下\"}"
#     }
# }
#
# url = "https://wangcai-test-ks.xiaoduoai.com/spi/chatbotevent"
#
# res = requests
# res1 = res.post(url=url, json=data )
# print(res1)
#
import xlrd


data = xlrd.open_workbook("D:/新建文件夹/tbp-tst/testdata/sizechart_test.xlsx")
table = data.sheets()[0]
test_data = []
print(table.nrows)

for i in range(1, table.nrows):
    # 对应excel表格的类目
    category_name = table.row_values(i)[0]
    # print(category_name)
    # 对应excel表格的尺码表类型
    sizechart = table.row_values(i)[1]
    # print(sizechart)
    # 对应excel表格的用例标题
    case_name = table.row_values(i)[2]
    # print(case_name)
    # 对应excel表格的咨询问题
    answer = table.row_values(i)[4]
    answer_list = [answer]
    # print(answer)
    # print(answer_list)
    # 对应excel表格的预期回复结果
    expect = table.row_values(i)[5]
    expect_list = [expect]
    # print(expect)
    # print(expect_list)

    data = [category_name, sizechart, case_name, answer_list, expect_list]
    test_data.append(data)
    # print(test_data)

# 清洗数据格式，需要把数据组装成下列格式
# ["类目标题", "尺码表类型", ["咨询问题1", "咨询问题2", "咨询问题3"],["预期回复结果1", "预期回复结果2","预期回复结果3"]]
# 第一步清洗：将合并的单元格中为空的值进行补充
for i in range(0, len(test_data)):

    category_name = test_data[i][0]
    sizechart_name = test_data[i][1]
    case_name = test_data[i][2]

    if category_name == "":

        test_data[i][0] = test_data[i - 1][0]
        # print(test_data)

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


            b = test_data[i + 1][3] = test_data[i][3]
            print(b)
            test_data[i][4].extend(test_data[i + 1][4])
            test_data[i + 1][4] = test_data[i][4]

            test_data[i] = "0000000"
            print(i)
            print(test_data[i])

while "" in test_data:
    test_data.remove("")


print(test_data)
print(len(test_data))













