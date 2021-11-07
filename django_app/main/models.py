from django.db import models

# Create your models here.
class ProgramTable(models.Model):
    MUL_CHOICE = [
        ('JAN', 'January'),
        ('FEB', 'February'),
        ('...', '...')
    ]

    # field_name = models.<fieldType>(*args, **kw)
    name = models.CharField('field_name')

    def __str__(self):
        return '...'


class ExtTable(models.Model):
    field = models.ForeignKey(ProgramTable, on_delete=models.CASCADE)


# manage.py makemigrations
# manage.py migrate
