from django.db import models

class Essay(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    essay = models.FileField(upload_to="essays", blank=True, null=True)
    pub_date = models.DateField(blank=True, null=True)

