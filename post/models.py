from django.db import models
from main.models import User


class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    work = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    dest_lat = models.CharField(max_length=1000)
    dest_long = models.CharField(max_length=1000)
    source_lat = models.CharField(max_length=100)
    source_long = models.CharField(max_length=1000)
    source_address = models.CharField(max_length=1000)
    dest_address = models.CharField(max_length=1000)
    #s_time = models.CharField(max_length=50,default="hello")#, auto_now=True)
    time = models.CharField(max_length=50)
    payment = models.CharField(max_length=90)
    budget_min = models.CharField(max_length=50)
    budget_max = models.CharField(max_length=50)
    details = models.CharField(max_length=1000)
    image = models.TextField(null=True )
    v_admin = models.BooleanField(default=True)
    near_by = models.CharField(max_length=50,default="0.0")

    def __str__(self):
        return str(self.id) + "-" + str(self.user_id)


class Post_response(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    bid = models.CharField(max_length=50,default="0")
    status = models.CharField(max_length=3,default="0") #0 = waiting ,1 = confirmed , -1= over
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post_id) + "-" + str(self.user_id)

class passbook(models.Model):
    s_id = models.ForeignKey(User, on_delete=models.CASCADE)
    work = models.CharField(max_length=100)
    payment = models.CharField(max_length=7)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)