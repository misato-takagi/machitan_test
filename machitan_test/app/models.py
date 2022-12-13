from django.db import models
#スタッフはログインユーザーと連携するようにする
from accounts.models import CustomUser
from django.utils import timezone

class Store(models.Model):
    name = models.CharField(max_length=100,verbose_name='店舗')
    address = models.CharField(max_length=100,verbose_name='住所',blank=True,null=True)
    tel = models.CharField(max_length=100, verbose_name='電話番号',blank=True, null= True)
    description = models.TextField(verbose_name='説明',default='',blank=True)
    image = models.ImageField(upload_to='images',verbose_name='イメージ画像',null=True,blank=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    #OneToOneFieldは1対1。スタッフは店舗を掛け持ちできない
    user = models.OneToOneField(CustomUser,verbose_name='スタッフ',on_delete=models.CASCADE)
    store = models.ForeignKey(Store,verbose_name='店舗',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.store}:{self.user}'


class Booking(models.Model):
    staff = models.ForeignKey(Staff,verbose_name='スタッフ',on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='姓',max_length=100,null=True,blank=True)
    last_name = models.CharField(verbose_name='名',max_length=100,null=True,blank=True)
    tel = models.CharField(verbose_name='電話番号',max_length=100,null=True,blank=True)
    remarks = models.TextField(verbose_name='備考',default='',blank=True)
    start = models.DateTimeField(verbose_name='開始時間',default=timezone.now)
    end = models.DateTimeField(verbose_name='終了時間',default=timezone.now)
  
    def __str__(self):
        start = timezone.localtime(self.start).strftime('%Y/%m/%d %H:%M')
        end = timezone.localtime(self.end).strftime('%Y/%m/%d %H:%M')

        #管理画面での表示のされ方を指示している
        return f'{self.first_name}{self.last_name}{start}~{end}{self.staff}'