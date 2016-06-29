
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from todo import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^api/todos/$', views.TodoListAPIView.as_view(), name='todos_list_api_view'),
    url(r'^api/todos/(?P<pk>\d+)$', views.TodoDetailAPIView.as_view(), name='todos_detail_api_view'),

]
