from django.db import models
#スタッフはログインユーザーと連携するようにする
from accounts.models import CustomUser


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