from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, render


# 判断是否登录中间件

class AuthMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        #     if request.user.username:
        #         # 登陆成功
        #         print(self.__dict__)
        #         return None
        #     else:
        #         return redirect("/login/")

        # 设置白名单
        print(request.path)
        if request.path in ["/login/"]:
            return None

        if not request.user.username:
            return redirect("/login/")
