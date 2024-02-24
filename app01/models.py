# Create your models here.
from django.db import models
from django.utils import timezone


# 表结构设计
# 院校表
class School(models.Model):
    name = models.CharField(verbose_name="院校名称", max_length=32, null=True)
    location = models.CharField(verbose_name="所在地", max_length=32, null=True)
    department = models.CharField(verbose_name="院校隶属", max_length=32, null=True)
    department_choices = (

        (1, "研究生院"),
        (0, " ")
    )
    is_research = models.BooleanField(verbose_name="是否有研究生院", choices=department_choices, max_length=32,
                                      null=True)
    line_choices = (

        (1, "自划线"),
        (0, " ")
    )
    is_auto_line = models.BooleanField(verbose_name="是否为自划线院校", choices=line_choices, max_length=32, null=True)
    double_choices = (
        (1, "双一流"),
        (0, " ")
    )
    is_double_one = models.BooleanField(verbose_name="是否为双一流院校", choices=double_choices, max_length=32,
                                        null=True)
    icon = models.CharField(verbose_name="图标链接", max_length=255, default='')
    url = models.CharField(verbose_name="院校链接", max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "院校"
        verbose_name_plural = verbose_name


# 专业表
class Special(models.Model):
    # 专业代码
    code = models.CharField(verbose_name="专业代码", max_length=32, null=True)
    # 专业名称
    name = models.CharField(verbose_name="专业名称", max_length=32, null=True)
    # 所属学科门类
    subject = models.CharField(verbose_name="所属学科门类", max_length=32, null=True)
    # 所属一级学科
    first_subject = models.CharField(verbose_name="所属一级学科", max_length=32, null=True)
    # 专业类型
    type = models.CharField(verbose_name="专业类型", max_length=32, null=True)

    class Meta:
        verbose_name = "专业"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 分数线表
class ScoreLine(models.Model):
    # 招生年份
    year = models.CharField(verbose_name="招生年份", max_length=32, null=True)
    # 院校名称
    school = models.CharField(verbose_name="院校名称", max_length=32, null=True)
    # 院系
    department = models.CharField(verbose_name="院系", max_length=64, null=True)
    # 专业代码
    code = models.CharField(verbose_name="专业代码", max_length=32, null=True)
    # 专业名称
    name = models.CharField(verbose_name="专业名称", max_length=64, null=True)
    # 总分
    total_score = models.IntegerField(verbose_name="总分", null=True)
    # 政治
    politics = models.IntegerField(verbose_name="政治", null=True)
    # 外语
    english = models.IntegerField(verbose_name="外语", null=True)
    # 科目三
    subject_three = models.IntegerField(verbose_name="科目三", null=True)
    # 科目四
    subject_four = models.IntegerField(verbose_name="科目四", null=True)

    class Meta:
        verbose_name = "分数线"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.year, self.school, self.department, self.code, self.name


# 报录比表
class Rate(models.Model):
    # 招生年份
    year = models.CharField(verbose_name="招生年份", max_length=32, null=True)
    # 院校名称
    school = models.CharField(verbose_name="院校名称", max_length=32, null=True)
    # 院系
    department = models.CharField(verbose_name="院系", max_length=32, null=True)
    # 专业代码
    code = models.CharField(verbose_name="专业代码", max_length=32, null=True)
    # 专业名称
    name = models.CharField(verbose_name="专业名称", max_length=32, null=True)
    # 报考人数
    count = models.IntegerField(verbose_name="报考人数", null=True)
    # 录取人数
    record = models.IntegerField(verbose_name="录取人数", null=True)
    # 报录比
    rate = models.DecimalField(verbose_name="报录比", max_digits=10, decimal_places=2, default=0, null=True)

    def __str__(self):
        return self.year, self.school, self.department, self.code, self.name

    class Meta:
        verbose_name = "报录比"
        verbose_name_plural = verbose_name


# 用户表
class User(models.Model):
    username = models.CharField(max_length=255, unique=True, verbose_name="账号", null=True)
    password = models.CharField(max_length=255, verbose_name="密码", null=True)
    email = models.EmailField(verbose_name="邮箱", null=True)
    PROVINCE_CHOICES = (
        ('anhui', '安徽'),
        ('beijing', '北京'),
        ('chongqing', '重庆'),
        ('fujian', '福建'),
        ('gansu', '甘肃'),
        ('guangdong', '广东'),
        ('guangxi', '广西'),
        ('guizhou', '贵州'),
        ('hainan', '海南'),
        ('hebei', '河北'),
        ('heilongjiang', '黑龙江'),
        ('henan', '河南'),
        ('hubei', '湖北'),
        ('hunan', '湖南'),
        ('jiangsu', '江苏'),
        ('jiangxi', '江西'),
        ('jilin', '吉林'),
        ('liaoning', '辽宁'),
        ('neimenggu', '内蒙古'),
        ('ningxia', '宁夏'),
        ('qinghai', '青海'),
        ('shandong', '山东'),
        ('shanxi', '山西'),
        ('shanxi1', '陕西'),
        ('shanghai', '上海'),
        ('sichuan', '四川'),
        ('tianjin', '天津'),
        ('xinjiang', '新疆'),
        ('xizang', '西藏'),
        ('yunnan', '云南'),
        ('zhejiang', '浙江'),
    )

    like_province = models.CharField(verbose_name="用户意向地区", max_length=255,choices=PROVINCE_CHOICES,blank=True)

    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        verbose_name_plural = "用户"
        verbose_name = "用户"

    def __str__(self):
        return self.username


# 用户评分表
class UserScore(models.Model):
    user = models.ForeignKey(
        to='User', on_delete=models.CASCADE, blank=True, verbose_name="用户", related_name="userscores"
    )
    # 学校id
    school = models.ForeignKey(
        to="School", on_delete=models.CASCADE, blank=True, verbose_name="学校", related_name='schoolscores'
    )

    # 用户评分
    score = models.FloatField(verbose_name="评分", default=0)

    # 评分时间
    score_time = models.DateTimeField(verbose_name="评分时间",
                                      default=timezone.now
                                      )

    class Meta:
        verbose_name = "用户评分"
        verbose_name_plural = "用户评分"


# 用户收藏表
class UserCollection(models.Model):
    user = models.ForeignKey(
        to='User', on_delete=models.CASCADE, blank=True, verbose_name="用户", related_name="usercollections"
    )
    # 学校id
    school = models.ForeignKey(
        to="School", on_delete=models.CASCADE, blank=True, verbose_name="学校", related_name='schoolcollections'
    )

    # 是否收藏
    collection_choices = (
        (0, "点击收藏"),
        (1, "取消收藏")
    )
    # 用户是否收藏
    collection = models.BooleanField(
        verbose_name="用户收藏", choices=collection_choices, default=False
    )

    # 收藏时间
    collection_time = models.DateTimeField(verbose_name="收藏时间",
                                           default=timezone.now
                                           )

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = "用户收藏"





