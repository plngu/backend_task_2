## Описание сервиса

Калькулятор ипотечных предложений. [Пример](https://www.sravni.ru/ipoteka/?mortgagePurpose=1&creditAmount=11849421&initialAmount=1500000&mortgageTerm=120)

----

### Пользовательский сценарий
Клиент вводит следующие данные:
1. Стоимость объекта недвижимости, в рублях без копеек. Тип данных: integer.
2. Первоначальный взнос, в рублях без копеек. Тип данных: integer.
3. Срок, в годах. Тип данных: integer.

Клиент получает ответ:
1. Наименование банка. Тип данных: string.
2. Ипотечная ставка, в процентах. Тип данных: float.
3. Платеж по ипотеке, в рублях без копеек.  Тип данных: integer.

Реализована фильтрация и сортировка ипотечных предложений по введенным параметрам.


-----


### Используемый стек
- Django
- DRF
- django-filters
- PostgreSQL


-----


### Запуск проекта
```commandline
cd ~
git clone https://github.com/plngu/backend_task_2.git
cd backend_task_2
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
cd backend
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata dump.json 
python3 manage.py runserver
```


### Примеры запросов

GET, POST - получение списка ипотечных предложений и создание предложения ```http://127.0.0.1:8000/api/offer/```

Тело запроса (для POST):
```json  
{
    "bank_name": "sber", // название банка
    "term_min": 10, // минимальный срок ипотеки
    "term_max": 40, // максимальный срок ипотеки
    "rate_min": 12.0, // минимальный процент по ипотеке
    "rate_max": 16.0, // максимальный процент по ипотеке
    "payment_min": 1000000, // минимальная сумма кредита
    "payment_max": 30000000 // максимальная сумма кредита
}
```
Ответ:
```json
{
    "id": 17,
    "payment": "Выберите начальный взнос, срок ипотеки и цену недвижимости",
    "bank_name": "sber",
    "term_min": 10,
    "term_max": 40,
    "rate_min": 12.0,
    "rate_max": 16.0,
    "payment_min": 1000000,
    "payment_max": 30000000
}
```

PATCH - изменение ипотечного предложения```http://127.0.0.1:8000/api/offer/17/```

Тело запроса:
```json
{
    "term_max": 45
}
```
Ответ:
```json
{
    "id": 17,
    "payment": "Выберите начальный взнос, срок ипотеки и цену недвижимости",
    "bank_name": "sber",
    "term_min": 10,
    "term_max": 45,
    "rate_min": 12.0,
    "rate_max": 16.0,
    "payment_min": 1000000,
    "payment_max": 30000000
}
```

DELETE - удаление ипотечного предложения ```http://127.0.0.1:8000/api/offer/17/```


-----


GET-запрос с параметрами
```http://127.0.0.1:8000/api/offer/?deposit=1000000&term=35&price=10000000```

Выдаются предложения, для которых значения ```price``` - сумма ипотеки и ```term``` - срок ипотеки лежат 
в пределах минимальных и максимальных значений для конкретного предложения.

Ответ:
```json
[
    {
        "id": 13,
        "payment": 85732,
        "bank_name": "vtb",
        "term_min": 10,
        "term_max": 40,
        "rate_min": 11.2,
        "rate_max": 22.8,
        "payment_min": 100000,
        "payment_max": 30000000
    },
    {
        "id": 16,
        "payment": 89976,
        "bank_name": "sber",
        "term_min": 10,
        "term_max": 35,
        "rate_min": 11.8,
        "rate_max": 16.7,
        "payment_min": 500000,
        "payment_max": 15000000
    }
]
```
GET ```http://127.0.0.1:8000/api/offer/?deposit=1000000&term=35&price=10000000&payment_min=86000&payment_max=90000```

```json
[
    {
        "id": 16,
        "payment": 89976,
        "bank_name": "sber",
        "term_min": 10,
        "term_max": 35,
        "rate_min": 11.8,
        "rate_max": 16.7,
        "payment_min": 500000,
        "payment_max": 15000000
    }
]
```

GET ```http://127.0.0.1:8000/api/offer/?deposit=1000000&term=35&price=10000000&payment_min=85000&payment_max=90000```
```json
[
    {
        "id": 13,
        "payment": 85732,
        "bank_name": "vtb",
        "term_min": 10,
        "term_max": 40,
        "rate_min": 11.2,
        "rate_max": 22.8,
        "payment_min": 100000,
        "payment_max": 30000000
    },
    {
        "id": 16,
        "payment": 89976,
        "bank_name": "sber",
        "term_min": 10,
        "term_max": 35,
        "rate_min": 11.8,
        "rate_max": 16.7,
        "payment_min": 500000,
        "payment_max": 15000000
    }
]
```
