# Автозаполнение базы данных
После применения миграций

В Employees есть script.py

# Использование
Заходим в shell командой ./manage.py shell

Импортируем функцию

``from employees.script import run``

Прописываем дальше в строке интерпретатора 

``run()``