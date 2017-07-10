from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    # AbstractBaseUser를 상속받아 CustomUser만들기
    pass
