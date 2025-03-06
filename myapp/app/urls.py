from django.urls import path
from .views import login_user,register_user,User_API,Role_API

urlpatterns=[
    path('register/',register_user,name='register'),
    path('login/',login_user,name='login'),
   path('user/',User_API.as_view()),
   path('role/',Role_API.as_view())
]


