from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from main import views
from post.views import Post_responseList, PostList, PostLocationList, Post_UserIdList, Post_UserList, Status\
    , Response_postList, payment,passbookList

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^user/$', views.SignupList.as_view()),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.UserList.as_view()),
    url(r'^login/$', views.LoginList.as_view()),
    url(r'^email/$', views.EmailList.as_view()),
    url(r'^reset/$', views.ResetList.as_view()),
    url(r'^post/$', PostList.as_view()),
    url(r'^postuserid/(?P<user_id>[0-9]+)/(?P<pk>[0-9]+)/$', Post_UserIdList.as_view()),
    url(r'^post_response/(?P<post_id>[0-9]+)/$', Post_responseList.as_view()),
    url(r'^response_post/(?P<user_id>[0-9]+)/$', Response_postList.as_view()),
    url(r'^userlocation/(?P<user_id>[0-9]+)/$', views.UserLocationList.as_view()),
    url(r'^nearby/(?P<pk>[0-9]+)/$', PostLocationList.as_view()),
    url(r'^postuser/(?P<user_id>[0-9]+)/$', Post_UserList.as_view()),
    url(r'^passbook/(?P<user_id>[0-9]+)/$', passbookList.as_view()),
    # url(r'^notification/(?P<title>[A-Za-z]+)/(?P<message>[A-Za-z]+)/(?P<resgistration_id>[A-Za-z]+)/$', views.notifications),
    url(r'^status/(?P<res_id>[0-9]+)/$', Status.as_view()),
    url(r'^payment/(?P<res_id>[0-9]+)/$', payment),
)

urlpatterns = format_suffix_patterns(urlpatterns)
