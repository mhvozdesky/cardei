from django.contrib import admin
from users_items import models


class ElementAdmin(admin.ModelAdmin):
    readonly_fields = ['date_creation', 'date_update']


admin.site.register(models.Element, ElementAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)
