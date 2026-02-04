from django.contrib import admin

# Register your models here.
from .models import Photo, Comment
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author' , 'created_at', 'updated_at']
    raw_id_fields = ['author']
    list_filter = ['created_at', 'updated_at','author']
    search_fields = ['text', 'created_at']
    ordering = ['-updated_at', '-created_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'photo', 'text', 'created_at']
    list_filter = ['photo', 'author', 'created_at']
    search_fields = ['text']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment, CommentAdmin)