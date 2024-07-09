from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Course,Question,Text

# Register your models here.

admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Text)





from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)