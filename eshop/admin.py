from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import *
# Register your models here.




class LetadloAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80,'rows': 30})},
    }

admin.site.register(Letadlo, LetadloAdmin)