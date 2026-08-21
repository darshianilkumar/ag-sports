from django.contrib import admin
from mainmenu.models import coustmers

# Register your models here.

class coustmers_admin(admin.ModelAdmin):
    list_display=['name','age','designation','time']


admin.site.register(coustmers,coustmers_admin)



