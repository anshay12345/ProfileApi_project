from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    # way of working of the the manager is to specify some functions in the manager model that can manipulate
    # the objects of the model UserProfile
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)  # it will make the second half part of the email case insensitive
        user = self.model(email=email, name=name)  # this will create new profile object

        user.set_password(password)  # set_password function convert the password in the database to a hash
        user.save(using=self._db)  # saving the user in the database

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new user with the given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for the user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
