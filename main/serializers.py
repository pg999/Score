from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from .models import User, userlocation

content = [
    {
        'error': 0,
        'response': 'success',
        'id': 0
    }
]
error = [
    {
        'error': 1,
        'response': 'fail',
        'id': 0
    }
]


class SignupSerializer(serializers.ModelSerializer):


    def validate(self,data):
        temp = make_password(data['password'], salt = None, hasher = 'default')
        data['password'] = temp
        return data

    class Meta:
        model = User
        fields = ('name', 'password', 'mobile_no', 'email', 'gender', 'dob')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'mobile_no', 'email', 'gender', 'dob','credits','image')


class userlocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = userlocation
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):


    def xyz(self,data):
        content[0]['id'] = 0
        x = User.objects.filter(email=data['email'])
        if x:
            temp = User.objects.get(email = data['email'])
            if check_password(data['password'], temp.password):
                content[0]['id'] = temp.id
        return content

    class Meta:
        model = User
        fields = ('email', 'password')


class EmailSerializer(serializers.ModelSerializer):
    def xyz(self, data):
        content[0]['id'] = 0
        temp = User.objects.filter(email=data['email'])
        if temp:
             content[0]['id'] = temp[0].id
        return content
    class Meta:
        model = User
        fields = ('email',)

class ResetSerializer(serializers.ModelSerializer):

    def xyz(self, data):
        content[0]['id'] = 0
        x = User.objects.filter(id= data['id']).update(password = make_password(data['password']))
        if x:
            content[0]['id'] =  User.objects.get(id = data['id']).id

        return content
    class Meta:
        model = User
        fields = ('id','password')
