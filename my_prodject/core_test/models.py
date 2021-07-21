from django.db import models
from django.contrib.auth.models import User, update_last_login
from django.utils import timezone


def user_avatar_path(instance, filename):
    return f'user_{instance.user.id}/avatar/{filename}'

def user_directory_path(instance, filename):
    return f'user_{instance.author.id}/post/{filename}'


class Profile(models.Model):
    """Модель профиля для пользователя"""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile'
        )
    birth_date = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True, max_length=500)
    avatar = models.ImageField(upload_to=user_avatar_path)
    

class Posting(models.Model):
    """Объявления пользователя"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to=user_directory_path)
    date_pub = models.DateTimeField(default=timezone.now)
    date_edit = models.DateTimeField(default=timezone.now)

