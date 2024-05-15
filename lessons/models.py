from django.db import models

from users.models import NULLABLE, User


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


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date = models.DateField(auto_now=True, verbose_name='дата платежа')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    summ = models.PositiveIntegerField(verbose_name='сумма платежа')
    pay_choice = {'наличными': 'наличными', 'перевод': 'перевод'}
    pay_method = models.CharField(max_length=30, choices=pay_choice, verbose_name='способ платежа')

    def __str__(self):
        return (f'Платёж {self.summ} от {self.user} способ оплаты {self.pay_method} '
                f'за {self.paid_course if self.paid_course else self.paid_lesson}')

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
        ordering = ('date',)
