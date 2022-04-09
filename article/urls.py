from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('', views.articles, name="articls_list"),
    path('/<str:slug>', views.single_article, name="single_article")
]
