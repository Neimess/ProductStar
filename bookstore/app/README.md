# Работа программы
Сервер запускается командой flask --app bookstore/ --debug run
При нахождении в папке app

## Было создано:

- Хранилище для любых релятивистких известных БД при помощи SQLAlchemy
- Расширен функционал - добавлен метод get_by_id и update
- Базовый класс MemoryStorage стал абстрактным

## Создание книги
- *HTTP Method*: POST
- *Адрес*: localhost:5000/books/
- ```curl -XPOST --json '{"title":"thebook", "description": "a book", "publish_year": 2020, "pages_count":100, "created_at": "2022-11-21"}' "http:/localhost:5000/books/"``

## Получение всех
- *HTTP Method*: GET
- *Адрес*: localhost:5000/books/
- ```curl -s "http://localhost:5000/books/"

## Получение книги по id
- *HTTP Method*: GET
- *Адрес*: localhost:5000/books/1
- ```curl -s "http://localhost:5000/books/1" 

## Удаление из хранилища
- *HTTP Method*: DELETE
- *Адрес*: localhost:5000/books/1
- curl -XDELETE "http://localhost:5000/books/1" 

## Обновление данных
- *HTTP Method*: PATCH
- *Адрес*: localhost:5000/books/1
- ```curl -XPATCH --json '{"title":"thebook", "description": "a book", "publish_year": 2020, "pages_count":100, "created_at": "2022-11-25"}' "http:/localhost:5000/books/2"
