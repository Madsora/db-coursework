import uuid
from faker import Faker
from generator.utils import write_generated_data
from repo.books_repo import books_repo

faker = Faker()


def generate_books(author_id, quantity=10):
    books = []

    for i in range(quantity):
        words_quantity = faker.random_int(1, 3)
        words = faker.words(words_quantity)
        name = ' '.join(words)
        books.append({
            '_id': f'{uuid.uuid4()}',
            'name': name,
            'author_id': author_id,
        })

    write_generated_data(books_repo, books)
    return books
