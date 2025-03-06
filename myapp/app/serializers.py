from rest_framework import serializers
from .models import CustomUser,Role,User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
       model=CustomUser
       fields = ['username', 'email', 'password']
       extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user=CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class  RoleRespondeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields=['role_name','access_modules']
    

class  UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model=User
        fields='__all__'
        
        
class  UserResponseSerializer(serializers.ModelSerializer):
    role=RoleRespondeSerializer()
    class Meta: 
        model=User
        exclude= ['password']
        # fields='__all__'



class  RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'
    