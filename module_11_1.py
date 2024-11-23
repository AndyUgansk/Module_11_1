import matplotlib.pyplot as plt
import numpy as np
import requests
from datetime import datetime


print(25 * "*", "Работа с библиотекой  NumPy", 25 * "*")
# Создаем массив чисел с помощью библиотеки NumPy
array = np.array([1, 2, 3, 4, 5])

# Выполняем математические операции
multiplied_array = array * 2
added_array = array + 10
sum_of_elements = np.sum(array)
mean_of_elements = np.mean(array)

# Выводим результаты в консоль
print("Исходный массив:", array)
print("Умноженный массив:", multiplied_array)
print("Массив с добавленными элементами:", added_array)
print("Сумма элементов:", sum_of_elements)
print("Среднее значение элементов:", mean_of_elements)

print(24 * "*", "Работа с библиотекой Requests", 24 * "*")
# Выполняем GET-запрос
url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)

# Проверяем статус запроса
if response.status_code == 200:
    # Получаем данные в формате JSON
    data = response.json()

    # Извлекаем данные
    date = data['Date']
    eur_rate = data['Valute']['EUR']['Value']
    usd_rate = data['Valute']['USD']['Value']

    # Получаем текущую дату
    current_date = datetime.now().strftime('%d.%m.%Y')

    # Вывод результата
    print(f"Дата: {current_date}")
    print(f"Курс EUR: {eur_rate}")
    print(f"Курс USD: {usd_rate}")
else:
    print("Не удалось получить данные.")

# Генерируем данные для визуализации
# Создаем массив x от 0 до 10 с шагом 0.1
x = np.arange(0, 10, 0.1)
# Создаем зависимости y = sin(x) и y2 = cos(x)
y1 = np.sin(x)
y2 = np.cos(x)

# Начинаем создание графика
plt.figure(figsize=(10, 6))  # Указываем размер холста

# Устанавливаем первую линию с заголовком, цветом и стилем
plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2)

# Устанавливаем вторую линию с заголовком, цветом и стилем
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)

# Добавляем заголовок графика
plt.title('Графики функций sin(x) и cos(x)')

# Добавляем подписи к осям
plt.xlabel('x-ось')
plt.ylabel('y-ось')

# Добавляем сетку для удобства чтения графика
plt.grid(True)

# Размещаем легенду (описание графиков) на графике
plt.legend()

# Отображаем график
plt.show()
