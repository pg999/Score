from rest_framework import serializers
from .models import Post , Post_response, passbook

content = [
    {
        'error': 0,
        'response': 'success',
        'id':0
    }
]
error = [
    {
        'error': 1,
        'response': 'fail',
        'id':0
    }
]


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        # fields = ('user_id', 'title','summary', 'budget', 'loc', 's_time', 'e_time', 'about', 'v_admin')
        fields = '__all__'


class PostuserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        # fields = ('user_id', 'title','summary', 'budget', 'loc', 's_time', 'e_time', 'about', 'v_admin')
        fields = ('id','work','category','image')


class Post_responseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post_response
        fields = '__all__'

class PassbookSerializer(serializers.ModelSerializer):

    class Meta:
        model = passbook
        fields = '__all__'