from django.shortcuts import render
from items.models import Item


def view(request, id: int):
    item = Item.objects.filter(id=id).get()
    return render(request, 'items/item.html', {'tovar': item})
# Create your views here.

def index(request):
    items = Item.objects.all()
    return render(request, 'items/items.html', {'items': items})