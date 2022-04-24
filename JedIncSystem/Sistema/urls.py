from django.urls import re_path
from Sistema import views

urlpatterns=[
    re_path(r'^projeto/$', views.Projeto.as_view()),
    re_path(r'^projeto/(?P<pk>[0-9]+)/$', views.Projeto.as_view())
]