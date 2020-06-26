#作者    ：YCKJ1130   

#创建时间：2020/6/24 14:10  

#文件    ：do_regx.py

#编译器  ：PyCharm

import re
from common.get_data import GetData
class DoRegx:
    @staticmethod
    def do_regx(afterdata):
        vardict={}   #存储通过正则找到的key和value组成的键值对
        i=0
        for key in re.findall('\$\{.*?\}', str(afterdata)):   #找到${xxx}
            valuelist=[]     #存储value值
            for value in re.findall('\$\{(.*?)\}', str(afterdata)):   #找到xxx
                valuelist.append(value)
            vardict[key]=valuelist[i]   #按value列表的下表查找值，与key形成键值对
            i += 1  #每遍历第一个value后i就自加1
        '''替换变量值，判断是否为${loanid},不对它进行替换'''
        for key,value in vardict.items():
            if key=="${loanid}":
                afterdata.replace(key,key)
            else:
                afterdata=afterdata.replace(key,str(getattr(GetData, value)))
        return afterdata



        #用于将所有变量替换的操作
        # while re.search('\$\{(.*?)\}',str(afterdata)):
        #     key=re.search('\$\{(.*?)\}',afterdata).group(0)
        #     value=re.search('\$\{(.*?)\}',afterdata).group(1)
        #     if getattr(GetData,value)!=None:
        #         afterdata=afterdata.replace(key,str(getattr(GetData,value)))
        #     else:
        #         afterdata=afterdata.replace(key,key)

if __name__ == '__main__':
    s='{"case_id":"${loanid}", "interface":"${login_tel}","interface1":"${admin_tel}"}'
    afterdata=DoRegx.do_regx(s)
    print(eval(afterdata))
    # print(type(eval(afterdata)))