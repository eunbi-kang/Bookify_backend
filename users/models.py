from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True, unique=True)
    profile_image = models.ImageField(upload_to="profile/", null=True, blank=True)  # ✅ 이미지 필드 추가
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
