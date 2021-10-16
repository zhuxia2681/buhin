from django.db import models
class Anken(models.Model):
    id = models.AutoField('No.',primary_key=True)
    ankenid = models.IntegerField('案件番号',Null=False,default=id)
    item_name = models.CharField('件名',max_length=20)
    ope_name = models.CharField('担当者',max_length=20)

    def __str__(self):
        return self.item_name
