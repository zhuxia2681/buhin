from django.db import models
import datetime as dt
from django.utils import timezone
from django.contrib.auth.models import User

inq_type_choice = (("Inquiry", "見積"),
        ("Order", "注文"))
prog_choice = (
        ("InqNow","見積中"),
        ("InqDone","見積完了"),
        ("PartDone","一部完了"),
        ("AllDone","全部完了"),
        )

user_name = []
n = 0
for i in User.objects.all():
    user_name.append((str(n),str(i)))
    n += 1

class Anken(models.Model):
    id = models.IntegerField('No.',primary_key=True)
    anken_id = models.IntegerField('案件番号')
    item_name = models.CharField('件名',max_length=20)
    ope_name = models.CharField('担当者',max_length=20)
    created_at = models.DateTimeField('作成日時',default=dt.datetime.now())
    updated_at = models.DateTimeField('更新日時',default=dt.datetime.now())
    inq_type = models.CharField("種類",max_length=10,choices=inq_type_choice,default=inq_type_choice[0][1])
    progress = models.CharField("進捗",max_length=10,choices=prog_choice,default="見積中")
    body_num = models.CharField("車台番号",max_length=10,default="0000")

    def __str__(self):
        return self.item_name
