## «Фабрика проектов».
Версия 1.0

Реализация с использованием следующего стека:

- Python (v.3.9)
- PostgreSQL (v.13.7)

Продукт «Фабрика проектов» представляет собой сервис, который размещается на хостинге и предоставляет пользователям возможности:

   • создавать и управлять собственными проектами;
    
   • искать проекты других пользователей по интересующим категориям;
    
   • добавлять в созданный проект других пользователей продукта.



## Запуск в Docker

docker compose up

docker compose down


http://0.0.0.0:8000/api/v1/auth/users/ - POST запрос создает пользователя
JSON request:
{
	"email": "some_name",
	"password": "some_pass"
}
==========================================================================================

http://0.0.0.0:8000/api/v1/auth/token/login/ - вход пользоватля по токену

JSON request:
{
	"email": "some_name",
	"password": "some_pass"
}

==========================================================================================

http://0.0.0.0:8000/api/v1/auth/token/logout/ - выход пользоватля по токену

Headers:
"Authorization": "Token 740ffd4612e03a6ff62aadfdfa5535adbcb444b8"

==========================================================================================

http://0.0.0.0:8000/api/v1/popular_proj/ - 3 популярных проекта
==========================================================================================
http://0.0.0.0:8000/api/v1/stacks/ - стеки технологий
==========================================================================================
http://0.0.0.0:8000/api/v1/search/ - поиск проектов по названию проекта и направлению проекта
Возвращает JSON вида:
	[
		{
			"name":"Проект Разработка на python",
			"direction":"Направление разработки на python",
			"deadline":"2022-07-28"
		},
	]

==========================================================================================
http://0.0.0.0:8000/api/v1/project/  :

POST запрос создает новый проект. Только для авторизованных пользователей.
В JSON нужно указать:

Headers:
"Authorization": "Token 740ffd4612e03a6ff62aadfdfa5535adbcb444b8"

[
    {
        "id": 8,
        "name": "Новый проект 111",
        "description": "Описание нового проекта",
        "colour": "красный",
        "profile": [
            5
        ]
    }
]

GET запрос возвращает наименование, описание, цвет и список участников проекта по его id (http://127.0.0.1:8000/api/v1/project/?id=1)

==========================================================================================
http://0.0.0.0:8000/api/v1/tasks/
POST запрос создает новую задачу. Только для авторизованных пользователей.
В JSON нужно указать:


    {
        "status": 2,
        "description": "Задача №2",
        "profile": [{"id": 2}, {"id": 3}],
        "project": 1
    }

GET запрос возвращает статус задачи, описание задачи, id и nick_name пользователя, id проекта
по id задачи (http://0.0.0.0:8000/api/v1/project/?id=1)

{
    "id": 498,
    "status": 2,
    "description": "Задача №2",
    "profile": [
        {
            "id": 2,
            "nick_name": "user1"
        },
        {
            "id": 3,
            "nick_name": "user2"
        }
    ],
    "project": 1
}

==========================================================================================
http://0.0.0.0:8000/api/v1/user-projects/

GET запрос возвращает список всех проектов пользователя. Только для авторизованных пользователей.
В JSON нужно указать:

Headers:
"Authorization": "Token 740ffd4612e03a6ff62aadfdfa5535adbcb444b8"

Возвращает результат:

[
    {
        "id": 1,
        "name": "Разработка на python",
        "description": "Проект на питоне",
        "colour": "green"
    },
    {
        "id": 2,
        "name": "Fourth project",
        "description": "Четвертый проект",
        "colour": "red"
    }
]

==========================================================================================