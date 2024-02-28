## Реализация REST API для учебного проекта Yatube на Яндекс.Практикуме. Сделан на Django Rest Framework.

### Описание

API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

### Описание работы.

На сайте не предусмотрено нормального веб-интерфейса, всё работает через REST API. Есть перечень эндпоинтов на главной странице и подробное описание на /redoc. Также, можно воспользоваться стандартным интерфейсом DRF, но только для анонимного чтения (посты и комментарии).

### Установка

#### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:ваш-аккаунт-на-гитхабе/api_final_yatube.git

cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```bash
python -m venv env

source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```
Выполнить миграции:
```bash
python manage.py migrate
```
Запустить проект:
```bash
python manage.py runserver
```
### Примеры запросов

Получить список всех публикаций. При использовании параметров limit и offset выдача будет работать с пагинацией.
```bash
GET http://127.0.0.1:8000/api/v1/posts/
```
#### Пример ответа:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
#### Создание новой публикации. Создавать публикации и комментарии могут только аутентифицированные пользователи.
POST https://127.0.0.1:8000/api/v1/posts/
```
{
"text": "string",
"image": "string",
"group": 0
}
Пример ответа:

{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
#### Стек технологий:

Python 3.11.5,
Django 3.2.16,
DRF,
JWT + Djoser

#### Полезные ссылки на документации:
```
1 Simple JWT https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html
```
```
2 Generic views https://www.django-rest-framework.org/api-guide/generic-views/
```
```
3 Mixins https://testdriven.io/blog/drf-views-part-2/
```
```
4 Django Rest Framework https://www.django-rest-framework.org/
```
```
5 Unique Constraint https://django.fun/ru/docs/django/4.1/ref/models/constraints/#uniqueconstraint
```


Авторы
[Timofey - Razborshchikov](https://github.com/Timofey3085)
