# coding:utf-8
# @Time : 2020/9/10 下午4:47 
# @Author : wxm
# @File : middleware.py.py 
# @Software: PyCharm
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class my_test_middle(MiddlewareMixin):
    def __init__(self, get_response):
        print("-----------init--------------")
        self.get_response = get_response
        print("-------get_response-------------")
        print(type(self.get_response), self.get_response)

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_request(self, request):
        res = self.get_response(request)
        print("get_response方法或者的值:", res)
        print("-----------------------process_request-------------")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        addr = request.META['REMOTE_ADDR']
        addr_list = ['192.168.10.1']
        print("------------process_view---------------")

    def process_exception(self, request, exception):
        print("Exception:", exception)
        raise exception

    def process_response(self, request, response):
        print("---------------process_response-----------------")
        # print(response)
        return response