from .models import Tag, ElementTag


def clear_empty_tags(user):
    user_tags = Tag.objects.filter(user=user)
    list_to_delete = []
    for tag in user_tags:
        if not tag.element_tag.all().exists():
            list_to_delete.append(tag)

    for i in list_to_delete:
        i.delete()