from django.contrib import admin
from users_items import models


class ElementTagInLineElement(admin.TabularInline):
    model = models.ElementTag
    extra = 1


class ElementAdmin(admin.ModelAdmin):
    readonly_fields = ['date_creation', 'date_update']

    inlines = (ElementTagInLineElement,)


admin.site.register(models.Element, ElementAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)
