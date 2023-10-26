# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/25 1:10
@Author  : wenjiawei
"""
import pymongo


class MongoDB:
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.conn['XYQ']
        self.user = self.db.get_collection('xyq_user')


g_mongo = MongoDB()


if __name__ == '__main__':
    print(list(g_mongo.user.find()))
