from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/', views.ArticleList.as_view()),
    path('posts/<slug:name>/', views.ArticleDetail.as_view())
]
