# Работа программы
Программа связывает пользователей при помощи псевдобазы данных, использованы уникальные id, как primary ключи в БД
## Class User
Содержит геттер:
- *get_id*: возвращающий id пользователя
### Create user:
- *HTTP Method*: POST
- *Адрес*: localhost:5000/users
- *Пример запроса raw типа JSON*: {"username": "maxim", "id":1} 

### Get users
- HTTP Method: GET
- Адрес: localhost:5000/users
### Get user
- HTTP Method: GET
- Пример Адреса: localhost:5000/users/1

*где 1 это id пользователя* 
- *(Возвращает данные по конкретному пользователю в формате JSON)*

## Class Twit
Содержит геттер:
- *get_id*: возвращающий id твита
- *get_user_id*: возвращающий id пользователя
### Create twit
- HTTP Method: POST
- Адрес: localhost:5000/user/1/twit

*где 1 это id пользователя*
- Пример запроса raw типа JSON: {"body": "stromae", "author": "zaz", "id": 4}
### Read twits
- HTTP Method: GET
- Адрес: localhost:5000/twits
- Возвращает JSON со списком twit
### Read twit
- HTTP Method: GET
- Пример адреса: localhost:5000/user/1/twit

*где 1 это id пользователя*
- Возвращает JSON со списком twit
### Delete twit
- HTTP Method: DELETE
- Пример адреса: localhost:5000/twit/2

*где 2 - это id блога для удаления*
- Возвращает сообщение об операции
### Update twit
- HTTP Method: PATCH
- Пример адреса: localhost:5000/twit/2
- Пример запроса raw типа JSON: {"body": "new_body"}
*где 2 - это id блога для обновления*
- Возвращает сообщение об операции
## Class comment
Содержит геттер:
Содержит геттер:
- *get_id*: возвращающий id комментария
- *get_twit_id*: возвращающий id твита
### Create comment
- HTTP Method: POST
- Адрес: localhost:5000/twit/1/comments

*где 1 это id пользователя*
- Пример запроса raw типа JSON: {"body": "a new comment", "id": 1}

### Delete comment
- HTTP Method: DELETE
- Пример адреса: localhost:5000/comment/2

*где 2 - это id комметария для удаления*
- Возвращает сообщение об операции
