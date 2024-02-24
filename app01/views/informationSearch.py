from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import render, redirect
from app01 import models
from django.utils.safestring import mark_safe
from app01.utils.bootstrap import BootStrapModelForm, BootStrapForm
from app01.utils.pagination import Pagination


def special_list(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["name__contains"] = search_data

    queryset = models.Special.objects.filter(**data_dict)

    page_object = Pagination(request, queryset)

    context = {
        "a2": "active",
        "search_data": search_data,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 页码
    }
    return render(request, 'special_list.html', context)


def scoreline_list(request):
    search_data = request.GET.get('q', "")

    queryset = models.ScoreLine.objects.filter(
        Q(year__icontains=search_data) | Q(school__icontains=search_data)
    ).order_by("-year")

    page_object = Pagination(request, queryset)

    context = {
        "a3": "active",
        "search_data": search_data,

        "queryset": page_object.page_queryset,  # 分完页的数据
        # "queryset": queryset,  # 分完页的数据
        "page_string": page_object.html()  # 页码
    }
    return render(request, 'scoreline_list.html', context)


def rate_list(request):
    search_data = request.GET.get('q', "")

    queryset = models.Rate.objects.filter(
        Q(year__icontains=search_data) | Q(school__icontains=search_data)
    ).order_by("-year")

    page_object = Pagination(request, queryset)

    context = {
        "a4": "active",
        "search_data": search_data,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 页码
    }
    return render(request, 'rate_list.html', context)


def index(request):
    search_data = request.GET.get('q', "")
    queryset = models.School.objects.all()
    if search_data:
        queryset = models.School.objects.filter(
            Q(name__icontains=search_data) | Q(location__icontains=search_data)
        )
    location = request.GET.get('location', '')
    if location:
        queryset = models.School.objects.filter(location=location)

    loctions = [i.get('location') for i in models.School.objects.all().values('location').distinct()]
    # data_dict = {}
    # if search_data:
    #     data_dict["name__contains"] = search_data
    # queryset = models.School.objects.filter(
    #     **data_dict
    # )

    page_object = Pagination(request, queryset)
    context = {
        "locations":loctions,
        "link": "https://yz.chsi.com.cn",
        "a0": "active",
        "search_data": search_data,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 页码
    }
    return render(request, 'index.html', context)


def school_list(request):
    user_id = list(request.session.values())[0].get('id')
    search_data = request.GET.get('q', "")
    queryset = models.School.objects.all()
    if search_data:
        queryset = models.School.objects.filter(
            Q(name__icontains=search_data) | Q(location__icontains=search_data)
        )
    location = request.GET.get('location', '')
    if location:
        queryset = models.School.objects.filter(location=location)

    loctions = [i.get('location') for i in models.School.objects.all().values('location').distinct()]

    page_object = Pagination(request, queryset)

    context = {
        "locations": loctions,
        "user_id": user_id,
        "link": "https://yz.chsi.com.cn",
        "a1": "active",
        "search_data": search_data,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 页码
    }
    return render(request, 'school_list.html', context)
# def school_list_filter(request, location):
#     user_id = list(request.session.values())[0].get('id')
#     search_data = request.GET.get('q', "")
#
#     queryset = models.School.objects.filter(location=location)
#     queryset = queryset.filter(Q(name__icontains=search_data) | Q(location__icontains=search_data))
#
#     loctions = [i.get('location') for i in models.School.objects.all().values('location').distinct()]
#
#     print("locations", loctions)
#     page_object = Pagination(request, queryset)
#
#     context = {
#         "locations": loctions,
#         "user_id": user_id,
#         "link": "https://yz.chsi.com.cn",
#         "a1": "active",
#         "search_data": search_data,
#         "queryset": page_object.page_queryset,  # 分完页的数据
#         "page_string": page_object.html()  # 页码
#     }
#     return render(request, 'school_list.html', context)
