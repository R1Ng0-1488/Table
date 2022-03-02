from django.db import models


class Table(models.Model):
	date = models.DateTimeField('Дата')
	title = models.CharField('Название', max_length=100)
	quantity = models.PositiveIntegerField('Количество')
	distance = models.PositiveIntegerField('Расстояние')
	
	def __str__(self):
		return f'{self.title} {self.date}'


	class Meta:
		verbose_name = 'Таблица'
		verbose_name_plural = 'Таблицы'