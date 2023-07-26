# coding:utf-8

import unittest
import requests


class DeviceTestCase(unittest.TestCase):
    u'''测试用例集合：离线设备数接口'''

    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        cls.url = 'http://staging.senserealty.sensetime.com/senserealty/device-stat/offline-devices-count'
        cls.ak = 'l1-f37b7f8c-w0f55aa0948a'
        cls.start_timestamp = '1610347760'

    def test01(self):
        u'''测试用例1：所有参数都正确'''
        par = {
            'ak': self.ak,
            'start_timestamp': self.start_timestamp
        }
        r = self.s.get(self.url, params=par)
        result = r.json()
        print(result)
        result = result['error_msg']
        self.assertTrue(result == 'ok')

    def test02(self):
        u'''测试用例2：不填ak'''
        par = {
            'ak': '',
            'start_timestamp': self.start_timestamp
        }
        r = self.s.get(self.url, params=par)
        result = r.json()
        print(result)
        result = result['error_code']
        self.assertNotEqual(result, 0)

    def test03(self):
        u'''测试用例3：不填start_timestamp'''
        par = {
            'ak': self.ak,
            'start_timestamp': ''
        }
        r = self.s.get(self.url, params=par)
        result = r.json()
        print(result)
        result = result['error_code']
        self.assertNotEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
