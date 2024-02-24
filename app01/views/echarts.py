from typing import List, Any

from django.db.models import Count
from django.shortcuts import render
from django.http import JsonResponse

from app01.models import UserCollection, School, UserScore


# 数据可视化页面
def chart_list(request):
    context = {
        "a6": "active",
        # "search_data": search_data,
        # "queryset": page_object.page_queryset,  # 分完页的数据
        # "page_string": page_object.html()  # 页码
    }
    return render(request, 'chart_list.html', context)
    # return render(request, 'chart_index.html', context)


# 院校收藏榜
def school_collection(request):
    # 数据可以去数据库中获取
    from django.db.models import Case, When

    collection_counts = UserCollection.objects.filter(collection=1).values('school').annotate(
        count=Count('school')).order_by('-count')[:10]
    # print(collection_counts)
    school_ids = [count['school'] for count in collection_counts]
    ordering = Case(
        *[When(id=school_id, then=index) for index, school_id in enumerate(school_ids)]
    )
    schools = School.objects.filter(id__in=school_ids).order_by(ordering)
    school_names = [school.name for school in schools]  # 院校名称
    school_names.reverse()
    school_counts = [count['count'] for count in collection_counts]  # 对应收藏人数
    school_counts.reverse()
    result = {
        "x_data": school_names,
        "y_data": school_counts,
    }
    return JsonResponse(result)


# 院校评分榜
def school_score(request):
    # 数据可以去数据库中获取
    from django.db.models import Avg
    from django.db.models import Case, When

    school_scores = UserScore.objects.values('school').annotate(avg_score=Avg('score')).order_by('-avg_score')[:10]
    print('school scores', school_scores)

    school_ids = [count['school'] for count in school_scores]

    ordering = Case(
        *[When(id=school_id, then=index) for index, school_id in enumerate(school_ids)]
    )
    # print(school_ids)
    schools = School.objects.filter(id__in=school_ids).order_by(ordering)
    # print(schools)
    school_names = [school.name for school in schools]  # 院校名称
    school_names.reverse()
    school_avg = [count['avg_score'] for count in school_scores]  # 对应平均分
    school_avg.reverse()

    result = {
        "x_data": school_names,
        "y_data": school_avg,
    }

    return JsonResponse(result)


# 院校总数量数据提交
def total_school(request):
    province_counts = School.objects.values('location') \
                          .annotate(count=Count('id')).order_by('-count')[:10]
    # for province_count in province_counts:
    #     print('province_count', province_count)
    data = {}
    total_data = []
    for province_count in province_counts:
        data["name"] = province_count['location']
        data["value"] = province_count['count']
        total_data.append(data)
        data = {}
    print('total_data', total_data)

    # print(total_data)
    result = {
        "total_data": total_data

    }

    return JsonResponse(result)


def double_school(request):
    province_counts = School.objects.filter(is_double_one=1).values('location') \
                          .annotate(count=Count('id')).order_by('-count')[:10]

    # for province_count in province_counts:
    #     print('province_count', province_count)

    data = {}
    total_data = []
    for province_count in province_counts:
        data["name"] = province_count['location']
        data["value"] = province_count['count']
        total_data.append(data)
        data = {}
    # print('total_data', total_data)

    # school_ids = [count['school'] for count in school_scores]

    # ordering = Case(
    #     *[When(id=school_id, then=index) for index, school_id in enumerate(school_ids)]
    # )
    # print(school_ids)
    # schools = School.objects.filter(id__in=school_ids).order_by(ordering)
    # print(schools)
    # school_names = [school.name for school in schools]  # 院校名称
    # school_names.reverse()
    # school_avg = [count['avg_score'] for count in school_scores]  # 对应平均分
    # school_avg.reverse()
    # print(total_data)
    result = {
        "double_data": total_data

    }

    return JsonResponse(result)


def auto_school(request):
    province_counts = School.objects.filter(is_auto_line=1).values('location') \
                          .annotate(count=Count('id')).order_by('-count')[:10]

    data = {}
    total_data = []
    for province_count in province_counts:
        data["name"] = province_count['location']
        data["value"] = province_count['count']
        total_data.append(data)
        data = {}
    # print('total_data', total_data)
    #
    # print(total_data)
    result = {
        "auto_data": total_data
    }
    return JsonResponse(result)

# import json
# from random import randrange
#
# from django.http import HttpResponse
# from rest_framework.views import APIView
#
# from pyecharts.charts import Bar
# from pyecharts import options as opts
#
#
# # Create your views here.
# def response_as_json(data):
#     json_str = json.dumps(data)
#     response = HttpResponse(
#         json_str,
#         content_type="application/json",
#     )
#     response["Access-Control-Allow-Origin"] = "*"
#     return response
#
#
# def json_response(data, code=200):
#     data = {
#         "code": code,
#         "msg": "success",
#         "data": data,
#     }
#     return response_as_json(data)
#
#
# def json_error(error_string="error", code=500, **kwargs):
#     data = {
#         "code": code,
#         "msg": error_string,
#         "data": {}
#     }
#     data.update(kwargs)
#     return response_as_json(data)
#
#
# JsonResponse = json_response
# JsonError = json_error
#
#
# def bar_base() -> Bar:
#     c = (
#         Bar()
#         .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#         .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
#         .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
#         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
#         .dump_options_with_quotes()
#     )
#     return c
#
#
# class ChartView(APIView):
#     def get(self, request, *args, **kwargs):
#         return JsonResponse(json.loads(bar_base()))
#
#
# class IndexView(APIView):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse(content=open("./templates/chart_list.html").read())
