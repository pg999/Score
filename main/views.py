# from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, userlocation
from .serializers import SignupSerializer, LoginSerializer, EmailSerializer, ResetSerializer, userlocationSerializer,\
     UserSerializer
import json
import requests
from django.conf import settings
from post import models, views
# from django.shortcuts import render
# from django.http import HttpResponse

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

class SignupList(APIView):

    def get(self, request):
        # users = self.get_object(pk)
        users = User.objects.all()
        u_serializer = SignupSerializer(users,many=True)
        # views.notifications()
        return Response(u_serializer.data)

    def post(self, request):
        u_serializer = SignupSerializer(data=request.data)

        if u_serializer.is_valid():
            u_serializer.save()
            usr = User.objects.get(email = u_serializer.data['email'])
            a = userlocation(user_id =usr,latitude='0.0',longitude='0.0')
            a.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):

    def get_object(self, pk):
        return User.objects.get(pk=pk)

    def get(self, request, pk, format = None):
        users = self.get_object(pk)
        # users = User.objects.all()
        response = []
        u_serializer = UserSerializer(users)
        # views.notifications()
        response.insert(0,u_serializer.data)
        return Response(response)

    def patch(self, request, pk):
        users = self.get_object(pk)
        u_serializer = UserSerializer(users,data=request.data,partial=True)
        if u_serializer.is_valid():
            u_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    # def put(self,request,pk,format=None):
    #     users = self.get_object(pk)
    #     u_serializer = UserSerializer(users,data=request.data)
    #     if u_serializer.is_valid():
    #         u_serializer.save()
    #         return Response(content, status=status.HTTP_201_CREATED)
    #     return Response(error, status=status.HTTP_400_BAD_REQUEST)



class UserLocationList(APIView):


    def get_object(self, user_id):
        return userlocation.objects.get(user_id = user_id)

    def get(self, request, user_id , format = None):
        userlocations = self.get_object(user_id)
        ul_serializer = userlocationSerializer(userlocations)
        return Response(ul_serializer.data)

    def put(self, request, user_id , format = None):
        userlocations = self.get_object(user_id)
        ul_serializer = userlocationSerializer(userlocations,data=request.data)
        if ul_serializer.is_valid():
            ul_serializer.save()
        views.nearby(user_id)
        posts = models.Post.objects.all()
        ctr = 0
        for p in posts:
            if p.near_by != "0.0 km":
                ctr += 1

        title = "Works Near You!!"
        message = "You have " + str(ctr) + " works near you"
        registration_id = "eTEQy-1jPgQ:APA91bE5krR2rhn85VnFyL6lApGwcm0A81_G1yoMiGVUgPR1nW7KddDS4JmoSaWCuLxBmQY9cY2WuMSMxLkbp9SZTlg2KUP_oSb0HyqsjPhLm4OM9xMTJj9OzbCr_48scLr4tuBruMTB"
        notifications(title,message,registration_id)
        return Response(content, status=status.HTTP_201_CREATED)
        # return Response(error, status=status.HTTP_400_BAD_REQUEST)




class LoginList(APIView):


    def get(self, request):
        return Response()

    def post(self, request):
        l = LoginSerializer(data=request.data)
        content = l.xyz(data=request.data)
        if content[0]['id'] != 0:
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class EmailList(APIView):

    def get(self, request):
        ls = User.objects.all()
        l = EmailSerializer(ls, many=True)
        return Response(l.data)

    def post(self, request):
        l = EmailSerializer(data=request.data)
        content = l.xyz(data=request.data)
        if content[0]['id'] != 0:
            return Response(content, status=status.HTTP_200_OK)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class ResetList(APIView):


    def get(self, request):
        ls = User.objects.all()
        l = ResetSerializer(ls, many=True)
        return Response(l.data)

    def post(self, request):
        l = ResetSerializer(data=request.data)
        content = l.xyz(data = request.data)
        if content[0]['id'] != 0:
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


def notifications(title, message, registration_id):

    registration_id = registration_id
    post_data = dict(to=registration_id,
                     priority='high',
                     notification=dict(
                         title=title,
                         text=message,
                         click_action='OPEN_ACTIVITY_NOTIFICATIONS',
                         sound='default',
                        )
                     )
    json_data = json.dumps(post_data)
    headers = {
        'UserAgent': "FCM-Server",
        'Content-Type': 'application/json',
        'Authorization': 'key = AIzaSyB2yZ5PZLJtIyWIV8JEn709uHk1RK8fqsk'
    }

    response = requests.post(
        data=json_data,
        url=settings.PUSH_NOTIFICATIONS_SETTINGS['GCM_POST_URL'], headers=headers)

    response.raise_for_status()
