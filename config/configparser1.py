import  configparser

config = configparser.ConfigParser()

config["ProjectConfig"] = {
    "target_url": "https://wangcai-test-ks.xiaoduoai.com",
    "login_url": "/api/auth/mp_switcher"
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)

# import configparser
#
# config = configparser.ConfigParser()
# config.read("config.ini", encoding="utf-8")
# print(config.sections())
