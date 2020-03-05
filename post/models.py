from django.db import models

class Posts(models.Model):
    postid = models.CharField(db_column='POSTID',max_length=30, primary_key=True)
    title = models.CharField(db_column='TITLE', max_length=30)
    content = models.CharField(db_column='CONTENT',max_length=1000,blank=True,null=True)
    date = models.DateField(db_column='DATE',blank=True,null=True)







# Create your models here.
