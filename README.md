![статус тестов](https://github.com/4uku/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# YaMDb API


##### В этом проекте реализован API для небольшой социальной сети YaMDb. В YaMDb пользователи могут писать рецензии к различным произведениям (книги, музыка, фильмы и т.д.), а также оставлять к рецензиям комментарии. Сами произведения в YaMDb не хранятся.
### Больше информации:
Подробную документацию к API вы можете найти после запуска проекта по адресу http://localhost/redoc/
### Как запустить проект:
Клонируйте репозиторий, в папке *infra* создайте *.env* файл по шаблону:

    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=YOUR_DB_NAME
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432
Вам потребуется установленные Docker и docker-compose. Все операции с docker-compose выполняются из папки *infra* **(!!!)** . Для запуска проекта выполните команду в терминале:

    docker-compose up
Для заполнения базы данными выполните из папки *infra* команду в терминале:

    docker-compose exec web python manage.py loaddata fixtures.json
##### Для добавления данных из ```csv``` файлов в базу в следующем порядке выполнить:
```
python manage.py add_user users.csv
python manage.py add_category category.csv
python manage.py add_genre genre.csv
python manage.py add_title titles.csv
python manage.py add_review review.csv
python manage.py add_comment comments.csv

```
Автор проекта: Дмитрий Некрасов

