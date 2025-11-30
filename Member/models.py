from django.db import models

# Create your models here.
class ModelMember(models.Model):
    ho = models.CharField(max_length=255)
    ten = models.CharField(max_length=255)
    codeforces_id = models.CharField(max_length=255)
    org = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.ho} {self.ten}"