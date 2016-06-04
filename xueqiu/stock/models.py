#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(
        verbose_name="stock_name",
        max_length=100
    )
    followers_number = models.PositiveIntegerField(
        verbose_name="followers_number",
        default=0

    )
    new_followers_number = models.IntegerField(
        verbose_name="increased_number",
        default=0
    )
    value_increased_percent = models.CharField(
        "increase_percent",
        max_length=10,
        blank=True,
        null=True
    )
    update_time = models.DateTimeField(
        'update_time',
        auto_now=True
    )
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '股票信息'
        ordering = ['new_followers_number', 'update_time']

    


    

        




        

