# -*- coding: utf-8 -*-

from django.db import models


class Allowed(models.Model):
    username = models.CharField('username', max_length=64, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'usuario permitido'
        verbose_name_plural = "usuarios permitidos"
