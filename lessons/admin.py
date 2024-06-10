from django.contrib import admin

from lessons.models import Payments, Course


@admin.register(Payments)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'paid_lesson', 'paid_course', 'summ', 'pay_method', 'session_id', 'link')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'owner',)
