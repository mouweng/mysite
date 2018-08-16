from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod,ReadDetail

class BlogType(models.Model):
	type_name = models.CharField(max_length=15)
	def __str__(self):
		return self.type_name


class Blog(models.Model,ReadNumExpandMethod):
	title = models.CharField(max_length=50)
	blog_type  = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
	content = RichTextUploadingField(ReadDetail)
	author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	read_details = GenericRelation(ReadDetail)


	def __str__(self):
		return "<Blog:%s>" %self.title

	class Meta:
		ordering = ['-create_time']