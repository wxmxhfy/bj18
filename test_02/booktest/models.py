from django.db import models

# Create your models here.
class BookInfoManage(models.Manager):
    '''图书模型管理类'''
    def all(self):
        books = super().all()
        books = books.filter(isDelete=False)
        return books

    def create_book(self, btitle, bpub_date):
        # book = BookInfo()
        book = self.model()
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        return book


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bauthor = models.CharField(max_length=20)
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    objects = BookInfoManage()      # 图书模型管理类的对象

    def __str__(self):
        return self.btitle

    class Meta:
        db_table = 'book'

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hbook = models.ForeignKey('BookInfo', on_delete='models.CASCADE')
    hcomment = models.CharField(max_length=20, null=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname

    class Meta:
        db_table = 'hero'


class AreaInfo(models.Model):
    '''地区类模型'''
    # 地区名称
    atitle = models.CharField(max_length=30)
    # 关系属性，代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'area'


class PicTest(models.Model):
    goods_pic = models.ImageField(upload_to='booktest')

