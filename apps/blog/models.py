from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.CharField(max_length=100, default="Ashwani Kumar")
    updated_on = models.DateTimeField(auto_now=True)
    content = CKEditor5Field('Text', config_name='extends')
    meta_description = models.CharField(max_length=160, blank=True, help_text="Search engine summary")
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_pics', blank=True, null=True)
    status = models.IntegerField(choices=((0,"Draft"), (1,"Publish")), default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.meta_description:
            self.meta_description = (self.content[:157] + '...') if len(self.content) > 160 else self.content
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
