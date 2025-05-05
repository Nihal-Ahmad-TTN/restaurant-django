from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("ENter Email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is False:
            raise ValueError
        if extra_fields.get('is_superuser') is False:
            raise ValueError
        
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_customer = True
        user.is_manager = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser


class Manager(models.Model):
    manager_name = models.CharField(max_length=100)
    manager_email = models.EmailField(max_length=100)
    manager_city = models.CharField(max_length=50)
    manager_phone = models.IntegerField()
    manager_password = models.CharField(max_length=100)

    def __str__(self):
        return self.manager_name

class Menu(models.Model):
    categories = (
        ('starters', "starters"),
        ('Chinese', "Chinese"),
        ("indian", 'indian'),
        ('snacks', "snacks"),
        ('Dessert', "Dessert"),
        ('Breads', 'Breads'),
        ('south indian', 'south indian'),
        ('main course', "main course"),
    )
    vegetarian = (
        ('Vegetarian', 'Vegetarian'),
        ('Non Vegetarian', 'Non Vegetarian'),
    )
    # food_id = models.CharField(max_length = 10)
    food_name = models.CharField(max_length = 50)
    food_desc = models.CharField(max_length = 200)
    food_category = models.CharField(max_length=50, choices=categories)
    food_type = models.CharField(max_length=20, choices=vegetarian)
    food_price = models.IntegerField(default = 0)
    food_image = models.ImageField(upload_to="media/", default= None)
    food_quantity = models.IntegerField(default=10)


    def __str__(self):
        return self.food_name