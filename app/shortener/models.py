from django.db import models


class Url(models.Model):
    original_url = models.TextField(unique=True)
    hash = models.CharField(max_length=55, unique=True)
    number_clicks = models.IntegerField(default=0)


    def add_click(self):
        self.number_clicks +=1
        self.save()

    def __str__(self) -> str:
        return self.original_url