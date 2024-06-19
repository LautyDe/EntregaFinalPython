from django.contrib import admin
from .models import *


class CurseAdmin(admin.ModelAdmin):
  list_display = ['name', 'category']
  search_fields = ['name', 'category']
  list_filter = ['name']

# Register your models here.
admin.site.register(Curse, CurseAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Works)
admin.site.register(Avatar)