
from django.contrib.auth.models import User
from django.db import models


class Predicions(models.Model):
    type_refuses = models.CharField(max_length=500, verbose_name="тип отказа")
    type_gpa = models.CharField(max_length=500, verbose_name="Тип ГПА")
    type_say = models.CharField(max_length=500, verbose_name="Тип САУ")
    type_equioment = models.CharField(max_length=500, verbose_name="Внешнее проявления отказа")
    element = models.CharField(max_length=500, verbose_name="Подробное описание причины отказа")
    refuses_element = models.CharField(max_length=500, verbose_name="Элемента отказа")
    maybe_reasons = models.CharField(max_length=500, verbose_name="Отказавший элемент")
    meropriation = models.CharField(max_length=500, verbose_name="Содержание Мероприятия")

    class Meta:
        verbose_name = 'Экспертная система отказ СА'
        verbose_name_plural = 'Экспертная система отказ СА'


