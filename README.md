# Culinary_book — кулинарная книга на Django

Web-site для хранения рецептов с возможностью поиска по наименованию рецептов.

**Выполнили:** Данилин Егор, Малышев Артём, Ошкин Артём 

---

## Функционал

- **Список своих рецептов** 
- **Создание рецепта** 
- **Редактирование и удаление** 
- **Поиск по названию рецептов**
- **Авторизация**

---

## Стек технологий

- Python 3.11+
- Django 6.0
- SQLite
- HTML + CSS (Bootstrap 5)
- Django Templates
- DB Browser for SQLite
- Postman
- Docker
---

## Запуск локально

```bash
git clone https://github.com/murmyauuu/culinary_book.git
cd culinary_book
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/macOS
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver