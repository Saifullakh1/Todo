from django.db import models


class List(models.Model):
    title = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ('-id',)
