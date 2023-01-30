from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db import models
from mptt.models import MPTTModel
# Create your models here.
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(max_length=55)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

class Product(models.Model):
    class ChoiceSize(models.TextChoices):
        XS = 'XS'
        X = 'X'
        M = 'M'
        L = 'L'
        XL = 'XL'

    class ChoiceColor(models.TextChoices):
        BLACK = 'Black'
        WHITE = 'White'
        RED = 'Red'
        BLUE = 'Blue'
        GREEN = 'Green'
        GREY = 'GREY'
        YELLOW = 'YELLOW'



    image = models.ImageField(upload_to='product')
    title = models.CharField(max_length=155)
    text = models.TextField()
    size = models.CharField(max_length=155, choices=ChoiceSize.choices, default=ChoiceSize.M)
    color = models.CharField(max_length=155, choices=ChoiceColor.choices, default=ChoiceColor.WHITE)
    quantity = models.IntegerField(default=1)
    rivew = models.IntegerField(default=1)
    price = models.FloatField()
    category = models.ForeignKey('app.Category', on_delete=models.CASCADE)

class Women(Product):
    class ChoiceColor(models.TextChoices):
        TOMATO = 'TOMATO'

class Men(Women):
    class ChoiceColor(models.TextChoices):
        BROWN = 'BROWN'


class UserManager(BaseUserManager):

    def create_user(self,email, password=None,  **kwargs):
        if not email:
            raise ValueError('email not found')
        user = self.model(email=email,  **kwargs)
        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self,email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=155, unique=False)
    phone_number = models.CharField(max_length=13, validators=[integer_validator])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

class Contact(models.Model):
    username = models.CharField(max_length=155, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
