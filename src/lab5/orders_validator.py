import re
from collections import Counter

# Регулярное выражение для проверки формата номера телефона
PHONE_PATTERN = re.compile(r"^\+\d-\d{3}-\d{3}-\d{2}-\d{2}$")

def validate_and_process_orders(orders):
    """
    Проверяет заказы на корректность и разделяет их на валидные и невалидные.

    Аргументы:
        orders (list[str]): Список строк заказов.

    Возвращает:
        tuple:
            - list[str]: Валидные заказы в отформатированном виде.
            - list[str]: Невалидные заказы с указанием ошибок.

    Формат строки заказа:
        order_id;products;customer;address;phone;priority

        - order_id (str): Идентификатор заказа.
        - products (str): Список товаров через запятую.
        - customer (str): Имя клиента.
        - address (str): Адрес в формате "страна. регион. город. улица".
        - phone (str): Номер телефона в формате "+X-XXX-XXX-XX-XX".
        - priority (str): Приоритет заказа (MAX, MIDDLE, LOW).
    """
    valid_orders = []
    invalid_orders = []

    for order in orders:
        # Разделение строки заказа на поля
        fields = order.strip().split(";")
        if len(fields) != 6:
            continue  # Пропускаем строки с некорректным количеством полей

        order_id, products, customer, address, phone, priority = fields

        # Проверка ошибок в адресе
        if not address or len(address.split(".")) != 4:
            invalid_orders.append(f"{order_id};1;{address if address else 'no data'}")

        # Проверка ошибок в номере телефона
        if not phone or not PHONE_PATTERN.match(phone):
            invalid_orders.append(f"{order_id};2;{phone if phone else 'no data'}")

        # Если ошибок нет, добавляем заказ в список валидных
        if address and PHONE_PATTERN.match(phone):
            valid_orders.append((order_id, products, customer, address, phone, priority))

    # Сортировка валидных заказов
    valid_orders.sort(key=lambda x: (x[3].split(".")[0], ["MAX", "MIDDLE", "LOW"].index(x[5])))

    # Форматирование валидных заказов для записи в файл
    formatted_valid_orders = []
    for order_id, products, customer, address, phone, priority in valid_orders:
        product_counts = Counter(products.split(", "))
        formatted_products = ", ".join(
            f"{product} x{count}" if count > 1 else product
            for product, count in product_counts.items()
        )
        country, region, city, street = address.split(". ")
        formatted_address = f"{region}. {city}. {street}"
        formatted_valid_orders.append(
            f"{order_id};{formatted_products};{customer};{formatted_address};{phone};{priority}"
        )

    return formatted_valid_orders, invalid_orders


# Чтение данных из входного файла
with open("orders.txt", "r", encoding="utf-8") as file:
    orders = file.readlines()

# Обработка заказов
valid_orders, invalid_orders = validate_and_process_orders(orders)

# Запись валидных заказов в файл
with open("order_country.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(valid_orders))

# Запись невалидных заказов в файл
with open("non_valid_orders.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(invalid_orders))
