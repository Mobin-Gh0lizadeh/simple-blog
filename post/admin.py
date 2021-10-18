from django.contrib import admin
from .models import Comment, Post, Category, like


class PostAdmin(admin.ModelAdmin):
    list_display=['title','created','status']
    list_filter=['title','created','status']
    search_fields=['title','description']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Post,PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    search_fields=['name']
    prepopulated_fields={'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

admin.site.register(Comment)
admin.site.register(like)
