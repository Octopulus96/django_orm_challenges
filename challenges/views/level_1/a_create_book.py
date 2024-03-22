"""
В этом задании вам нужно реализовать функцию create_book, которая создаёт в БД строку с новой книгой.

Чтобы проверить, работает ли ваш код, запустите runserver и сделайте POST-запрос на 127.0.0.1:8000/book/create/
с теми же параметрами. Если всё отработало без ошибок и ручка возвращает вам описание новой книги в json-формате,
задание выполнено.

Делать post-запрос я рекомендую с помощью Postman (https://www.postman.com/downloads/).
"""
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse
import logging, json
from challenges.models import Book

logger = logging.getLogger(__name__)

def create_book(title: str, author_full_name: str, isbn: str) -> Book:
    book = Book(title=title, author_full_name=author_full_name, isbn=isbn)
    book.save()
    return book


def create_book_handler(request: HttpRequest) -> HttpResponse:
    logger.debug(request.body)
    data = json.loads(request.body)
    title = data.get("title")
    author_full_name = data.get("author_full_name")
    isbn = data.get("isbn")
    if not all([title, author_full_name, isbn]):
        return HttpResponseBadRequest("One of required parameters are missing")

    book = create_book(title, author_full_name, isbn)

    return JsonResponse({
        "id": book.pk,
        "title": book.title,
        "author_full_name": book.author_full_name,
        "isbn": book.isbn,
    })
