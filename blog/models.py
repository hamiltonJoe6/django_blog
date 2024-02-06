from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
            return self.name

class Blog(models.Model):

	options = (
		('draft', 'Draft'),
		('published', 'Published'),
	)

	title = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
	tag = models.CharField(max_length=50)
	body = models.TextField(blank=True, default="")
	slug = models.SlugField(max_length=200)
	published = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=options, default='draft')

	class Meta:
		ordering = ('-published',)

	def __str__(self):
		return self.title
