from django.contrib import admin
from .models import Land,LandImage,LandType,Katha,Side,Plot,LandQuery
# Register your models here.
class LandTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class LandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(LandType, LandTypeAdmin)
admin.site.register(Land, LandAdmin)
admin.site.register(LandImage)
admin.site.register(Katha)
admin.site.register(Side)
admin.site.register(Plot)
admin.site.register(LandQuery)