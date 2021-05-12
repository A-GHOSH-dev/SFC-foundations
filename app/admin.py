from django.contrib import admin
from app.models import *
# Register your models here.


admin.site.register(BlogPostComment)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/adminjs/admin_blog.js',)

    
@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/adminjs/admin_news.js',)