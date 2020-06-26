#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import unittest
import HTMLTestRunnerNew
from common.read_path import *
from common.test_httprequest import TestHttpRequest
import time
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
with open(testreport_path,'wb') as file: #上下文管理器，自动关闭文件
    #执行用例
    runner= HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                             verbosity=2,
                                             title='单元测试报告-'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
                                             tester='蛋挞',
                                             description='第一阶段总结测试报告')
    runner.run(suite)
# my_logger.info('我自己的收集器info日志')
