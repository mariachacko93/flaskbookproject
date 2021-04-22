# flaskbookproject

BOOKSTORE PROJECT USING FLASK RESTPLUS APIS

Database:MongoDB

APIs - Requests and Responses

Request Method : GET (Search Fields - Author Name,Book Name)

Url - http://127.0.0.1:5000/booklist/  (Complete List of Books)
Url - http://127.0.0.1:5000/book/<objectId>(Particular Book)
For search
Url - http://127.0.0.1:5000/booklist/<searchkeyword>
Response - status 200 ok

Request Method : POST

Url - http://127.0.0.1:5000/add
Body - 
	{
    "bookname": "In Search of Lost Time",
    "author": "Marcel Proust",
    "pubyear":2020,
    "pages": 330,
}
Response - status 201 created


Request Method : PUT and PATCH

Url - http://127.0.0.1:5000/bookupdate<objectId>
Body - 
	{
    "bookname": "In Search of Lost Time by Marcel Proust",
    "author": "Marcel Proust 1",
    "pubyear":2019,
    "pages": 430,
}

Response - status 200 ok


Request Method : DELETE

Url - http://127.0.0.1:5000/bookdelete/<objectId>
Response - status 204 no content


