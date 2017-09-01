from django.db import models

# Create your models here.

class instanc(models.Model):
    instance = models.FileField(upload_to='uploads/', max_length=100)
    name = models.TextField(max_length=100)
    last_accessed = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=50)
    #user = models.ForeignKey
    #shared_with = m2m

    class Meta:
        verbose_name = "file"
        verbose_name_plural = "files"

    def __str__(self):
        return self.name

    def save(self):
        pass

    @models.permalink
    def get_absolute_url(self):
        return ('')

