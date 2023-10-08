# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/6 16:00
@Author  : wenjiawei
"""
import views
from R import R

if __name__ == "__main__":
    data = views.begin()
    res = R().Data(data)
    res = res.Json()
    pass
