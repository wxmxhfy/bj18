from django.contrib import admin
from booktest.models import BookInfo, HeroInfo, PicTest
# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bpub_date', 'bread', 'isDelete']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hcomment', 'isDelete']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(PicTest)
