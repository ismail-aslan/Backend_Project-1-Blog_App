from django.contrib import admin
from .models import Post,Like,Comment,Profile,PostView,Category
# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(PostView)
admin.site.register(Category)