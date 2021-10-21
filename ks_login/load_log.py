import logging
import os
import time

project_abs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(project_abs_path, 'log_file')


class Log(object):
    def __init__(self):
        self.filename = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def basicconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger("author")
        logger.setLevel(logging.DEBUG)
        # 创建一个用于写入文件的handler
        file_handler = logging.FileHandler(filename=self.filename, mode='a', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        # 创建一个输出到控制台的handler
        console_handler = logging.StreamHandler()  # 可设置stream
        console_handler.setLevel(logging.DEBUG)
        # 设置输入格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(file_handler)
        logger.removeHandler(console_handler)
        file_handler.close()

    def debug(self, message=None, title='日志'):
        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as e:
            print(e)
        # self.write.write_log(title, 'debug', '自动化测试日志', message)
        self.basicconsole('debug', time.strftime('%Y-%m-%d %H:%M:%S') + '\t' + message + '\n')

    def info(self, message=None, title='日志'):
        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as e:
            print(e)
        # self.write.write_log(title, 'info', '自动化测试日志', message)
        self.basicconsole('info', time.strftime('%Y-%m-%d %H:%M:%S') + '\t' + message + '\n')

    def warning(self, message=None, title='日志'):
        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as e:
            print(e)
        # self.write.write_log(title, 'warning', '自动化测试日志', message)
        self.basicconsole('warning', time.strftime('%Y-%m-%d %H:%M:%S') + '\t'  + message + '\n')

    def error(self, message=None, title='日志'):
        try:
            if isinstance(message, str):
                pass
            else:
                message = str(message)
        except Exception as e:
            print(e)
        # self.write.write_log(title, 'error', '自动化测试日志', message)
        self.basicconsole('error', time.strftime('%Y-%m-%d %H:%M:%S') + '\t' + message + '\n')






