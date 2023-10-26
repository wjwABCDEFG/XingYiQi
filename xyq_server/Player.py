# 暂时先不要这个对象，不维护player列表，只有socket列表
# # -*- coding: utf-8 -*-
# """
# @Time    : 2023/10/6 17:53
# @Author  : wenjiawei
# """
# from common.Serializable import Serializable
# from common.db import g_mongo
#
#
# class Player(Serializable):
#
#     def __init__(self, client=None, id=None):
#         super().__init__()
#         self.pai_list = []
#         self.client = client
#         self.user_info = {}
#         if id:
#             self.id = id
#
#     def get_user_info(self, id):
#         if not self.user_info:
#             self.user_info = g_mongo.user.find_one({'open_id': id})
#         return self.user_info
