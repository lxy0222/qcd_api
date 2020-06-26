import unittest
from common.read_path import *
from common.http_request import HttpRequest
from common.do_excel import DoExcel
from common.get_data import GetData
from ddt import ddt,data
from common.do_mysql import DoMysql
testdata = DoExcel.get_data(testcase_path)
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass
    @data(*testdata)
    def test_api(self,item):
        passorfail=None
        #请求之前完成loanid的替换
        if item['data'].find('${loanid}') != -1:
            if getattr(GetData, 'loanid')==None:
                id=DoMysql.cnn_db('select max(id) from loan where memberid=82')[0]
                item['data'] = str(item['data']).replace('${loanid}', str(id))
                setattr(GetData, 'loanId',id)  #利用反射去存储结果
            else:
                item['data'] = str(item['data']).replace('${loanid}',str(getattr(GetData, 'LoanId')))
        #判断sql语句
        if item['sql']==None:  #没有sql语句时
            print('正在执行的用例是：第{}条用例'.format(item['case_id']))
            res = HttpRequest().http_request(item['url'], eval(item['data']), item['http_method'],
                                             getattr(GetData, 'COOKIE'))
        else:  #有sql语句时
            print('正在执行的用例是：第{}条用例'.format(item['case_id']))
            sql=eval(item['sql'])['sql']
            #http请求前
            before_amount=DoMysql.cnn_db(sql)[0]
            res = HttpRequest().http_request(item['url'], eval(item['data']), item['http_method'],
                                             getattr(GetData, 'COOKIE'))
            #http请求后
            after_amount=DoMysql.cnn_db(sql)[0]
            amount=abs(after_amount - before_amount)
            if str(amount)==str(eval(item['data'])['amount']):
                check_res='数据库校验正确'
            else:
                check_res='数据库校验失败'
            DoExcel.write_checkres(testcase_path,item['interface'],item['case_id'],check_res)
        print(res.json())
        if res.cookies:
            setattr(GetData, 'COOKIE', res.cookies)
        try:
            self.assertEqual(str(item['excepted']), res.json()['code'])  # 断言，没有断言默认不管对错测试用例都执行通过
            passorfail="成功"
        except Exception as e:
            print('失败用例{},{}：{}'.format(item['interface'], item['case_id'], res.json()))
            passorfail="失败"
            raise e
        finally:
            DoExcel.write_back(testcase_path,item['interface'],item['case_id'],str(res.json()),passorfail)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
    # TestHttpRequest().test_api()