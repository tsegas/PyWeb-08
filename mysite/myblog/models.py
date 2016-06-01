from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'post_id': self.id})

class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User)                        # link to another model
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True) # to have unpublished posts , blank

    def get_absolute_url(self):
    	return reverse('blog_detail', kwargs={'post_id': self.id})

    def __str__(self):
        return self.title

class Category(models.Model):
	name = models.CharField(max_length=128)
	description = models.TextField(blank=True)
	posts = models.ManyToManyField(
		Post,
		blank=True,
		related_name='Categories'
		)

	def __str__(self):
		return self.name


#class Author(models.Model):
#	pass

