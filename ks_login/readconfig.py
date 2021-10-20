import configparser
import codecs


class ReadConfig:
    """
    专门读取配置文件的，.ini文件格式
    """
    def __init__(self, filename):
        # configpath = os.path.join(prjDir,filename)
        configpath = filename
        # print(configpath)
        fd = open(configpath, encoding="utf-8")
        data = fd.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codecs.open(configpath, "w")
            files.write(data)
            files.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath, encoding="utf-8")

    def getValue(self, env, name):
        return self.cf.get(env, name)


ff = open("D:/新建文件夹/new 1.txt", encoding="utf-8")
data1 = ff.read()
print(data1[:3])
print(codecs.BOM_UTF8)
print(data1[:3] == codecs.BOM_UTF8)