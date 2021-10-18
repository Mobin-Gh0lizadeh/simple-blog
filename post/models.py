from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post:post_list_by_category' ,
                        args=[self.slug])

class Post(models.Model):

    STATUS_CHOICES=(
        ('draft','draft'),
        ('published','published')
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='PostCategory')
    description = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='media/post-image/%Y/%m/%d/', null=True ,blank=True)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_detail', args =
                                            [self.created.year,
                                            self.created.month,
                                            self.created.day, self.slug]
                                            )

    def likes_count(self):
	    return self.postlike.count()

    def comment_count(self):
	    return self.commentpost.count()



class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='commentuser')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commentpost')
	body = models.TextField(max_length=500)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.user} - {self.body[:30]}'

	class Meta:
		ordering = ('-created',)

class like(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postlike')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userlike')

	def __str__(self):
		return f'{self.user} liked {self.post}'
