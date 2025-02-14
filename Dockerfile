FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Собираем статику
RUN python manage.py collectstatic --noinput

# Запускаем приложение через Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "shop.wsgi:application"]