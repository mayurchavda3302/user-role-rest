from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializers import CustomUserSerializer,UserSerializer,RoleSerializer,UserResponseSerializer
from .models import CustomUser,Role,User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def register_user(request):
    if request.method == "POST":
        serializer=CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def login_user(request):
    if request.method == "POST":
        username=request.data.get('username')
        password=request.data.get('password')
        user=None
        
        if  '@' in username:
            try:
                user=CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass
        # serializer=CustomUserSerializer(data=request.data)

        if not user:
            user=authenticate(username=username,password=password)

        if user:
            token,__=Token.objects.get_or_create(user=user)
            return Response({"Token":token.key},status=status.HTTP_200_OK)
        return Response({"Message":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)

class User_API(APIView):
   def get(self,request):
      search = request.GET.get('search')
      objs=User.objects.all()
      if search:
            objs = objs.filter(first_name__startswith=search)  
      serialization=UserResponseSerializer(objs,many=True)
      return Response(serialization.data)
   
   def post(self,request):
      data=request.data
      serialization=UserSerializer(data=data)
      if serialization.is_valid():
         serialization.save()
         return Response(serialization.data)
      return Response(serialization.errors)
   
   def patch(self,request):
      data=request.data
      obj=User.objects.get(id=data['id'])
      serialization=UserSerializer(obj,data=data,partial=True)
      if serialization.is_valid():
         serialization.save()
         return Response(serialization.data)
      return Response(serialization.errors)
   
   def put(self,request):
      data= request.data
      obj=User.objects.get(id=data["id"])
      serialization=UserSerializer(obj,data=data)
      if serialization.is_valid():
         serialization.save()
         return Response({"data" :serialization.data})
      return Response(serialization.errors)
      

   def delete(self,request):
      data=request.data
      obj=User.objects.get(id=data['id'])
      # if 
      User_id=data['id']
      obj.delete()
      return Response({"Message" :f"Userid  :- {User_id} Got deleted "})

   
class Role_API(APIView):
   def get(self,request):
      obj=Role.objects.all()
      Serializer=RoleSerializer(obj,many=True)
      return Response(Serializer.data)
   
   def post(self,request):
      data=request.data
      Serializer=RoleSerializer(data=data)
      if Serializer.is_valid():
         Serializer.save()
         return Response(Serializer.data)
      return Response(Serializer.errors)
   
   def patch(self,request):
      data=request.data
      obj=Role.objects.get(id=data['id'])
      serialization=RoleSerializer(obj,data=data,partial=True)
      if serialization.is_valid():
         serialization.save()
         return Response(serialization.data)
      return Response(serialization.errors)
   
   
   def delete(self,request):
      data=request.data
      obj=Role.objects.get(id=data['id'])
      role_id=data['id']
      obj.delete()
      return Response({"Message" :f" Role_id :- {role_id} Got deleted "})


