from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from PIL import Image


class UserAccountManager(BaseUserManager):
    def create_user(self, email, full_name, phone, address, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not full_name:
            raise ValueError('Enter your full name')
        if not phone:
            raise ValueError('Enter a working phone number')
        if not address:
            raise ValueError('Enter your current address')

        user  = self.model(
                email=self.normalize_email(email),
                full_name=full_name,
                phone=phone,
                address=address
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, phone, address, password):
        user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                full_name=full_name,
                phone=phone,
                address=address
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser):

    # personal_information

    email                   = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    full_name               = models.CharField(verbose_name='full Name', max_length=20, unique=True)
    phone                   = models.CharField(verbose_name="Mobile Number", max_length=14)
    phone2                  = models.CharField(verbose_name='Alternate Number', max_length=14, blank=True)

    # Location

    address                 = models.CharField(verbose_name='Address', max_length=60, null=True)

    # required_variables

    date_joined             = models.DateField(verbose_name='Date Joined', auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)

    USERNAME_FIELD          = 'email'
    REQUIRED_FIELDS         = ['full_name', 'phone', 'address',]

    objects = UserAccountManager()

    def __str__(self):
        return self.full_name + ' | ' + self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    brand_name = models.CharField(verbose_name='Brand Name', max_length=20)
    about_brand = models.TextField(verbose_name='About us', max_length=200)

    def __str__(self):
        return f'(self.user.full_name) Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


