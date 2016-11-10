from django.contrib import admin
from .models import *
from user_profile.models import *
# Register your models here.
admin.site.register(Member)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Media)
admin.site.register(Follow)
admin.site.register(Upload)
admin.site.register(Block)
admin.site.register(Report)
admin.site.register(HashTag)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Interests)
admin.site.register(View)
