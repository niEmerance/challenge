# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Restaurant(models.Model):
    resto_name = models.CharField(max_length =30)
    resto_location = models.CharField(max_length =30)
    resto_speciality= models.CharField(max_length =30)
    resto_image = models.ImageField(upload_to = 'photos/')
    resto_email = models.EmailField()
    resto_uploader = models.CharField(max_length =30)

    def __str__(self):
        return self.resto_name

    def save_Restaurant(self, user):
        self.save()