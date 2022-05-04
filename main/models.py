from django.db import models

# Create your models here.
class ToDoList(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateField()
	checked = models.BooleanField(default=False)
	def __str__(self):
		return self.title
