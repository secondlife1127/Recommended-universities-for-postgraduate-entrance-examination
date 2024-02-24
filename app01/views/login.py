from django.shortcuts import render, redirect

from app01 import models

from django.utils.safestring import mark_safe

from app01.views.form import LoginForm, UserRegisterModelForm


def login(request):
    """ 登录 """
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    # print(form.cleaned_data)

    # print(form.errors)
    if form.is_valid():
        # 验证成功，获取到的用户名和密码
        # {'username': 'wupeiqi', 'password': '123',"code":123}
        # {'username': 'wupeiqi', 'password': '5e5c3bad7eb35cba3638e145c830c35f',"code":xxx}
        # 验证码的校验
        # user_input_code = form.cleaned_data.pop('code')
        # code = request.session.get('image_code', "")
        # if code.upper() != user_input_code.upper():
        #     form.add_error("code", "验证码错误")
        #     return render(request, 'login.html', {'form': form})

        # 去数据库校验用户名和密码是否正确，获取用户对象、None
        # admin_object = models.Admin.objects.filter(username=xxx, password=xxx).first()
        user_object = models.User.objects.filter(**form.cleaned_data).first()
        # admin_object = models.Admin.objects.filter(username="root").first()
        if not user_object:
            form.add_error("password", "用户名或密码错误")
            # form.add_error("username", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})
        # 用户名和密码正确
        # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
        request.session["info"] = {'id': user_object.id, 'name': user_object.username}
        # # session可以保存7天
        # request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/")
    return render(request, 'login.html', {'form': form})


def logout(request):
    """注销"""
    request.session.clear()
    return redirect("/")


def register(request):
    """注册"""

    if request.method == 'GET':
        # print("Register")
        form = UserRegisterModelForm()
        # print(form.cleaned_data)

        context = {
            # "title": "用户注册",
            "form": form,
        }
        return render(request, 'register.html', context)

    form = UserRegisterModelForm(data=request.POST)
    context = {
        # "title": "用户注册",
        "form": form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/login')
    # 校验失败
    print(form.cleaned_data)

    return render(request, 'register.html', context)