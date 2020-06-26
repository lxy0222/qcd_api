import configparser
class ReadConfig:
    def read_config(self,config_path,section,option):
        '''读取配置文件'''
        cf=configparser.ConfigParser()
        cf.read(config_path)
        return cf[section][option]
if __name__ == '__main__':
    from common import read_path
    mode=eval(ReadConfig().read_config(read_path.config_path,'MODE','mode'))  #读取的配置文件为字符串格式，需要还原为字典类型
    print(mode)