from rest_framework import serializers

from users_items import models
from constants.constants import items_fields


class TagSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)

    class Meta:
        model = models.Tag
        fields = ['title']


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    field_set = serializers.SerializerMethodField()

    def get_field_set(self, obj):
        return items_fields[obj.title]

    class Meta:
        model = models.Category
        fields = '__all__'


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class ItemTagField(serializers.Field):
    def to_representation(self, obj):
        return list(obj)

    def to_internal_value(self, data):
        return data

    def add_tag_to_element(self, tags: set, instance_super):
        for tag in tags:
            tag_inst = self.process_tags(tag, instance_super)
            models.ElementTag.objects.create(element=instance_super, tag=tag_inst)

    def process_tags(self, tag_name, instance_super):
        tag_exists = models.Tag.objects.filter(title=tag_name, user=instance_super.user).exists()
        if tag_exists:
            return models.Tag.objects.filter(title=tag_name, user=instance_super.user).first()

        return models.Tag.objects.create(title=tag_name, user=instance_super.user)


class UsersItemsSerializer(DynamicFieldsModelSerializer):
    tag = ItemTagField()

    class Meta:
        model = models.Element
        fields = '__all__'

    def create(self, validated_data):
        tags = validated_data.pop('tag', None)

        instance_super = super(UsersItemsSerializer, self).create(validated_data)

        if tags:
            self.add_tag_to_element(set(tags), instance_super)

        return instance_super

    def update(self, instance, validated_data):
        tags = validated_data.pop('tag', None)

        instance_super = super(UsersItemsSerializer, self).update(
            instance,
            validated_data
        )

        if tags:
            instance_super.element_tag.filter().delete()
            self.add_tag_to_element(set(tags), instance_super)
        else:
            instance_super.element_tag.filter().delete()

        return instance_super

    def add_tag_to_element(self, tags: set, instance_super):
        for tag in tags:
            tag_inst = self.process_tags(tag, instance_super)
            models.ElementTag.objects.create(element=instance_super, tag=tag_inst)

    def process_tags(self, tag_name, instance_super):
        tag_exists = models.Tag.objects.filter(title=tag_name, user=instance_super.user).exists()
        if tag_exists:
            return models.Tag.objects.filter(title=tag_name, user=instance_super.user).first()

        return models.Tag.objects.create(title=tag_name, user=instance_super.user)
