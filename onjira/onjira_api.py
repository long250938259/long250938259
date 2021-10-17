from jira import JIRA
import urllib3
import base64
from onjira import const


class JiraApi(object):
    global jira_url
    jira_url = const.jira_url

    def encryption(self, st):
        encode = base64.b64encode(st.encode('utf-8'))
        return str(encode, 'utf-8')

    def decrypt(self, st):
        decode = base64.b64decode(st)
        return str(decode, 'utf-8')

    def login(self):
        user_name = self.decrypt(const.email_user_name)
        password = self.decrypt(const.email_password)
        jirap = JIRA(basic_auth=(user_name, password), options={
            'server': const.jira_url})
        return jirap


if __name__ == "__main__":
    login = JiraApi()
    message = login.login()
    print(message)