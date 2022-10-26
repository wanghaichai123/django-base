from book.views import index
from django.urls import path
urlpatterns=[
    # path(路由，视图函数名称)
    path('index/',index)
]