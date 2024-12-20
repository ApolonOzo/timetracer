from django.db import models

class Person(models.Model):
    name = models.CharField('Имя пользователя', max_length=50)
    gmail = models.CharField('Почта', max_length=50)
    password = models.CharField('Пароль', max_length=50)
    passwordagain = models.CharField('Пароль повторно', max_length=50)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_pluar = 'Пользователи'