from django.db import models


# A category of an entry
class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


# Entries are the key items of the Portfolio
# An entry is a thing done, achievement, award....
class Entry(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # file will be uploaded to MEDIA_ROOT/uploads
    pdf = models.FileField(upload_to='pdf/')
    image = models.FileField(upload_to='image/')

    def __str__(self):
        return self.name

