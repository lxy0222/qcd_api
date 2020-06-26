import os
#获取顶级目录
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#获取测试用例路径
testcase_path=project_path+r"\test_data\test_case.xlsx"
#获取测试报告路径
testreport_path=project_path+r"\test_result\report.html"
#配置文件路径
config_path=project_path+r'\common\conf\testcaseconfiger.config'
#日志输出路径
log_path=project_path+r'\common\log\log.txt'
if __name__ == '__main__':
    print(project_path)
    print(testcase_path)
    print(testreport_path)
    print(config_path)