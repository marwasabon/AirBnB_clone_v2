#!/usr/bin/python3
'''Testcases for mysql database'''
import unittest
import os
import tests
import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'hbnb_dev'
DB_PWD = 'hbnb_dev_pwd!'
DB = 'hbn_dev_db'


class TestMySQLdb(unittest.TestCase):
    '''test the database'''

    def test_establish_connection(self):
        '''test connection to mysql db with configs'''
        try:
            db = MySQLdb.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PWD
            )
        except Exception as e:
            print("connection with DB failed due to {}", e)
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()

