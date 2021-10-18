from onjira import onjira_api
import requests
from datetime import date, datetime, timedelta
import calendar


jira_api = onjira_api.JiraApi()
jira = jira_api.login()

#业务线
product_ks = ' (店铺平台 = 快手) ) '
product_jd = '(店铺平台 = 京东))'

#解决部门
team_ks = '(解决部门 ~ 快手)'
team_jd = '(解决部门 ~ 京东)'

# 3.飞书机器人webhook地址（先建群，再添加机器人，在获取机器人的webhook地址）
feishu_url_cxxl = 'https://open.feishu.cn/open-apis/bot/v2/hook/2c593c2f-bf67-4e92-bd64-443feb024ea4'


def jql_deal(forward_day, today_day, product, teams):
    jql_create_bugs = 'project = BUG AND ( ' + product + ' AND created >= ' + str(forward_day) + \
          ' AND created <= ' + str(today_day) + ' ORDER BY created DESC'
    jql_repair_bugs = 'project = BUG AND ' + teams + ' AND created >= ' + str(forward_day) + \
        ' AND created <= ' + str(today_day) + ' ORDER BY cf[10468] DESC, resolved DESC, cf[10441] ASC, created DESC'
    print(jql_create_bugs)
    print(jql_repair_bugs)
    return jql_create_bugs, jql_repair_bugs


def create_bugs(f_day, l_day, product, team):
    all_bugs = jira.search_issues(jql_deal(f_day, l_day, product, team)[0],
                                  fields='', maxResults=1000)  # 获取所有bug
    print(all_bugs)
    # return all_bugs
    text = ''
    criti_bugs = ''
    L0 = 0
    L1 = 0
    L2 = 0
    L3 = 0
    result_support_list = {}
    result_onlingbug_list = {}
    for issue in all_bugs:
        assignee = str(issue.fields.assignee)  # 经办人
        result_support = str(issue.fields.customfield_10442)
        print(result_support)# 排查结果-技术支持
        if result_support:
            if result_support_list.get(result_support):
                result_support_list[result_support] += 1
            else:
                result_support_list[result_support] = 1
        result_onlingbug = str(issue.fields.customfield_10441)  # 排查结果-线上缺陷
        if len(assignee) == 2:  # 样式优化
            assignee = assignee[0] + " " + assignee[1]

        # print(assignee)
        # reporter = str(issue.fields.reporter)
        # if len(reporter) == 2:
        #     reporter = reporter[0] + "   " + reporter[1]
        level = str(issue.fields.customfield_10440)  # bug等级
        if level == 'None':
            level = "L2"
        status = str(issue.fields.status)  # 状态
        summary = issue.fields.summary  # bug标题
        if len(summary) > 20:
            summary = summary[:24] + "..."
        bug = str(issue) + " " + level + "-" + str(assignee) + "-" + status + "-" + summary
        text += bug + "\n"
        creatime = "创建时间：" + str(issue.fields.created[:10])
        text = text + creatime + "\n"
        if level == 'L0':
            L0 += 1
            criti_bugs += bug + "\n"
        elif level == 'L1':
            L1 += 1
            criti_bugs += bug + "\n"
        elif level == 'L2':
            L2 += 1
        elif level == 'L3':
            L3 += 1
        else:
            L2 += 1
    return str(len(all_bugs)), text, (L0, L1, L2, L3), criti_bugs, result_support_list


def send_to_feishu_developer(text, feishu_url):
    """
    发送飞书消息
    :param text:
    :param feishu_url:
    :return:
    """
    headers = {'Content-Type': 'application/json'}
    data = {"msg_type": "text", "content": {"text": text}}
    res = requests.post(feishu_url, json=data, headers=headers)
    if res.status_code == 200:
        return True
    else:
        return False





wd = 7
t_day1 = date.today()
# print(t_day1)
f_day1 = (datetime.now() - timedelta(days=wd)).strftime('%Y-%m-%d')
# print(f_day1)


a = create_bugs(f_day=f_day1, l_day=t_day1, product=product_jd, team=team_jd)
print(a)


# send_to_feishu_developer(a[1], feishu_url_cxxl)


