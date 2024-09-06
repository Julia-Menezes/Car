from django.contrib import admin
from Cars.models import Car, Brand


# Register your models here.

class adminBrand(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, adminBrand)

class adminCar(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year','value','photo',)
    search_fields = ('model',)


admin.site.register(Car, adminCar)
 