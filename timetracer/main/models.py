from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    gmail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    passwordagain = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
