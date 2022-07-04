# from django.db.models.signals import post_save
# from django.conf import settings
# from django.dispatch import receiver
# from .models import Profile

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(get_user_model=instance)


# @receiver(post_save, sender=get_user_model())
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()



from django.conf import settings
from django.db.models.signals import post_save
from .models import Profile
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)

