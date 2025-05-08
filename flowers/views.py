from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from .models import Flower, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from users.forms import ARegistrationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework import routers, serializers, viewsets
from flowers.serializers import FlowerSerializer
from flowers.warehouse_client import WarehouseClient
from yookassa import Configuration, Payment
from django.shortcuts import render
from django.http import JsonResponse
from shop.settings import YOOKASSA_SHOP_ID, YOOKASSA_SECRET_KEY

Configuration.configure(YOOKASSA_SHOP_ID, YOOKASSA_SECRET_KEY)
class RegisterView(generic.CreateView):
    form_class = ARegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def flower_list(request):
    flower_list = Flower.objects.filter(available=True)
    items_per_page = 9

    page = int(request.GET.get('page', 1))

    paginator = Paginator(flower_list, items_per_page)

    try:
        flowers = paginator.page(page)
    except:
        flowers = paginator.page(1)

    return render(request, 'flowers/flower_list.html', {'flowers': flowers})


def flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'flowers/flower_detail.html', {'flower': flower})


@login_required
def add_to_cart(request, flower_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Неавторизованный доступ.'})

    cart = request.session.get('cart', {})

    try:
        cart[str(flower_id)] = cart.get(str(flower_id), 0) + 1
        request.session['cart'] = cart
        return JsonResponse({
            'success': True,
            'cart_count': sum(cart.values())
        })
    except KeyError:
        return JsonResponse({'error': 'Ошибка при добавлении товара в корзину.'})


def logout_view(request):
    logout(request)
    return redirect('flower_list')


@login_required
def cart(request):
    cart_items = request.session.get('cart', {})
    items = []
    total_price = 0
    total_quantity = 0  # Переменная для подсчета общего количества товаров

    for flower_id, quantity in cart_items.items():
        flower = get_object_or_404(Flower, id=flower_id)
        subtotal = flower.price * quantity
        total_price += subtotal
        total_quantity += quantity  # Увеличиваем общее количество
        items.append({
            'flower': flower,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'flowers/cart.html', {
        'items': items,
        'total_price': total_price,
        'total_quantity': total_quantity  # Передаем общее количество в шаблон
    })
    #
    #     # Очищаем корзину
    #     request.session['cart'] = {}
    #
    #     return redirect('order_success')
    #
    # return redirect('cart')

def get_flower_quantity(request, flower_id):
    # flower = get_object_or_404(Flower, id=flower_id)
    quantity = 3
    if flower_id == 1:
        quantity = 4
    if flower_id == 2:
        quantity = 2
    if flower_id == 3:
        quantity = 1
    
    return JsonResponse({'quantity': quantity})


def buy_flower(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    warehouse = WarehouseClient()
    available_count = warehouse.check_flower_availability(flower)
    if not available_count or available_count == 0:
        return redirect('flower_list')
    # логика оплаты и тд
    #warehouse.start_assemble(order)

def create_payment(request):
    if request.method == 'POST':
        payment = Payment.create({
            "amount": {
                "value": "100.00",  # Сумма платежа
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://your-domain.com/success/"
            },
            "capture": True,
            "description": "Тестовый платеж"
        })

        return JsonResponse({'payment_url': payment.confirmation.confirmation_url})

    return render(request, 'flowers/payment.html')



# для API
class FlowersViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    


