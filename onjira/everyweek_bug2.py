# from onjira import onjira_api
import requests
from datetime import date, datetime, timedelta
from test1 import testtoemail
import calendar
import base64
from jira import JIRA
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# from onjira import const


# jira_api = onjira_api.JiraApi()
# jira = jira_api.login()
jira_url = "https://jira.xiaoduoai.com"
email_user_name = "bGlsb25n"
# email_password = "c3VuZGF5MTU1USM="
email_password="WGlhb2R1bzIwMjA="


def send_email_by_qq(to, file_name):
    mailserver = "smtp.163.com"
    sender = "long250938259@163.com"
    reciver = "250938259@qq.com"
    passwd= "DSKYGJIOVIYIKBGC"

    text_info = file_name
    text_sub = MIMEText(text_info, _subtype="plain", _charset="utf-8")

    message = MIMEMultipart("alternative")
    subject = 'python sendemail test successful'
    message['From'] = sender
    message['To'] = to
    message['subject'] = subject
    message.attach(text_sub)

    # txt_file = open(file_name, 'rb').read()
    # txt = MIMEText(txt_file, 'base64', 'utf-8')
    # txt["Content-Type"] = 'application/octet-stream'
    # # 以下代码可以重命名附件为hello_world.txt
    # txt.add_header('Content-Disposition', 'attachment', filename=file_name.split("\\")[-1])
    # message.attach(txt)



    try:
        server = smtplib.SMTP()
        server.connect(mailserver, 25)

        # server.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
        # server.starttls()
        server.login(sender, passwd)
        server.sendmail(sender, reciver, message.as_string())
        server.quit()
        print('sendemail successful!')
    except Exception as e:
        print('sendemail failed next is the reason')
        print(e)



class JiraApi(object):
    global jira_url


    def encryption(self, st):
        encode = base64.b64encode(st.encode('utf-8'))
        return str(encode, 'utf-8')

    def decrypt(self, st):
        decode = base64.b64decode(st)
        return str(decode, 'utf-8')

    def login(self):
        user_name = self.decrypt(email_user_name)
        password = self.decrypt(email_password)
        jirap = JIRA(basic_auth=(user_name, password), options={
            'server': jira_url})
        return jirap



jira_api = JiraApi()
jira = jira_api.login()
"""
每周线上bug情况数据（需要jenkins建立任务）
1.添加对应BUG模块：product字段(BUG模块，暂定按BUG模块来处理)，如product_cxxl，需要和jira对应
2.添加对应解决部门：如teams_cxxl，需要和jira对应
3.添加飞书机器人地址：如feishu_url_cxxl，获取机器人的webhook地址
4.将developer、feishu_url追加到group_list，以列表的形式
"""

# 1.业务线
product_cxxl = ' BUG模块 in cascadeOption(11666) OR BUG模块 in cascadeOption(11721) ' \
       'OR BUG模块 in cascadeOption(11667) OR  BUG模块 in cascadeOption(11668) OR BUG模块 ' \
       'in cascadeOption(11669) OR BUG模块 in cascadeOption(11671) OR BUG模块 in cascadeOption(11738)' \
       ' OR BUG模块 in cascadeOption(11740) OR BUG模块 in cascadeOption(11741)) '
# 知更后台、千牛运营后台、订购和授权、设置、违禁词监控、物流&售后、问答-问答知识库（有京东组、售后组、增值场景组）、问答-未识别问题
product_kxx = ' BUG模块 in cascadeOption(11738) OR BUG模块 in cascadeOption(11741)) '  # 客晓晓（企微）、CVD
product_kb = ' BUG模块 in cascadeOption(11666)) '  # 客户维护（知客、客伴等）
product_tn = ' BUG模块 in cascadeOption(11671) OR BUG模块 in cascadeOption(11669) OR ' \
             'BUG模块 in cascadeOption(11667) OR BUG模块 in cascadeOption(11668)) '  # 目标管理、明察智能质检、买家之声、金牌话术
product_sxx = ''
product_jd = ' (店铺平台 = 京东) )'
product_ks = ' (店铺平台 = 快手) ) '
product_reminder = ' BUG模块 in cascadeOption(11664)) '  # 智能跟单
product_sh = ' BUG模块 in cascadeOption(11739) OR BUG模块 in cascadeOption(11740)) '  # 工单系统、王牌教练
product_client = ' BUG模块 in cascadeOption(11672)) '  # 客户端
"""
-- 增值场景：问答知识库-自定义问题，精准意图，属性问答，问答知识库-搜索
增值场景组：
BUG模块：
问答-自定义问题
问答-精准意图
问答-属性问答
商品知识库-尺码表
推荐导购-商品推荐
推荐导购-求购推荐
售后场景-发货物流
设置-转接设置
"""
product_values = ' BUG模块 in cascadeOption(11644, 11657) OR BUG模块 in cascadeOption(11644, 11659) OR ' \
                 'BUG模块 in cascadeOption(11662, 11679) OR BUG模块 in cascadeOption(11663) OR ' \
                 'BUG模块 in cascadeOption(11743, 11744) OR BUG模块 in cascadeOption(11646, 11698) OR ' \
                 'BUG模块 in cascadeOption(11644, 11912) OR BUG模块 in cascadeOption(11644, 11913)) '
"""
-- 核心应答：问答知识库-测试机器人，自动学习，活动管理，未识别问题
核心应答组：
BUG模块：
数据统计
问答-自动学习
问答-活动管理
商品知识库-商品列表
商品知识库-商品分类
商品知识库-商品对比
配置诊断
雪球系统 - jira没有对应BUG模块
"""
product_answer = ' BUG模块 in cascadeOption(11642) OR BUG模块 in cascadeOption(11644, 11661) OR ' \
                 'BUG模块 in cascadeOption(11644, 11660) OR BUG模块 in cascadeOption(11662, 11676) OR ' \
                 'BUG模块 in cascadeOption(11662, 11677) OR BUG模块 in cascadeOption(11662, 11678) OR ' \
                 'BUG模块 in cascadeOption(11670) OR BUG模块 in cascadeOption(11644, 11645) OR ' \
                 'BUG模块 in cascadeOption(11644, 11914) OR BUG模块 in cascadeOption(11644, 11658)) '
# 2.解决部门
teams_cxxl = '(解决部门 ~ XCRM OR 解决部门 ~ BI OR 解决部门 ~ 客晓晓 OR ' \
        '解决部门 ~ CVD OR 解决部门 ~ 客服提能组 OR 解决部门 ~ XDATA)'
team_kxx = '(解决部门 ~ CVD OR 解决部门 ~ 客晓晓)'
team_kb = '(解决部门 ~ XCRM)'
team_tn = '(解决部门 ~ 客服提能组)'
team_sxx = '解决部门 ~ XDATA'
team_jd = '(解决部门 ~ 京东组)'
team_ks = '(解决部门 ~ 快手组)'
team_reminder = '(解决部门 ~ 跟单组)'
team_sh = '(解决部门 ~ 售后组)'
team_client = '(解决部门 ~ 客户端)'
team_values = '(解决部门 ~ 增值场景组)'
team_answer = '(解决部门 ~ 核心应答组)'

# 3.飞书机器人webhook地址（先建群，再添加机器人，在获取机器人的webhook地址）
feishu_url_ks1 = 'https://open.feishu.cn/open-apis/bot/v2/hook/2c593c2f-bf67-4e92-bd64-443feb024ea4'
feishu_url_cxxl = 'https://open.feishu.cn/open-apis/bot/v2/hook/55ad2004-db5f-44f4-8b6c-1c2ccda53186'
feishu_url_kxx = 'https://open.feishu.cn/open-apis/bot/v2/hook/ab7a1d68-9172-49bb-8981-bb79760794bf'
feishu_url_kb = 'https://open.feishu.cn/open-apis/bot/v2/hook/13ac21a4-d883-4e51-b3ff-71f8da0884c6'
feishu_url_tn = 'https://open.feishu.cn/open-apis/bot/v2/hook/657cea6b-1fc1-4d45-921c-7ed310b2dede'
feishu_url_sxx = ''
feishu_url_jd = 'https://open.feishu.cn/open-apis/bot/v2/hook/b3312539-55ec-4b45-8cb4-201057a4e61e'
feishu_url_ks = 'https://open.feishu.cn/open-apis/bot/v2/hook/55010761-fc94-4bc8-a5c2-3dcedcab074c'
feishu_url_reminder = 'https://open.feishu.cn/open-apis/bot/v2/hook/d3da0f6e-ff96-4adb-b9d1-6245ae200284'
feishu_url_sh = 'https://open.feishu.cn/open-apis/bot/v2/hook/511111aa-d71b-4093-8bdd-5aef2053d8ca'
feishu_url_client = 'https://open.feishu.cn/open-apis/bot/v2/hook/27ecef2d-528e-4a62-94ed-3d0abcba1f8a'
feishu_url_values = 'https://open.feishu.cn/open-apis/bot/v2/hook/e9929284-3c7d-40fa-93a3-5f8264e78157'
feishu_url_answer = 'https://open.feishu.cn/open-apis/bot/v2/hook/bb805faa-1b1d-40d2-b407-b03d63fcb314'

group_list = [
              [product_kxx, team_kxx, feishu_url_kxx],
              [product_kb, team_kb, feishu_url_kb],
              [product_tn, team_tn, feishu_url_tn],
              [product_reminder, team_reminder, feishu_url_reminder],
              # [product_sh, team_sh, feishu_url_sh],
              [product_client, team_client, feishu_url_client],
              [product_values, team_values, feishu_url_values],
              [product_answer, team_answer, feishu_url_answer],
              [product_ks, team_ks, feishu_url_ks1],
              [product_jd, team_jd, feishu_url_ks1]
              ]


# 组装jql，可以自己获取jql填入
def jql_deal(forward_day, today_day, product, teams):
    jql_create_bugs = 'project = BUG AND ( ' + product + ' AND created >= ' + str(forward_day) + \
          ' AND created <= ' + str(today_day) + ' ORDER BY created DESC'
    jql_repair_bugs = 'project = BUG AND ' + teams + ' AND created >= ' + str(forward_day) + \
        ' AND created <= ' + str(today_day) + ' ORDER BY cf[10468] DESC, resolved DESC, cf[10441] ASC, created DESC'
    print(jql_create_bugs)
    print(jql_repair_bugs)
    return jql_create_bugs, jql_repair_bugs

# jira登录返回jira对象，进行数据获取


# jira_api = jira_api.JiraApi()
# jira = jira_api.login()


class EveryWeek:
    def __init__(self, f_day, l_day, product, team):
        self.f_day = f_day
        self.l_day = l_day
        self.product = product
        self.team = team

    def create_bugs(self, f_day, l_day):
        all_bugs = jira.search_issues(jql_deal(f_day, l_day, self.product, self.team)[0],
                                      fields='', maxResults=1000)  # 获取所有bug
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
            result_support = str(issue.fields.customfield_10442)  # 排查结果-技术支持
            if result_support:
                if result_support_list.get(result_support):
                    result_support_list[result_support] += 1
                else:
                    result_support_list[result_support] = 1
            result_onlingbug = str(issue.fields.customfield_10441)  # 排查结果-线上缺陷
            if len(assignee) == 2:  # 样式优化
                assignee = assignee[0] + "   " + assignee[1]
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

    def repair_bugs(self):
        all_bugs = jira.search_issues(jql_deal(self.f_day, self.l_day, self.product, self.team)[1],
                                      fields='', maxResults=1000)  # 获取所有bug
        text = ''
        for issue in all_bugs:
            assignee = str(issue.fields.assignee)  # 经办人
            if len(assignee) == 2:  # 样式优化
                assignee = assignee[0] + "   " + assignee[1]
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
        return str(len(all_bugs)), text

    def valid_bugs(self):
        all_bugs = jira.search_issues(jql_deal(self.f_day, self.l_day, self.product, self.team)[0],
                                      fields='', maxResults=1000)  # 获取所有bug
        text = ''
        num = 0
        for issue in all_bugs:
            if issue.fields.customfield_10441 or (str(issue.fields.status) in ['待研发修复', '研发修复中']):
                # issue.fields.customfield_10441  # 处理结果-线上缺陷
                # issue.fields.customfield_10422  # 修复人
                num += 1
                assignee = str(issue.fields.assignee)  # 经办人
                if len(assignee) == 2:  # 样式优化
                    assignee = assignee[0] + "   " + assignee[1]
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
        return str(num), text

    def need_deal_bugs(self):
        pass

    def bugs_data_deal_week(self):
        """
        bug数据处理
        :return:
        """
        all_bugs = jira.search_issues('', fields='', maxResults=1000)  # 获取所有bug
        text = ''
        for issue in all_bugs:
            assignee = str(issue.fields.assignee)  # 经办人
            if len(assignee) == 2:  # 样式优化
                assignee = assignee[0] + "   " + assignee[1]
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
        return text

    def send_to_feishu_developer(self, text, feishu_url):
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

    def send_rich_text(self, title, text, feishu_url):
        headers = {'Content-Type': 'application/json'}
        data = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": title,
                        "content": [
                            [
                                {
                                    "tag": "text",
                                    "text": text
                                }
                            ]
                        ]
                    }
                }
            }
        }
        res = requests.post(feishu_url, json=data, headers=headers)
        if res.status_code == 200:
            return True
        else:
            return False

    def bug_type_deal(self, da):
        res = {}
        for i in da:
            if i in ['不是bug-客成排查不足（知识库中已有排查方法）', '不是BUG-客户原因-使用/配置问题']:
                if res.get('客成排查不足、客户使用问题'):
                    res['客成排查不足、客户使用问题'] += da[i]
                else:
                    res['客成排查不足、客户使用问题'] = da[i]
            elif i in ['不是BUG-用户体验-隐藏逻辑', '不是bug-超出客成排查范围（产品固有逻辑）',\
                       '不是bug-超出客成排查范围（知识库中没有排查方法）', '不是BUG-前置条件限制-可优化']:
                if res.get('产品可解释性问题、缺乏排查手段'):
                    res['产品可解释性问题、缺乏排查手段'] += da[i]
                else:
                    res['产品可解释性问题、缺乏排查手段'] = da[i]
            elif i in ['不是BUG-客户原因-网络异常', '不是bug-产品隐藏逻辑（需要研发查代码排查）']:
                if res.get('需研发排查定位'):
                    res['需研发排查定位'] += da[i]
                else:
                    res['需研发排查定位'] = da[i]
            elif i in ['是BUG-内部原因-服务异常', '是BUG-有临时解决方案', '是bug-创建工单时已修复', '是BUG-客户端高版本已修复',\
                    '是bug-工单重复', '不是BUG-内部原因-产研沟通']:
                if res.get('是BUG'):
                    res['是BUG'] += da[i]
                else:
                    res['是BUG'] = da[i]
            elif i in ['不是BUG-外部原因-平台特性', '不是BUG-外部原因-平台BUG', '不是bug-外部原因（外部不可控因素导致）']:
                if res.get('外部不可控因素'):
                    res['外部不可控因素'] += da[i]
                else:
                    res['外部不可控因素'] = da[i]
            elif i in ['不是BUG-客户原因-信息不全', '无法定位/复现', '无法定位-日志超期', '无法定位-日志缺失']:
                if res.get('未定位'):
                    res['未定位'] += da[i]
                else:
                    res['未定位'] = da[i]
        res_da = sorted(res.items(), key=lambda x: x[1], reverse=True)
        res_text = ''
        for i in res_da:
            a = str(i[0]) + " :" + str(i[1]) + " \n"
            res_text += a
        return res_text

    def text_deal(self, num):
        wk_bu = self.create_bugs(self.f_day, self.l_day)
        wk_bugs = wk_bu[0]
        cri_bugs = wk_bu[3]
        criti_text = ''
        if cri_bugs:
            criti_text = '线上严重问题：\n' + cri_bugs
        text = '\n----------------------------\n本周概况(统计上周五至本周四)\n' + criti_text + '本周新增bug：' + wk_bugs \
               + '\n' + '本周修复bug：' + self.repair_bugs()[0] + '\n'
        # ew.send_rich_text('上周线上bug情况', text, jqr_url)
        text += '----------------------------\n' + '近5周新增趋势\n'
        # print(text)
        text_a = ''
        bugs_sum = 0
        for i in range(5):
            f_day = (datetime.now() - timedelta(days=num * (i + 1))).strftime('%Y-%m-%d')
            s_day = (datetime.now() - timedelta(days=num * (i + 2))).strftime('%Y-%m-%d')
            tt = self.create_bugs(s_day, f_day)[0]
            bugs_sum += int(tt)
            text_a += s_day + "-" + f_day + ": 新增" + tt + '\n'
        text_a += '近5周平均值：' + format(float(bugs_sum) / float(5), '.2f')
        avg = float(bugs_sum) / float(5)
        diff_va = float(wk_bugs) - avg
        ta = self.values_status(diff_va / avg)
        text_c = ta[1]
        text_b = ('\n----------------------------\n本周质量情况星级评估: {0}\n').format(ta[0])  # + '\n近5周平均值：' + format(float(bugs_sum) / float(5), '.2f')
        # print(text + text_a + text_b + text_c)
        text_e = '\n----------------------------\n本周BUG分类\n'
        text_e += self.bug_type_deal(wk_bu[4])
        return text_b + text_c + text + text_a + text_e

    def values_status(self, va):
        text = ''
        if va < -0.4:
            text = '★'*5, ('BUG总数降低: ' + format(abs(va), '.2%') + '\n本周质量情况优秀，是优秀的小伙伴们努力的结果，下周继续保持哦~')
        elif -0.4 <= va < -0.2:
            text = '★'*4, ('BUG总数降低: ' + format(abs(va), '.2%') + '\n本周质量情况良好，是优秀的小伙伴们努力的结果，继续加油哦~')
        elif -0.2 <= va < 0:
            text = '★'*3, ('BUG总数降低: ' + format(abs(va), '.2%') + '\n本周质量情况有一定提升，不过仍有很大的提升空间，继续加油哦~')
        elif 0 <= va < 0.2:
            text = '★'*2, ('BUG总数增加: ' + format(abs(va), '.2%') + '\n本周质量情况不佳，我们一起来找找改进机会吧~')
        elif 0.2 <= va < 0.4:
            text = '★', ('BUG总数增加: ' + format(abs(va), '.2%') + '\n本周质量情况不理想，但意味着改进机会也很多，我们一起来找找吧！')
        elif va >= 0.4:
            text = '', ('BUG总数增加: ' + format(abs(va), '.2%') + '\n本周工单有大幅增加，请尽快分析原因！！！')
        return text


if __name__ == '__main__':
    # 向对应分飞书群发送消息
    # send_to_feishu_developer(bugs_data_deal(), jqr_url)
    wd = 7  # 维度，单位天
    currentdate = date.today()
    year = currentdate.year
    month = currentdate.month
    day = currentdate.day
    currentday = calendar.weekday(year, month, day)
    t_day1 = date.today()
    f_day1 = (datetime.now() - timedelta(days=wd)).strftime('%Y-%m-%d')
    # if currentday == 4:
    #     for group in group_list:
    #         ew = EveryWeek(f_day1, t_day1, group[0], group[1])
    #         print(group[1])
    #         print(ew.text_deal(wd))
    #         # ew.send_to_feishu_developer(ew.text_deal(wd), group[2])

    ew = EveryWeek(f_day1, t_day1, group_list[7][0], group_list[7][1])
    print(group_list[7][2])
    print(ew.text_deal(wd))
    # ew.send_to_feishu_developer(ew.text_deal(wd), group_list[7][2])  # 快手
    to = '250938259@qq.com'
    testtoemail.send_email_by_qq(to, ew.text_deal(wd))

    # ew = EveryWeek(f_day1, t_day1, group_list[8][0], group_list[8][1])
    # print(group_list[8][2])
    # print(ew.text_deal(wd))
    # ew.send_to_feishu_developer(ew.text_deal(wd), group_list[8][2])  # 京东
    # email = testtoemail.send_email_by_qq(ew.text_deal(wd))



