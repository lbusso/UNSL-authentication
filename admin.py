# -*- coding: utf-8 -*-

from django.contrib import admin
from authentication.models import Allowed


@admin.register(Allowed)
class AllowedAdmin(admin.ModelAdmin):
    pass
