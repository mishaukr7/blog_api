from django.urls import path, include
from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', views.UserList.as_view()),
    path('accounts/<int:pk>/', views.UserDetail.as_view())
]



