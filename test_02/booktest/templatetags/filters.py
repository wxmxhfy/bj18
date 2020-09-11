# coding:utf-8
# @Time : 2020/9/9 下午2:44 
# @Author : wxm
# @File : filter.py 
# @Software: PyCharm
# 导入library类
from django.template import Library

# 创建一个Library类对象
register = Library()

@register.filter
def mod(value):
    return value % 2 == 0

@register.filter
def mod_val(num, val):
    return num % val == 0
