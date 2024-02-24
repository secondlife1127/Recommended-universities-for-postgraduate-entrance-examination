import datetime
from datetime import time
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.pagination import Pagination
from app01.views.form import UserInfoModelForm


# 用户列表，调试用
# def user_list(request):
#     # 去数据库中获取用户列表
#     user_list = models.User.objects.all()
#
#     return render(request, 'user_list.html', {'user_list': user_list})
#
# from django.http import JsonResponse


# 用户评分模块
def user_score(request, school_id):
    # 获取用户id
    user_id = list(request.session.values())[0].get('id')

    if request.method == 'POST':
        # 获取评分
        score = request.POST.get('score')
        print(score)
        if not score.isnumeric():
            return JsonResponse({'message': '请求方法不支持'}, status=405)

        score_time = timezone.now()

        # 将信息写入数据库
        exists = models.UserScore.objects.filter(user_id=user_id, school_id=school_id)
        if exists:
            exists.update(score=score, score_time=score_time)
        else:
            models.UserScore.objects.create(user_id=user_id, score=score, school_id=school_id, score_time=score_time)
        # 返回 JSON 响应
        return JsonResponse({'message': '提交成功'})
    # 非 POST 请求时的处理
    return JsonResponse({'message': '请求方法不支持'}, status=405)


# 我的评分显示模块
def score_list(request):
    # score_list = []
    # 显示当前用户的评分信息
    user_id = list(request.session.values())[0].get('id')

    # 从用户评分表中获取数据
    # object_list = models.UserScore.objects.filter(user_id=user_id)
    queryset = models.UserScore.objects.filter(user_id=user_id).order_by('-score_time')
    # 2.实例化分页对象
    page_object = Pagination(request, queryset)
    context = {
        "a7": "active",
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'score_list.html', context)


# 用户删除评分模块
def score_delete(request, school_id):
    user_id = list(request.session.values())[0].get('id')
    models.UserScore.objects.filter(school_id=school_id, user_id=user_id).delete()
    return redirect('/score/list')


# 用户信息显示和修改
def user_info(request):
    """ 编辑用户信息"""
    user_id = list(request.session.values())[0].get('id')

    row_object = models.User.objects.filter(id=user_id).first()
    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行数据（对象）
        form = UserInfoModelForm(instance=row_object)
        # print("form:",form)
        return render(request, 'user_info.html', {'form': form})

    form = UserInfoModelForm(data=request.POST, instance=row_object)
    print("form:",form)
    if form.is_valid():
        # 默认保存的是用户输入的所有数据，如果想要再用户输入以外增加一点值
        # form.instance.字段名 = 值
        form.save()
        return render(request, 'user_info.html', {"status": "信息修改成功！","form": form})
    return render(request, 'user_info.html', {"form": form})


# 用户收藏模块
@csrf_exempt
def user_collection(request):
    #获取用户在前端页面点击收藏的学校id
    school_id = request.POST.get('school_id')
    # 获取用户id
    user_id = list(request.session.values())[0].get('id')
    collection_time = timezone.now()

    # 判断用户是否已经收藏过该院校
    exists = models.UserCollection.objects.filter(user_id=user_id, school_id=school_id)
    if exists:
        exists.delete()
        # collection = exists.first().collection
        # exists.update(collection=not collection, collection_time=collection_time)
        is_collected = False
    else:
        models.UserCollection.objects.create(user_id=user_id, collection=1, school_id=school_id,
                                             collection_time=collection_time)
        is_collected = True

    response_data = {'is_collected': is_collected}
    return JsonResponse(response_data)


# 显示我的收藏模块
def collection_list(request):
    # score_list = []

    user_id = list(request.session.values())[0].get('id')

    # 从用户收藏表中获取数据
    # object_list = models.UserScore.objects.filter(user_id=user_id)
    queryset = models.UserCollection.objects.filter(user_id=user_id).order_by('-collection_time')

    # 2.实例化分页对象
    page_object = Pagination(request, queryset)

    context = {
        "a8": "active",
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, 'collection_list.html', context)


# 用户取消收藏模块
def collection_delete(request, school_id):
    user_id = list(request.session.values())[0].get('id')
    models.UserCollection.objects.filter(school_id=school_id, user_id=user_id).delete()
    return redirect('/collection/list')
