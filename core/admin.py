from django.contrib import admin
from .models import Setting, ContactUs, Testimonial, OurTeam,Slider
# Register your models here.
admin.site.register(Setting)
admin.site.register(Slider)
admin.site.register(ContactUs)
admin.site.register(Testimonial)
admin.site.register(OurTeam)