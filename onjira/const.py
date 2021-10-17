# @Time : 2020/08/23 16:52
# @Author : "杨伟伟"

jira_url = "https://jira.xiaoduoai.com"
test_plan_url = "https://tester.xiaoduoai.com/api/v1/functioncase/casePlanList"
test_plan_url_day_range = "https://tester.xiaoduoai.com/api/v1/functioncase/casePlanList?currentPage=1&pageSize=10&pageTotal=0&pageCurrent=1&name=&plan_tester=&created_time=2021-06-01,2021-12-17&user="
test_plan_info = 'https://tester.xiaoduoai.com/#/Function/CasePlanInfo?id='
plan_info_url = "https://tester.xiaoduoai.com/api/v1/functioncase/planInfo"
plan_detail="https://tester.xiaoduoai.com/api/v1/functioncase/newRunList?case_plan_id={}&case_name=&tester=&currentPage=1&pageSize=100&count=0"
test_case_url = "https://tester.xiaoduoai.com/api/v1/functioncase/caseAutoList"
test_case_url_new = "https://tester.xiaoduoai.com/api/v1/functioncase/caseList?user={}&created_time={},{}"
test_case_url_deleted="https://tester.xiaoduoai.com/api/v1/functioncase/caseList?case_path=966&user={}&created_time={},{}"
email_user_name = "bGlsb25n"
# email_password = "c3VuZGF5MTU1USM="
email_password="WGlhb2R1bzIwMjA="

jql_created_bugs_all = "issuetype = 缺陷 AND creator in ({}) AND created >= {} AND created <= {}   ORDER BY updated DESC"
# 测试组创建的bug--按创建时间算
jql_created_bugs_not_valid = "issuetype = 缺陷 AND creator in ({}) AND created >= {} AND created <= {}  AND 处理结果-线下缺陷 in ('不是bug-产品原有/隐藏逻辑', 不是bug-外部不可控因素导致, 不是bug-测试人员操作问题误报, 不是bug-需UI优化, 不是bug-需产品优化, 无法重现, 是bug-工单重复) ORDER BY updated DESC"

# 体验改进组负责的线上bug
jql_online_bugs = 'project = BUG AND 技术负责组 ~ {} AND resolved >= {} AND resolved <= {}  AND 处理结果-线上缺陷 in (产品设计缺陷, 历史遗留缺陷, 外部不可控因素导致, 技术实现缺陷, 技术设计缺陷, 运维故障)  ORDER BY updated DESC'
# jql_online_bugs = 'project = 线上BUG反馈 AND resolved >= {} AND resolved <= {}'
jql_online_bugs_created = 'project = 线上BUG反馈 AND created >= {} AND created <= {}'
jql_online_bugs_tmp = 'project = BUG  AND resolved >= 2021-08-01 AND resolved <= 2021-09-01  AND 处理结果-线上缺陷 in (产品设计缺陷, 历史遗留缺陷, 外部不可控因素导致, 技术实现缺陷, 技术设计缺陷, 运维故障)  ORDER BY updated DESC'
# 体验改进组负责的线上bug且是客户提交的
jql_online_bugs_tester = 'project = BUG AND creator not in (membersOf(test))  AND 技术负责组 ~ {} AND resolved >= {} AND resolved <= {}  AND 处理结果-线上缺陷 in (产品设计缺陷, 历史遗留缺陷, 外部不可控因素导致, 技术实现缺陷, 技术设计缺陷, 运维故障)  ORDER BY updated DESC'


#整个测试部的线上bug
jql_online_bugs_all='project = BUG AND resolved >= {} AND resolved <= {}  AND 处理结果-线上缺陷 in (产品设计缺陷, 历史遗留缺陷, 外部不可控因素导致, 技术实现缺陷, 技术设计缺陷, 运维故障)  ORDER BY updated DESC'
# 线上非测试提交的bug
# jql_online_bugs_tester="project = BUG AND creator not in (membersOf(test))  AND resolved >= {} AND resolved <= {}  AND 处理结果-线上缺陷 in (产品设计缺陷, 历史遗留缺陷, 外部不可控因素导致, 技术实现缺陷, 技术设计缺陷, 运维故障)  ORDER BY updated DESC"
# 体验改进测试组的任务过滤器
tiyan_tag_ongoing = '进行中的测试任务'
parent_task = "issueKey="

tiyan_jql_ongoing_task_personal = 'project != QS  AND issuetype = 子任务 AND status = 进行中 AND resolution = Unresolved AND assignee in ({}) ORDER BY priority DESC, updated DESC'
tiyan_jql_not_start_task_personal = 'project != QS AND issuetype = 子任务 AND status = 未开始 AND resolution = Unresolved AND assignee in ({}) ORDER BY priority DESC, updated DESC'

# tiyan_Q4_task_jql = 'project != QS AND issuetype = 子任务 AND resolved >= 2020-12-06 AND resolved <= 2020-12-31 AND assignee in (yangjiashi, liulei01, shenchuan, currentUser(), liujinyang) order by updated DESC'
demands_jql='project != QS  AND issuetype = 需求 AND resolved >= {} AND resolved <= {} order by updated DESC'
#  'issuetype in subTaskIssueTypes() AND  resolution = 已完成  AND  resolved >= -30d AND resolved <= "1" AND assignee in (yangjiashi, shenchuan, wangjianqiang) ORDER BY assignee'

# 邮箱
tiyan_tolist = ['yangjiashi@xiaoduotech.com', 'yangweiwei@xiaoduotech.com', 'shenchuan@xiaoduotech.com', 'liulei01@xiaoduotech.com', 'liujinyang@xiaoduotech.com', 'lizhipeng@xiaoduotech.com', 'liujiayong@xiaoduotech.com', 'liuyunfeng@xiaoduotech.com', 'linhaili@xiaoduotech.com', 'fengliang@xiaoduotech.com', 'wuhan@xiaoduotech.com',
                'dushanshan@xiaoduotech.com', 'liuxin@xiaoduotech.com', 'mapingchuan@xiaoduotech.com', 'xiaochi@xiaoduotech.com', 'wenwen@xiaoduotech.com', 'xionglei@xiaoduotech.com', 'wangbinhan@xiaoduotech.com', 'xiaolin@xiaoduotech.com', 'zhuhonghui@xiaoduotech.com', 'chenjiewen@xiaoduotech.com', 'zengqiang@xiaoduotech.com', 'ranyixin@xiaoduotech.com']
t = ['yangweiwei@xiaoduotech.com']
to_mail_list = {
    "tiyan": tiyan_tolist
}

bug_fuzezu_tiyan = ["会话改进组", "开发组", "算法组","增值场景组","核心应答组","开发组"]
bug_fuzezu_zhineng = ["配置中台组", "渠道支撑组", "CDE对接部","客户端一组","京东组","快手组","售后组","客户端组"] #客户端组
bug_fuzezu_xiaolv = ["客服提能组", "客户运营组", "客伴技术组","创新业务部" ,"智能跟单组","跟单组","客伴组","明察组","客晓晓","XDATA","XCRM","CVD组"]


# 体验改进组的测试和研发
tiyan_tester_chinese = ["申川",  "刘金洋", "刘磊", "杨伟伟","范凯林"]
zhineng_tester_chinese = ["张沛", "李东", "黄怡然", "李龙","张怀宇", "李超超", "张明柱"]
chuangxin_tester_chinese = ["何相玄", "白佳鑫", "李九龙","王健强", "谢鹏"]



# 体验改进组测试
tiyan_tester_eng = ["fankailin", "shenchuan", "liulei01", "liujinyang"]
zhineng_tester_eng=["zhangpei","lidong","huangyiran","lilong01","zhanghuaiyu","lichaochao01","zhangmingzhu"]
chuangxin_tester_eng=["hexiangxuan","baijiaxin","lijiulong","wangjianqiang","xiepeng"]



# 测试部全体测试
all_tester_eng = ["yangweiwei", "shenchuan", "yangjiashi", "liulei01", "liujinyang",
                     "zhangpei", "fankailin", "huangyiran", "lidong01", "lidong", "lijian", "lilong",
                     "zhanghuaiyu", "lichaochao01", "liulei", "zhangmingzhu",
                     "hexiangxuan", "leishiqi", "lijiulong", "yuechun",
                     "wangjianqiang", "xiepeng","wangsong","lizhipeng","wangqiang"]

all_testers = ["申川", "杨佳石",  "杨伟伟", "刘金洋", "刘磊",  "张沛", "李龙", "李超超", "李九龙", "张怀宇", "李东",
                "谢鹏", "雷仕锜", "范凯林",  "白佳鑫", "黄怡然", "王健强", "何相玄", "张明柱", "刘金洋", "岳纯", "刘磊","王强"]


fuzezu_data={
    "tiyan":{"bug_fuzezu":bug_fuzezu_tiyan,"tester_chinese":tiyan_tester_chinese,"tester_eng":tiyan_tester_eng},
    "zhineng":{"bug_fuzezu":bug_fuzezu_zhineng,"tester_chinese":zhineng_tester_chinese,"tester_eng":zhineng_tester_eng},
    "chuangxin":{"bug_fuzezu":bug_fuzezu_xiaolv,"tester_chinese":chuangxin_tester_chinese,"tester_eng":chuangxin_tester_eng}
}
#无效bug分类

invalid_categary = ['BUG','客成排查不足、客户使用问题','需研发排查定位','外部不可控因素','产品可解释性问题、缺乏排查手段','未定位','未明确分类']

invalid_issue_bug = ['是BUG-内部原因-服务异常','是BUG-有临时解决方案','是bug-创建工单时已修复','是BUG-客户端高版本已修复','是bug-工单重复','不是BUG-内部原因-产研沟通']
invalid_issue_outcontrol = ['不是BUG-外部原因-平台特性','不是BUG-外部原因-平台BUG','不是bug-外部原因（外部不可控因素导致）']
invalid_issue_product = ['不是BUG-用户体验-隐藏逻辑','不是bug-超出客成排查范围（产品固有逻辑）','不是bug-超出客成排查范围（知识库中没有排查方法）','不是BUG-前置条件限制-可优化']
invalid_issue_kecheng = ['不是bug-客成排查不足（知识库中已有排查方法）','不是BUG-客户原因-使用/配置问题']
invalid_issue_dev_analysis = ['不是BUG-客户原因-网络异常','不是bug-产品隐藏逻辑（需要研发查代码排查）']
invalid_issue_untargeted = ['不是BUG-客户原因-信息不全','无法定位/复现','无法定位-日志超期','无法定位-日志缺失']
