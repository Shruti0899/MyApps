from django.contrib import admin
from .models import Form,Regform,Userform

# Register your models here.
admin.site.register(Form)
admin.site.register(Regform)
admin.site.register(Userform)