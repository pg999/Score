from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.TextField()
    mobile_no = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=10)
    reg_time = models.DateTimeField(auto_now_add=True, blank=True)
    registration_id = models.CharField(max_length=2000,default="Null")
    credits = models.CharField(max_length=7,default="50")
    image = models.TextField(default="none")
    dob = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class userlocation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user_id)
