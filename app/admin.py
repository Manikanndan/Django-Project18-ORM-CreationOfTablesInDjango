from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Topic)
admin.site.register(webpage)
admin.site.register(Access_Record)
admin.site.register(student)
admin.site.register(course)
admin.site.register(bonus)
admin.site.register(Salgrade)
admin.site.register(Employee)
admin.site.register(Department)