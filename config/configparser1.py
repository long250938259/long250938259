import  configparser

config = configparser.ConfigParser()

config["DEFAULT"] = {
    "target_url": "https://wangcai-test-ks.xiaoduoai.com",
    "login_url": "https://wangcai-test-ks.xiaoduoai.com"
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)