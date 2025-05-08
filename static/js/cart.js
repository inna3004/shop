// static/js/cart.js
document.addEventListener('DOMContentLoaded', function() {
    // Инициализация тоста
    const toastElement = document.getElementById('cartToast');
    const toast = new bootstrap.Toast(toastElement, {
        delay: 2000
    });


fetch('/create-payment', {
    method: 'POST',
    body: JSON.stringify(orderDetails),
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(response => response.json())
.then(data => {
    window.location.href = data.payment_url; // Перенаправление на страницу оплаты
})
.catch(error => console.error('Ошибка:', error));



    // Обработчики кнопок + и -
    const decreaseButtons = document.querySelectorAll('.decrease-quantity');
    const increaseButtons = document.querySelectorAll('.increase-quantity');
    const quantityInputs = document.querySelectorAll('.quantity-input');

    // Обработка уменьшения количества
    decreaseButtons.forEach(button => {
        button.addEventListener('click', function() {
            const flowerId = this.dataset.flowerId;
            const input = document.querySelector(`.quantity-input[data-flower-id="${flowerId}"]`);
            const currentValue = parseInt(input.value);
            if (currentValue > 1) {
                input.value = currentValue - 1;
                updateCart(flowerId, currentValue - 1, 'update');
            }
        });
    });

    // Обработка увеличения количества
    increaseButtons.forEach(button => {
        button.addEventListener('click', function() {
            const flowerId = this.dataset.flowerId;
            const input = document.querySelector(`.quantity-input[data-flower-id="${flowerId}"]`);
            const currentValue = parseInt(input.value);
            if (currentValue < 99) {
                input.value = currentValue + 1;
                updateCart(flowerId, currentValue + 1, 'add');
                showToast('Товар добавлен в корзину');
            }
        });
    });

    // Обработка ручного ввода количества
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            const flowerId = this.dataset.flowerId;
            let value = parseInt(this.value);

            if (isNaN(value) || value < 1) value = 1;
            if (value > 99) value = 99;

            this.value = value;
            updateCart(flowerId, value, 'update');
        });
    });

    // Функция обновления корзины
    function updateCart(flowerId, quantity, action) {
        fetch(`/cart/add/${flowerId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                quantity: quantity,
                action: action
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Обновление счетчика корзины
                updateCartCounter(data.cart_count);

                // Обновление количества товара
                updateItemQuantity(flowerId, data.item_quantity);

                // Обновление цены
                if (data.total_price) {
                    updateItemPrice(flowerId, data.total_price);
                }

                // Показ уведомления
                if (action === 'add') {
                    showToast(data.message);
                }
            }
        });
    }

    // Вспомогательные функции
    function updateCartCounter(count) {
        const counter = document.querySelector('.cart-counter');
        if (counter) {
            counter.textContent = count;
            counter.classList.remove('d-none');
        }
    }

    function updateItemQuantity(flowerId, quantity) {
        const input = document.querySelector(`.quantity-input[data-flower-id="${flowerId}"]`);
        if (input) {
            input.value = quantity;
        }
    }

    function updateItemPrice(flowerId, price) {
        const priceElement = document.querySelector(`.price-block[data-flower-id="${flowerId}"] .current-price`);
        if (priceElement) {
            priceElement.textContent = price + ' ₽';
        }
    }

    function showToast(message) {
        const toastBody = document.querySelector('.toast-body');
        if (toastBody) {
            toastBody.textContent = message;
        }
        toast.show();
    }


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});