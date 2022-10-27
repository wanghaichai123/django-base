from django.urls import path

from book02.views import index

urlpatterns = [
    # path(路由，视图函数名称)
    path('home/',index)
]