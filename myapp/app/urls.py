from django.urls import path,include
from .views import login_user,register_user,User_API,Role_API,Role_View
from .views import User_View

from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'User_View',User_View)
router.register(r'Role_View',Role_View)

urlpatterns=[
    path('register/',register_user,name='register'),
    path('login/',login_user,name='login'),
   path('user/',User_API.as_view()),
   path('role/',Role_API.as_view()),
   path('',include(router.urls))
]


