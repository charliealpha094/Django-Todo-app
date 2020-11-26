# Done by Carlos Amaral (2020/11/23)

from django.db import models
from django.utils import timezone
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateTimeField()
    check = models.CharField(max_length=20, default="Yes/No")
    description = models.TextField()

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
