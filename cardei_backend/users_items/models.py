import datetime
from django.db import models

from account import models as account_models


class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    picture = models.ImageField(
        upload_to='category/logo',
        null=True,
        blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        account_models.CardeiUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.user}. {self.title}'


class Element(models.Model):
    title = models.TextField(null=False, blank=False)
    login = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)
    site = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    owner_name = models.TextField(null=True, blank=True)
    card_number = models.TextField(null=True, blank=True)
    year = models.TextField(null=True, blank=True)
    month = models.TextField(null=True, blank=True)
    cvv = models.TextField(null=True, blank=True)
    pin_code = models.TextField(null=True, blank=True)
    date_creation = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False
    )
    date_update = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False
    )
    archived = models.BooleanField(default=False)
    tag = models.ManyToManyField(
        Tag,
        blank=True)
    category = models.ForeignKey(
        Category,
        null=False,
        blank=False,
        on_delete=models.CASCADE)

    user = models.ForeignKey(account_models.CardeiUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}. {self.category} - {self.id}'
