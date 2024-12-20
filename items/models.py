from django.db.models import Model, CharField, FloatField, TextField


# Create your models here.
class Item(Model):
    name = CharField(max_length=100)
    description = TextField()
    price = FloatField()


