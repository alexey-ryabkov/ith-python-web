# Итоговая работа по курсу Python on Web в ITHub

Веб-приложение позволяет просматривать и сохранять в избранное результаты спортивных матчей. Скринкаст с демо работы приложения [тут](https://disk.yandex.ru/i/gol4HHvFexZFfg)

## О реализации

- Для серверной части используется фреймворк [Flask](https://flask.palletsprojects.com/) и БД MySQL/MariaDB
- Для клиентской части используется UI-kit [Flowbite](https://flowbite.com/)

## Установка проекта

Для развертывания проекта в системе должны быть установлены 
- Python 3
- Node 22 
- MySQL/MariaDB (проект тестировался с MariaDB 11.5.2)

### Развернуть окружение

Выполнить последовательно
```bash
python3 -m venv ith-python-web_env
source ith-python-web_env/bin/activate
pip install -r requirements.txt
npm i
```

### Задать параметры подключения к БД 

Cоздать файл .env с параметрами, например:
```bash
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_DATABASE=match_result
DB_PORT=3306
FLASK_PORT=5000
```
Там же можно задать порт веб-сервера Flask.

### Запустить проект

Перед запуском проекта, необходимо запустить СУБД, затем выполнить:
```bash
npm start 
```

## Прочие команды

```bash
npm run build:css # сборка css-стилей для интерфейса приложения
npm run serve # запуск flask-приложения 
```
