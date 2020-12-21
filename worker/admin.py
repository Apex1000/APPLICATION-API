from django.contrib import admin
from worker.models import Worker,Activity
# Register your models here.
admin.site.register(Worker)
admin.site.register(Activity)