# Базовый образ, например, Python 3.9
FROM python:3.9-slim

# Установка рабочей директории
WORKDIR /app

# Копируем зависимости
COPY requirements.txt ./

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остального исходного кода и входных данных
COPY . .

# Указание команды для запуска приложения
CMD ["python3", "code_project.py"]
