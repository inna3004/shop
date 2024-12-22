from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Flower, Order, OrderItem


def flower_list(request):
    flower_list = Flower.objects.filter(available=True)
    items_per_page = 9


    page = request.GET.get('page', 1)
    paginator = Paginator(flower_list, items_per_page)

    try:
        flowers = paginator.page(page)
    except:
        flowers = paginator.page(1)

    return render(request, 'flowers/flowers_list.html', {'flowers': flowers})


def flower_detail(request, flower_id):
    #flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'flowers/flower_detail.html')


@login_required
def add_to_cart(request, flower_id):
    # if request.method == 'POST':
    #     cart = request.session.get('cart', {})
    #     cart[str(flower_id)] = cart.get(str(flower_id), 0) + 1
    #     request.session['cart'] = cart
    #     return JsonResponse({
    #         'success': True,
    #         'cart_count': sum(cart.values())
    #     })
    return JsonResponse({'success': False})

@login_required
def cart(request):
        # cart_items = request.session.get('cart', {})
        # items = []
        # total = 0
        #
        # for flower_id, quantity in cart_items.items():
        #     flower = get_object_or_404(Flower, id=flower_id)
        #     subtotal = flower.price * quantity
        #     total += subtotal
        #     items.append({
        #         'flower': flower,
        #         'quantity': quantity,
        #         'subtotal': subtotal
        #     })


    return render(request, 'flowers/cart.html')
    #
    #     # Очищаем корзину
    #     request.session['cart'] = {}
    #
    #     return redirect('order_success')
    #
    # return redirect('cart')