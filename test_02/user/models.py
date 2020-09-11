from django.db import models

# Create your models here.


class UserInfoManage(models.Manager):
    '''用户模型管理类'''
    def all(self):
        all_user = super().all()
        all_user = all_user.filter(isDelete=False)
        return all_user

    def create_user(self, username, password):
        # user = UserInfo()
        user = self.model()
        user.uname = username
        user.upassword = password
        user.save()
        return user


class UserInfo(models.Model):
    uname = models.CharField(max_length=30, unique=True, db_index=True)  # 增加索引值，唯一性
    # uname = models.CharField(max_length=30)
    upassword = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)

    objects = UserInfoManage()  # 用户模型管理类的实例

    def __str__(self):
        return self.uname

    class Meta:
        db_table = 'user'