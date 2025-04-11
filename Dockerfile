FROM python:3.12-slim

WORKDIR /app

# Используем альтернативное зеркало
COPY requirements.txt .
RUN pip install --no-cache-dir -i https://pypi.python.org/simple -r requirements.txt

COPY . .

CMD ["python", "a4/manage.py", "runserver", "0.0.0.0:8000"]