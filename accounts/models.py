from django.db import models
from django.contrib.auth.models import User
# Create your models here.


def user_directory_path(instance, filename):
    # ফাইলটি 'user_<username>/<filename>' এই ফরম্যাটে সেভ হবে
    # উদাহরণ: user_shuvo/my_photo.jpg
    return 'profile_pics/user_{0}/{1}'.format(instance.user.username, filename)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='prof_user')
    bio=models.TextField(blank=True)
    avater=models.ImageField(default='default.jpg', upload_to=user_directory_path)
    dob=models.DateField(blank=True,null=True)
    profession=models.CharField(default='blogger',null=True,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'