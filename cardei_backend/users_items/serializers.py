from rest_framework import serializers

from users_items import models


class TagSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)

    class Meta:
        model = models.Tag
        fields = ['title']


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UsersItemsSerializer(DynamicFieldsModelSerializer):
    tag = TagSerializer(many=True)

    class Meta:
        model = models.Element
        fields = '__all__'

    def create(self, validated_data):
        tags = validated_data.pop('tag', None)

        instance_super = super(UsersItemsSerializer, self).create(validated_data)

        if tags:
            tag_list = []
            for tag in tags:
                tag_inst = self.process_tags(tag['title'], instance_super)
                tag_list.append(tag_inst)

            instance_super.tag.set(tag_list)
            instance_super.save()

        return instance_super

    def process_tags(self, tag, instance_super):
        tag_exists = models.Tag.objects.filter(title=tag).exists()
        if tag_exists:
            return models.Tag.objects.filter(title=tag).first()

        return models.Tag.objects.create(title=tag, user=instance_super.user)
