from django.db import models
from django.urls import reverse
# Create your models here.

class LandType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='land_type/',blank=True)
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

class Land(models.Model):
    land_type = models.ForeignKey(LandType, on_delete=models.SET_NULL, blank=True, null=True, related_name='land_category')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    location = models.CharField(max_length=200)
    installment = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    land_image = models.ImageField(upload_to='land/',blank=True)
    flat_area = models.IntegerField(default=0)
    rooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    car_parking = models.IntegerField(default=0)
    contact = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Land"
        verbose_name_plural = "Lands"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Land_detail", kwargs={"pk": self.pk})

    def image_url(self):
        try:
            url = self.land_image.url
        except:
            url = ''
        return url

class LandImage(models.Model):

    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='property_image')
    caption = models.CharField(max_length=50)
    land_image = models.ImageField(upload_to='land/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "LandImage"
        verbose_name_plural = "LandImages"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("LandImage_detail", kwargs={"pk": self.pk})

        
class Katha(models.Model):
    katha_no = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.katha_no)


class Plot(models.Model):
    plot_no = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.plot_no)

class Side(models.Model):
    side_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.side_name


class LandQuery(models.Model):
    
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='property_query')
    katha = models.ForeignKey(Katha, on_delete=models.SET_NULL, blank=True, null=True, related_name='land_katha')
    side = models.ForeignKey(Side, on_delete=models.SET_NULL, blank=True, null=True, related_name='land_side')
    plot = models.ForeignKey(Plot, on_delete=models.SET_NULL, blank=True, null=True, related_name='land_plot')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField( max_length=254, blank=True)
    job_title = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name