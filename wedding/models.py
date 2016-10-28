#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Gift(models.Model):
    name = models.CharField(max_length=200)
    decs = models.CharField(max_length=1000)
    url = models.URLField()
    price = models.IntegerField()
    proposed_by = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
