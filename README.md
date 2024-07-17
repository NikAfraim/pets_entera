# Домашние питомцы

### Описание проекта
"Домашние питомцы" — это веб-сервис, который позволяет пользователям находить информацию о питомцах и их владельцах.

### Технологии
![](https://img.shields.io/badge/Python-blue?logo=Python&logoColor=yellow&style=for-the-badge)
![](https://img.shields.io/badge/Django-092e20?logo=Django&logoColor=white&style=for-the-badge)
![](https://img.shields.io/badge/Django%20REST%20FrameWork-730000?logo=DRF&logoColor=white&style=for-the-badge)
![](https://img.shields.io/badge/Postgre_SQL-blue?logo=postgresql&logoColor=white&style=for-the-badge)
![](https://img.shields.io/badge/poetry-ad998b?logo=poetry&logoColor=white&style=for-the-badge)
![](https://img.shields.io/badge/docker-blue?logo=docker&logoColor=white&style=for-the-badge)
![](https://img.shields.io/badge/gunicorn-white?logo=gunicorn&logoColor=%23092E20&style=for-the-badge)

### Разработчик
[Никита Сенгилейцев](https://github.com/NikAfraim)

## Запуск проекта

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/NikAfraim/pets_entera.git
```

2. Перейдите в каталог проекта:
```bash
cd pets_entera
```

3. Создайте файл .env в `/infra` и в `/pets_site`, используя шаблон `/infra/.env.example_docker` и `/pets_site/.env.example_django` соответственно.


### Запуск

1. Перейдите в `infra/`:
```bash
cd infra/
```

2. Запустите docker-compose:
```bash
docker compose up -d --build
```

3. Выполните миграции внутри контейнера:
```bash
docker-compose exec backend python manage.py migrate
```

* Вы можете загрузить небольшой объем данных в БД:
```bash
docker-compose exec backend python manage.py add_types
```

Проект будет доступен по адресу: http://localhost/.  
API проекта: http://localhost/api/.