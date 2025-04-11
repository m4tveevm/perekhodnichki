# Переходнички ЛЭТИ - Проект геймификация музеев

[![CI/CD Status](https://github.com/m4tveevm/perekhodnichki/actions/workflows/deploy.yml/badge.svg)](https://github.com/m4tveevm/perekhodnichki/actions/workflows/deploy.yml)
[![Перейти на сайт](https://img.shields.io/badge/Перейти-на_сайт-blue)](https://spbetu.ru)
## О проекте

Интерактивная платформа для вовлечения студентов в изучение богатой истории
музеев и корпусов ЛЭТИ с использованием игровых механик и виртуальных квестов.

---

## Структура проекта:

- `/src` – Django backend
- `/frontend` – React frontend

## Подготовка к запуску проекта

### Backend (Django)

Убедитесь, что у вас установлены:

- [Git](https://git-scm.com/downloads)
- [Python 3.10+](https://www.python.org)

Клонируйте проект:

```sh
git clone https://github.com/m4tveevm/perekhodnichki.git
cd perekhodnichki/src
```

Создайте виртуальное окружение:

```sh
# Linux/MacOS
python3 -m venv .venv
source .venv/bin/activate

# Windows (шиндоус)
python -m venv .venv
.venv\Scripts\activate
```

Установите зависимости:

```sh
pip install -r requirements/prod.txt
# Опционально (для разработки и тестирования):
pip install -r requirements/dev.txt
pip install -r requirements/test.txt
```

### Переменные окружения

Наш проект как им ногие другие использует переменные окружения, для их задачи
скопируйте и настройте файл `.env`:

```sh
cp .env.example .env
```

Откройте и измените файл `.env`:

```sh
nvim .env
```

PS: для выхода из nvim/vim следует нажать shift + ":" и написать в поле q,
также допускается вариант с перерезанием кабеля питания вашего кудахтера (
компьютера)

Шаблон с необходимыми переменным в файле `.env` (в целом, мы хоть и не советуем
задавать сикреты так, но для локальной разработки возможно вам так будет удобнее
справиться с запуском проекта):

```env
DJANGO_SECRET=your-secret-key-here
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,.edu.spbetu.ru
CSRF_TRUSTED_ORIGINS=http://localhost:3000,https://edu.spbetu.ru
DJANGO_DB_HOST=db
DJANGO_DB_NAME=postgres
DJANGO_DB_USER=postgres
DJANGO_DB_PORT=5432
DJANGO_SUPERUSER_USERNAME=user
DJANGO_SUPERUSER_EMAIL=username@123.you
DJANGO_SUPERUSER_PASSWORD=not-a-real-password
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=db-password
CORS_ALLOWED_ORIGIN_REGEXES=^https:\/\/(?:.*\.)?edu\.spbetu\.ru$
LOG_LEVEL=INFO
```

Применение миграций и сервера:

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

### Frontend (React)

Убедитесь, что у вас установлен [Node.js](https://nodejs.org/) версии 20+.

Перейдите в каталог фронтенда:

```sh
cd ../frontend
```

Установите зависимости и запустите фронтенд:

```sh
npm install
npm run dev
```

После успешного запуска фронтед-приложение доступно по адресу:

```
http://localhost:5173/
```
