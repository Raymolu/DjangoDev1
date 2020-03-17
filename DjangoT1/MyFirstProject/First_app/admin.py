from django.contrib import admin
from First_app.models import Bears, Webpage, AccessRecord, Users

# Register your models here.

admin.site.register(Bears)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(Users)