# -*- coding:utf-8 -*-

"""
 author 对象. 存储author页面(http://www.shicimingju.com/category/xianqinshiren)相关信息
 以及其简介(http://www.shicimingju.com/chaxun/zuozhe/67.html)
"""
class Author:
    # 名字
    name = ""

    # 诗词个数
    numofpoems = 0

    # 所在的url
    url = ""

    # 简介
    brief = ""

    # 内置方法，方便输出.
    def __str__(self):
        return "name=" + self.name  + ", " + "numofpoems=" + str(self.numofpoems) + ", " \
                + "url=" + self.url + ", " + "brief:" + str(len(self.brief))
