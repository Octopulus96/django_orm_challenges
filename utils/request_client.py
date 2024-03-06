import requests
from json import JSONDecodeError
from faker import Faker

# Пускай пока остается, наработки можно использовать в тестировании
def add_book(titles: str, author_full_name: str, isbn: str) -> str:
    url = "http://127.0.0.1:8000/book/create/"
    headers = {'Content-Type': 'application/json'}
    data = {"titles": titles,
            "author_full_name": author_full_name,
            "isbn": isbn
    }
    response = requests.post(url, headers=headers, json=data)
    try:
        return response.json(), response.status_code
    except JSONDecodeError:
        return response.status_code

def fake_book_generator(book_count: int):
    for _ in [x ** 2 for x in range(book_count)]:
        fake = Faker()
        fake_data = {"titles" : fake.sentence(nb_words=3),
                     "author_full_name" : fake.name_male(),
                     "isbn" : fake.isbn13()
        }
        add_book(**fake_data)


def get_book(book_id: int):
    url = f"http://127.0.0.1:8000/book/{book_id}/"
    response = requests.get(url)
    try:
        return response.json(), response.status_code
    except JSONDecodeError:
        return response.status_code

def delete_book(book_id: int) -> int:
    url = f"http://127.0.0.1:8000/book/{book_id}/delete/"
    response = requests.post(url)
    try:
        return response.json(), response.status_code
    except JSONDecodeError:
        return response.status_code

def update_book(book_id: int, new_title: str, new_author_full_name: str, new_isbn: str) -> int:
    url = f"http://127.0.0.1:8000/book/{book_id}/update/"
    headers = {'Content-Type': 'application/json'}
    data = {
        "titles": new_title,
        "author_full_name": new_author_full_name,
        "isbn": new_isbn,
    }
    response = requests.post(url, headers=headers, json=data)
    try:
        return response.json(), response.status_code
    except JSONDecodeError:
        return response.status_code
        
if __name__ == "__main__":
    pass
    # fake = Faker()
    # fake_data1 = {"titles" : fake.sentence(nb_words=3),
    #               "author_full_name" : fake.name_male(),
    #               "isbn" : fake.isbn13()
    # }
    # add_book(**fake_data1)
    # get_book(1)
    # get_book(49)
    # delete_book(1)
    # delete_book(99)
    # fake_data2 = {"new_title" : fake.sentence(nb_words=3),
    #               "new_author_full_name" : fake.name_male(),
    #               "new_isbn" : fake.isbn13()
    # }
    # update_book(book_id=20, **fake_data2)
    # update_book(book_id=1, **fake_data2)

