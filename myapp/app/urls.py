from django.urls import path,include
from .views import login_user,register_user,User_API,Role_API,Role_View,User_Model_View
from .views import User_View

from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'User_View',User_View)
router.register(r'Role_View',Role_View)
# router.register(r'usermodel',User_Model_View)

router2=routers.DefaultRouter()
router2.register(r'model_user',User_Model_View)


urlpatterns=[
    path('register/',register_user,name='register'),
    path('login/',login_user,name='login'),
   path('user/',User_API.as_view()),
   path('role/',Role_API.as_view()),
   path('',include(router.urls)),
   path('',include(router2.urls))

]


