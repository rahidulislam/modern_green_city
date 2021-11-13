from django.db import models
from django.urls import reverse

# Create your models here.
class Setting(models.Model):
    website_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo/', blank=True)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=100)
    address = models.TextField()
    facebook = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    youtube = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"
    
    def __str__(self):
        return self.website_name

    def get_absolute_url(self):
        return reverse("Setting_detail", kwargs={"pk": self.pk})

    def image_url(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url



class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_designation = models.CharField(max_length=50)
    client_testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonial/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class OurTeam(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='our_team/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
