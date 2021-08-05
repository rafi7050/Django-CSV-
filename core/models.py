from django.db import models



class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    profile_picture = models.ImageField(upload_to=None,default="./static/images/avatar.png", blank=True, verbose_name="Profile Picture")
    email = models.EmailField(unique=True,verbose_name="Email")
    phone_number = models.TextField(max_length=11, verbose_name="Phone Number")
    room_number = models.TextField(max_length=25, verbose_name="Room Number")
    Subject_1 = models.TextField(max_length=100,blank=True, verbose_name="Subject_1")
    Subject_2 = models.TextField(max_length=100,blank=True, verbose_name="Subject_2")
    Subject_3 = models.TextField(max_length=100,blank=True, verbose_name="Subject_3")
    Subject_4 = models.TextField(max_length=100,blank=True, verbose_name="Subject_4")
    Subject_5 = models.TextField(max_length=100,blank=True, verbose_name="Subject_5")

    def __str__(self):
        return self.first_name
    
class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(Self):
        return f"File id: {Self.id}"
