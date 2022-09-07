from django.contrib import admin
from users_items import models


class TagInLineElement(admin.TabularInline):
    model = models.Element.tag.through


class ElementAdmin(admin.ModelAdmin):
    readonly_fields = ['date_creation', 'date_update']

    inlines = (TagInLineElement,)


admin.site.register(models.Element, ElementAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)
