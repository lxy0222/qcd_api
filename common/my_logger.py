#作者    ：YCKJ1130   

#创建时间：2020/6/23 10:59  

#文件    ：my_logger.py

#编译器  ：PyCharm

# import logging
# from logging.handlers import RotatingFileHandler
# from common.read_path import *
# from common.read_config import ReadConfig
# mylevel=ReadConfig().read_config(config_path,'LOG','log_config')
# my_logger=logging.getLogger('root')
# my_logger.setLevel(mylevel)
# formatter= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler=RotatingFileHandler(log_path,encoding='UTF-8',maxBytes=1*1024,backupCount=3)  #输出到指定文件txt
# handler.setFormatter(formatter)
# handler.setLevel('INFO')
# my_logger.addHandler(handler)