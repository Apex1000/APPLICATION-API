from django.contrib import admin
from authentication.models import User,UserDetail,Role
# Register your models here.
admin.site.register(User)
admin.site.register(UserDetail)
admin.site.register(Role)