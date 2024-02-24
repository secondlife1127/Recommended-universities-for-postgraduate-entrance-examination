from django import template

register = template.Library()


@register.filter
def filter_by_user(collection, user_id):
    if collection.filter(user_id=user_id):
        res = collection.filter(user_id=user_id).first().get_collection_display()
        return [res]

    else:
        return ["点击收藏"]


@register.filter
def filter_by_user1(collection, user_id):
    if collection:
        if collection.filter(user_id=user_id):
            res = collection.filter(user_id=user_id).first().score
            return [res]
        return ['未评分']
    else:
        return ['未评分']


