from django.contrib import admin

##from .models import Post

from myblog.models import Category 
from myblog.models import Post
#from myblog.models import Author


admin.site.register(Category)
admin.site.register(Post)


#class AuthorAdmin(admin.ModelAdmin):
#	pass
#admin.site.register(Author,AuthorAdmin)