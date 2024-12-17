from django.contrib import admin
from myBlog.models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'summary', 'content']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    list_editable = ['status']
    search_fields = ['title', 'category', 'status']
    # inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

