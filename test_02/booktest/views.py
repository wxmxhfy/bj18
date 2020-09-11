from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from booktest.models import HeroInfo, BookInfo, AreaInfo, PicTest
from django.core.paginator import Paginator
from django.conf import settings
from datetime import date
# Create your views here.
def index(request):
    # a = 's' + 1
    print(type(request))
    addr = request.META['REMOTE_ADDR']
    print(addr)
    return render(request, 'booktest/index.html', {'content':'<h1>转义</h1>'})


def show_books(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/show_books.html', {'books': books})


def show_heros(request, bid):
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()
    return render(request, 'booktest/show_heros.html', {'heros': heros})


def book_add(request):
    b = BookInfo()
    b.btitle = '真三国无双'
    b.bpub_date = date(2010,10,10)
    b.read = 100
    b.save()
#    return HttpResponseRedirect('/booktest/showbooks')
    return redirect('/booktest/showbooks')

def book_delete(request, bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    return HttpResponseRedirect('/booktest/showbooks')


def showareas(request, bid):
    area = AreaInfo.objects.get(id=bid)
    # 上级地区
    aParent = area.aParent
    # 下级地区
    aChild = area.areainfo_set.all()
    return render(request, 'booktest/areas.html', {'area': area, 'aParent': aParent, 'aChild': aChild})


def allarea(request, pindex):
    areas = AreaInfo.objects.all()
    # 分页，每页显示10条
    paginator = Paginator(areas, 10)
    # print(paginator.num_pages)
    # print(paginator.page_range)
    # page是Paginator类对象的方法，返回一个Page类对象
    if pindex == '':
        pindex = 1
    else:
        pindex = int(pindex)
    page = paginator.page(pindex)
    # print(page.number)
    # print(page.object_list)
    # print(page.paginator)
    return render(request, 'booktest/allarea.html', {'page': page, 'pindex':pindex})


def upload_pic(request):
    return render(request, 'booktest/upload_pic.html')


def upload_handle(request):
    '''上传图片处理'''
    pic = request.FILES['pic']
    print("----------------------")
    print(type(pic), pic.content_type, pic.size)
    # print(pic.name)
    # pic.chunks()
    # 创建一个文件
    save_path = "%s/booktest/%s" %(settings.MEDIA_ROOT, pic.name)
    # 获取上传文件的内容并写到创建的文件中
    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)
    # 在数据库上保存上传的文件
    PicTest.objects.create(goods_pic='booktest/%s' % pic.name)
    # 返回
    return HttpResponse("OK")
