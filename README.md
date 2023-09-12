api_final
api final

Описание проекта
В этом проекте разработан API для работы с базой данных:

создание, редактирование, удаление постов, комментариев к ним
создание и просмотр пользователей, подписок.
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
