from django.db import models

# Create your models here.
class TODO(models.Model):
    thing = models.CharField(max_length=20, verbose_name='待办事项')
    done = models.BooleanField(default=False, verbose_name='已完成')

    def __str__(self):
        return self.thing

    class Meta():
        db_table = 'todolist'
