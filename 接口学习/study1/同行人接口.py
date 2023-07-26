# coding:utf-8

import requests
import unittest
import hashlib


class GroupTestCase(unittest.TestCase):
    @classmethod  # 为了只在开头和结尾执行setup和teardown
    def setUpClass(cls):
        cls.s = requests.session()
        cls.url = 'http://sp.dida-test.sensetime.com/realty-api/v1/person/companion'
        cls.person_id = '1356515227117551616'
        cls.group_id = '8645b40f93'
        cls.start_time = 1618989271  # start_time和end_time只能是同一天的
        cls.end_time = 1618989876
        cls.h = {

        }

    @classmethod
    def tearDownClass(cls):
        pass

    def test_01(self):
        par = {
            "person_id": self.person_id,
            "group_id": self.group_id,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }
        r = self.s.post(self.url, params=par, headers=self.h)
        result = r.json()  # 将返回结果直接转成json
        result = result["message"]
        print(result)
        self.assertTrue(result == "success")


if __name__ == '__main__':
    unittest.main()
