<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Магазин цветов{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    {% load static %}
    <link href="{% static 'css/styles.css' %}" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
        <div class="container">
            <a class="navbar-brand" href="{% url 'flower_list' %}">
                <i class="fas fa-flower"></i> Цветочный рай
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'flower_list' %}">Каталог</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'cart' %}">
                            <i class="fas fa-shopping-cart"></i> Корзина
                            {% with total_items=request.session.cart.values|default:0|sum %}
                                {% if total_items > 0 %}
                                    <span class="badge bg-success">{{ total_items }}</span>
                                {% endif %}
                            {% endwith %}
                        </a>
                    </li>
                    {% if user.is_authenticated %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'logout' %}">Выход</a>
                        </li>
                    {% else %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'login' %}">Вход</a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <main class="mt-5 pt-4">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            {% endfor %}
        {% endif %}

        {% block content %}{% endblock %}
    </main>

    <footer class="bg-light mt-5 py-4">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <h5>Контакты</h5>
                    <p>Телефон: +7 (999) 123-45-67</p>
                    <p>Email: info@flowershop.ru</p>
                </div>
                <div class="col-md-4">
                    <h5>Режим работы</h5>
                    <p>Ежедневно с 9:00 до 21:00</p>
                </div>
                <div class="col-md-4">
                    <h5>Мы в соцсетях</h5>
                    <div class="social-links">
                        <a href="#" class="me-2"><i class="fab fa-vk"></i></a>
                        <a href="#" class="me-2"><i class="fab fa-telegram"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>