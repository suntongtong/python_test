import unittest
from common.login import Lgoin
import requests


#验证接口：https://xmgl-test.glodon.com/glm/services/worker-service/home/workerOverview/jobStatistics在岗工种人数统计
test_url='https://xmgl-test.glodon.com/glm/services/worker-service/home/workerOverview/jobStatistics'
class Hometest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.header = Lgoin().lgoin_system()
        print(cls.header)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        print("-------------用例开始执行了-----------")
    def tearDown(self):
        print("---------用例结束运行---------------")

    def test_count(self):
        res=requests.get(test_url,headers=self.header)
        print(res.text)




