from onjira import onjira_api
import requests
from datetime import date, datetime, timedelta
import calendar


jira_api = onjira_api.JiraApi()
jira = jira_api.login()

#业务线
product_ks = ' BUG模块 in cascadeOption(11644) ) '

#解决部门
team_ks = '(解决部门 ~ 快手)'


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
    return all_bugs


wd = 7
t_day1 = date.today()
f_day1 = (datetime.now() - timedelta(days=wd)).strftime('%Y-%m-%d')


a = create_bugs(f_day=f_day1, l_day=t_day1, product=' BUG模块 in cascadeOption(11672)) ', team=team_ks)
print(a)
print(a[-1])

