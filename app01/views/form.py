from django import forms
from django.core.exceptions import ValidationError
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm, BootStrapForm


class UserInfoModelForm(BootStrapModelForm):
    class Meta:
        model = models.User
        fields = ["username", "password", "email","like_province"]



class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )


class UserRegisterModelForm(BootStrapModelForm):

    class Meta:
        model = models.User
        fields = ["username", "password", "email", "like_province"]
        widgets = {
            "password": forms.PasswordInput(render_value=True),
        }

    # def clean_password(self):
    #     pwd = self.cleaned_data["password"]
    #
    #     # 返回什么，此字段保存到数据库就是什么
    #     return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        # confirm = md5(self.cleaned_data.get('confirm_password'))
        confirm = self.cleaned_data.get('confirm_password')
        if pwd != confirm:
            raise ValidationError("两次密码不一致")
        # 返回什么，此字段保存到数据库就是什么
        return confirm


# class UserLoginModelForm(BootStrapModelForm):
#     confirm_password = forms.CharField(
#         label="确认密码",
#         widget=forms.PasswordInput(render_value=True),
#     )
#
#     class Meta:
#         model = models.User
#         fields = ["username", "password", "confirm_password", "email"]
#         widgets = {
#             "password": forms.PasswordInput(render_value=True),
#         }
#
#     def clean_confirm_password(self):
#         pwd = self.cleaned_data.get('password')
#         # confirm = md5(self.cleaned_data.get('confirm_password'))
#         confirm = self.cleaned_data.get('confirm_password')
#         if pwd != confirm:
#             raise ValidationError("两次密码不一致")
#         # 返回什么，此字段保存到数据库就是什么
#         return confirm
