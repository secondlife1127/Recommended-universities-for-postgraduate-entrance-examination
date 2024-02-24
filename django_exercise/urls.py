"""django_exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01.views import echarts, informationSearch, login, recommend, user, test

urlpatterns = [

    #测试功能

    # 随机推荐
    # path('recommend_random/', recommend.recommend_random, name='recommend_random'),

    # 基于用户的协同过滤
    path('recommend_user/<int:alpha>/', recommend.user_based_recommend, name='recommend_user'),
    # 基于物品的协同过滤
    # path('recommend_item/', recommend.item_based_recommend, name='recommend_item'),
    # 用户对学校进行评分
    path('user/score/<int:school_id>/', user.user_score),
    # 后台管理
    path('admin/', admin.site.urls),
    # 用户收藏
    path('user/collection/', user.user_collection),
    # 用户取消收藏
    path('collection/delete/<int:school_id>/', user.collection_delete),
    # 用户收藏显示
    path('collection/list/', user.collection_list),
    # 用户评分显示
    path('score/list/', user.score_list),
    # 删除用户评分
    path('score/delete/<int:school_id>', user.score_delete),

    # 首页

    # 院校信息显示
    path("school/list/", informationSearch.school_list),
    #院校信息按地区筛选
    # path("school/list/<str:location>", informationSearch.school_list_filter),
    # 专业数据显示
    path("special/list/", informationSearch.special_list),

    # 分数线信息显示
    path("scoreline/list/", informationSearch.scoreline_list),
    # 报录比数据显示
    path("rate/list/", informationSearch.rate_list),

    # 数据可视化页面显示
    path("chart/list/", echarts.chart_list),

    # 院校收藏榜数据提交
    path("chart/school_collection/", echarts.school_collection),
    # 院校评分榜数据提交
    path("chart/school_score/", echarts.school_score),
    #全国各省市院校数量数据提交
    path("chart/total_school/",echarts.total_school),
    #全国各省市双一流院校数量提交
    path("chart/double_school/",echarts.double_school),
    # 全国各省市自划线院校数量提交
    path("chart/auto_school/",echarts.auto_school),
    #全国各省市院校数量对比
    # path("chart/count_school/",echarts.count_school),
    # 用户信息页面
    path('user/info/', user.user_info),
    # 注册
    path('register/', login.register),
    # 登录
    path('login/', login.login),
    # 注销
    path('logout/', login.logout),
    path('', informationSearch.index),

]
