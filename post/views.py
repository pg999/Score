from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer, Post_responseSerializer, PostuserSerializer, PassbookSerializer
from .models import Post_response, Post, passbook
from rest_framework.decorators import api_view
import simplejson
from main.models import userlocation, User
from main import views
import urllib.request as url

api = "AIzaSyCcV586wIJsNgTkKpAI5pGM0xR6wwNom-I"

content = [
    {
        'error': 0,
        'response': 'success',
        'email': 'null'
    }
]

error = [
    {
        'error': 1,
        'response': 'fail',
        'email': 'null'
    }
]


# to post work and to see all work
class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        p_serializer = PostSerializer(posts, many=True)
        c = p_serializer.data
        for p in c:
            usr = User.objects.get(pk=p['user_id'])
            p['usr_image'] = usr.image
        return Response(p_serializer.data)

    def post(self, request):
        p_serializer = PostSerializer(data=request.data)
        if p_serializer.is_valid():
            p_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# to customize a posted work by a particular user
class Post_UserIdList(APIView):
    def get_object(self, user_id, pk):
        return Post.objects.get(user_id=user_id, pk=pk)

    def get(self, request, user_id, pk, format=None):
        posts = self.get_object(user_id, pk)
        p_serializer = PostSerializer(posts)
        return Response(p_serializer.data)

    def put(self, request, user_id, pk, format=None):
        posts = self.get_object(user_id, pk)
        p_serializer = PostSerializer(posts, data=request.data)
        if p_serializer.is_valid():
            p_serializer.save()
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# to show all the posted work of particular user
class Post_UserList(APIView):
    def get_object(self, user_id):
        return Post.objects.filter(user_id=user_id)

    def get(self, request, user_id):
        posts = self.get_object(user_id)
        p_serializer = PostuserSerializer(posts, many=True)
        return Response(p_serializer.data)


# to check the nearby works to a particular user
class PostLocationList(APIView):
    def get_object(self, user):
        return userlocation.objects.get(user_id=user)

    def get(self, request, pk):
        nearby(pk)
        posts = Post.objects.all()
        p_serializer = PostSerializer(posts, many=True)
        return Response(p_serializer.data)

    def post(self, request):
        pass


# to show all the bid on a particular post
class Post_responseList(APIView):
    def get_object(self, post_id):
        return Post_response.objects.filter(post_id=post_id)

    def get_object_id(self, pk):
        return Post.objects.filter(pk=pk)

    def get(self, request, post_id):
        postresponses = self.get_object(post_id)
        posts = self.get_object_id(post_id)
        p_r_serializer = Post_responseSerializer(postresponses, many=True)
        p_serializer = PostSerializer(posts, many=True)
        p = p_r_serializer.data
        for c in p:
            u_r_id = c['user_id']
            usr = User.objects.get(pk=u_r_id)
            c['name'] = usr.name
            c['image'] = usr.image
        response = p_serializer.data + p_r_serializer.data
        return Response(response)

    def post(self, request, post_id):
        p_serializer = Post_responseSerializer(data=request.data)
        value = request.data
        posts = Post.objects.get(pk=post_id)
        user = User.objects.get(pk=posts.user_id.id)
        bid = value['bid']
        if p_serializer.is_valid():
            p_serializer.save()
            message = "Someone is willing to do your job in " + bid
            title = "See Your Post"
            registration_id = "eTEQy-1jPgQ:APA91bE5krR2rhn85VnFyL6lApGwcm0A81_G1yoMiGVUgPR1nW7KddDS4JmoSaWCuLxBmQY9cY2WuMSMxLkbp9SZTlg2KUP_oSb0HyqsjPhLm4OM9xMTJj9OzbCr_48scLr4tuBruMTB"
            views.notifications(title, message, registration_id)
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


# all the post which is bid by user
class Response_postList(APIView):
    def get_object_id(self, pk):
        return Post_response.objects.filter(user_id=pk)

    def get(self, request, user_id):
        response = []
        z = 0
        posts = self.get_object_id(user_id)
        p_serializer = Post_responseSerializer(posts, many=True)
        p = p_serializer.data
        for c in p:
            work = c['post_id']
            w = Post.objects.filter(pk=work)
            r_p = PostSerializer(w, many=True)
            post = r_p.data
            post[0]['status'] = c['status']
            post[0]['bid'] = c['bid']
            response = response + post
        return Response(response)


class Status(APIView):
    def get_object(self, res_id):
        return Post_response.objects.get(pk=res_id)

    def get(self, request, res_id):
        postresponses = self.get_object(res_id)
        p_r_serializer = Post_responseSerializer(postresponses)
        return Response(p_r_serializer.data)

    def patch(self, request, res_id, foramt=None):
        postresponses = self.get_object(res_id)
        p_r_serializer = Post_responseSerializer(postresponses, data=request.data, partial=True)
        if p_r_serializer.is_valid():
            p_r_serializer.save()
            # payment(p_r_serializer.data)
            # message = "confirmed"
            # title = "BID"
            # registration_id = "eKP9SVRi2A4:APA91bEvqw4lI4pLXy1trXH6OtuWDdWJ6n7CKraQHB7nLjXbpzf_Ac8z3AVEtdUXePprNI2f-H2ZX3ZUfkV3ZwEtfQgQvCBtSmdWmbHXbLk8-YTx4DWUFeLzdf0SBvjiqIdwsqQP-IGQ"
            # views.notifications(title, message, registration_id)
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

class passbookList(APIView):
    def get_object(self,user_id):
        return passbook.objects.filter(s_id = user_id)

    def get(self,request,user_id):
        payments = self.get_object(user_id)
        user = User.objects.get(pk = user_id)
        credits = user.credits
        serializer = PassbookSerializer(payments,many= True)
        response = [{"credits":credits}]+serializer.data
        return Response(response)

    def post(self,request):
        pass

def nearby(users):
    user = userlocation.objects.get(user_id=users)
    posts = Post.objects.all()
    origin_lat = user.latitude
    origin_long = user.longitude
    for p in posts:
        dest_lat = p.dest_lat
        dest_long = p.dest_long
        origin = origin_lat + "," + origin_long
        dest = dest_lat + "," + dest_long
        url_request = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(
            origin, dest)
        result = url.urlopen(url_request)
        rr = simplejson.load(result)
        p.near_by = rr['rows'][0]['elements'][0]['distance']['text']
        p.save()


@api_view(['GET','POST'])
def payment(request, res_id, format = None):

    if request.method == 'GET':
        pst = Post_response.objects.get(pk=res_id)
        p_r_serializer = Post_responseSerializer(pst)
        post = p_r_serializer.data
        if int(post['status']) != 1:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        post_id = post['post_id']
        user_id = post['user_id']
        p = Post.objects.get(pk=post_id)
        u_r = User.objects.get(pk=user_id)
        u_s = User.objects.get(pk=p.user_id.id)
        bid = post['bid']
        u_r.credits = str(int(u_r.credits) + int(bid))
        u_s.credits = str(int(u_s.credits) - int(bid))
        u_r.save()
        u_s.save()
        a = passbook(s_id = p.user_id, work = p.work,payment = bid, name = u_r.name)
        a.save()
        p.delete()
        return Response(content, status=status.HTTP_201_CREATED)

    if request.method == 'POST':
        pass

# @api_view(['GET'])
# def passbook(request,):
#     pass