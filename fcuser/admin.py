from django.contrib import admin
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')   #model클래스의 필드가 업로드 됨 

admin.site.register(Fcuser, FcuserAdmin)

