Тестовое задание на разработку API агрегатора и калькулятора ипотечных предложений
=====

Описание проекта
----------
Проект представляет собой API агрегатор и калькулятор ипотечных предложений на основе [примера](https://www.sravni.ru/ipoteka/?mortgagePurpose=1&creditAmount=11849421&initialAmount=1500000&mortgageTerm=120).

За основу для данного проекта взята реализация следующего [API](https://documenter.getpostman.com/view/6802079/UVeAvonG).

Проект разворачивается в трех Docker контейнерах: web-приложение, postgresql-база данных и nginx-сервер. 

Проект основан на Django Rest Framework, аутентификация в проекте не предусмотрена, настроены модели для отображения в панели администратора. Реализованы тесты эндпоинтов и моделей проекта.

Реализована сортировка выходных данных API по расчитанному ежемесячному платежу и по рассчитанной ставке.

Пользовательский сценарий
----------
Клиент вводит следующие данные:
1. Стоимость объекта недвижимости, в рублях без копеек.
2. Первоначальный взнос, в рублях без копеек.
3. Срок, в годах.

В ответ клиенту приходит массив с объектами ипотечных предложений. В каждом объекте есть следующие данные:
1. Наименование банка.
2. Ипотечная ставка, в процентах.
3. Платеж по ипотеке, в рублях без копеек.

Системные требования
----------
* Python 3.8+
* Docker
* Works on Linux, Windows, macOS, BSD

Стек технологий
----------
* Python 3.8
* Django 3.1
* PostgreSQL
* Django Rest Framework
* Nginx
* gunicorn
* Docker
* unittest

Установка проекта из репозитория (Linux и macOS)
----------
1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@contest.idacloud.ru:Nikita223/backend_task_2.git

cd backend_task_2
```

2. Cоздать и открыть файл ```.env``` с переменными окружения:
```bash 
cd infra

touch .env
```

3. Заполнить ```.env``` файл с переменными окружения по примеру:
```bash 
echo DB_NAME=postgres >> .env

echo POSTGRES_PASSWORD=postgres >> .env

echo POSTGRES_USER=postgres >> .env

echo DB_HOST=db >> .env

echo DB_PORT=5432 >> .env
```

4. Установка и запуск приложения в контейнерах:
```bash 
docker-compose up -d
```

5. Запуск миграций, сбор статики и запуск тестов:
```bash 
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py collectstatic --no-input 

docker-compose exec web python manage.py test 
```

Документация к проекту
----------
Документация для API после установки доступна по адресу ```/api/docs/```.
