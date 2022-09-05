from django.contrib import admin
from users_items import models

admin.site.register(models.Element)
admin.site.register(models.Category)
admin.site.register(models.Tag)
