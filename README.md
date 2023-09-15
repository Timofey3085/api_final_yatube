api_final

Реализация REST API для учебного проекта Yatube на Яндекс.Практикуме. Сделан на Django Rest Framework.

Описание
API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

Описание работы.
На сайте не предусмотрено нормального веб-интерфейса, всё работает через REST API. Есть перечень эндпоинтов на главной странице и подробное описание на /redoc. Также, можно воспользоваться стандартным интерфейсом DRF, но только для анонимного чтения (посты и комментарии).

Установка

Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:ваш-аккаунт-на-гитхабе/api_final_yatube.git

cd api_final_yatube

Cоздать и активировать виртуальное окружение:

python -m venv env

source venv/Scripts/activate

Установить зависимости из файла requirements.txt:

pip install -r requirements.txt

Выполнить миграции:

python manage.py migrate

Запустить проект:

python manage.py runserver

Примеры запросов
Получить список всех публикаций. При использовании параметров limit и offset выдача будет работать с пагинацией.

GET http://127.0.0.1:8000/api/v1/posts/

Пример ответа:

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
Создание новой публикации. Создавать публикации и комментарии могут только аутентифицированные пользователи.
POST https://127.0.0.1:8000/api/v1/posts/

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

Стек технологий
Python 3.11.5,
Django 3.2.16,
DRF,
JWT + Djoser

Автор: Тимофей Разборщиков (https://github.com/Timofey3085)