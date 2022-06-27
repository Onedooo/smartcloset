from django.db import models
from register.models import Account

class MyClothes(models.Model):
    myclothid = models.IntegerField(primary_key=True)
    accountid = models.ForeignKey(Account, on_delete=models.CASCADE, db_column='accountid')
    mycolor = models.CharField(max_length=40)
    mycategory = models.CharField(max_length=40)
    buydate = models.DateField()
    myimg = models.CharField(max_length=40)

    def insert_cloth(self, accountid, mycolor, mycategory, buydate, myimg):
        if not accountid:
            raise ValueError('id를 입력하세요')
        if not mycolor:
            raise ValueError('color 입력하세요')
        if not mycategory:
            raise ValueError('category 입력하세요')
        if not buydate:
            raise ValueError('구매일 입력하세요')
        if not myimg:
            raise ValueError('이미지명을 입력하세요')
        cloth = self.model(
            accountid=accountid,
            mycolor=mycolor,
            mycategory=mycategory,
            buydate=buydate,
            myimg=myimg
        )
        cloth.save(using=self._db)
        return cloth

    class Meta:
        managed = False
        db_table = 'MyClothes'

    def __str__(self):
        return "이름 : " + self.name
