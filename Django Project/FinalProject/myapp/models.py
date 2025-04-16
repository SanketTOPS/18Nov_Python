from django.db import models

# Create your models here.


class userSignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    password = models.CharField(max_length=12)
    state = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    photo = models.ImageField(upload_to="Photos")
    is_verified = models.BooleanField(default=False)


class noteSubmit(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    notefile = models.FileField(upload_to="media/Notes")
    user = models.ForeignKey(userSignup, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    status_choice = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]
    status = models.CharField(max_length=20, choices=status_choice)


class contactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    msg = models.TextField()
