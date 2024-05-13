from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название', **NULLABLE)
    preview = models.ImageField(upload_to='lessons/', verbose_name='Превью', **NULLABLE, help_text='Превью курса')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('name',)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Курс', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='название', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='lessons/', verbose_name='Превью', **NULLABLE, help_text='Превью курса')
    video_link = models.TextField(verbose_name='Видео', help_text='Ссылка на видео', **NULLABLE, default=None)

    def __str__(self):
        return f'{self.name} - ({self.course})'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('name',)
