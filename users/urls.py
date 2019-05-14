from django.conf.urls import url
from django.contrib import auth
from django.template.context_processors import static

from kvadra import settings
from users import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    # url(r'^login/(?P<urlname>[=\/]\w+\/\w+\/)/$', views.login, name='login'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^log_out/', views.log_out, name='log_out'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^change_password/', views.change_password, name='change_password'),
    url(r'^rest_password/', views.rest_password, name='rest_password'),
    # url(r'^settings/', views.settings, name='settings'),
    url(r'^guest/', views.guest, name='guest'),
    # url(r'^https://promin.stage.it.loc/ProminShell/oauth/token', views.login, name='login'),
]
