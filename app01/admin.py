# Register your models here.
from django.contrib import admin
from app01.models import School, Rate, Special, ScoreLine, User, UserScore, UserCollection


# app01/admin.py:
class SchoolAdmin(admin.ModelAdmin):
    # 指定后台网页要显示的字段
    list_display = ["id", "name", "location", "department", "is_research", "is_auto_line", "is_double_one", "icon",
                    "url"]


class SpecialAdmin(admin.ModelAdmin):
    # 指定后台网页要显示的字段
    list_display = ["id", "code", "name", "subject", "first_subject", "type"]


class RateAdmin(admin.ModelAdmin):
    list_display = ["id", "year", "school", "department", "code", "name", "count", "record", "rate"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "password", "email", "created_time"]


class ScoreLineAdmin(admin.ModelAdmin):
    list_display = ["id", "year", "school", "department", "code", "name", "total_score", "politics", "english",
                    "subject_three", "subject_four"]


class UserScoreAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "school", "score","score_time"]


class UserCollectionAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "school", "collection","collection_time"]


admin.site.register(School, SchoolAdmin)
admin.site.register(Special, SpecialAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(ScoreLine, ScoreLineAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserScore, UserScoreAdmin)
admin.site.register(UserCollection, UserCollectionAdmin)
admin.AdminSite.site_header = '考研院校推荐系统后台'
admin.AdminSite.site_title = '考研院校推荐系统后台'
