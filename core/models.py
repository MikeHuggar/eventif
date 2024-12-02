from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('photo')
    website = models.URLField('website', blank=True)
    description = models.TextField('description', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'
    
    def __str__(self):
        return self.name