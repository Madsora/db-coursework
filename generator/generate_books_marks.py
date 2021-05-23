import uuid
from faker import Faker
from generator.utils import write_generated_data
from repo.books_marks_repo import books_marks_repo

faker = Faker()


def generate_books_marks(book_id, resource_id, quantity=10):
    books_marks = []

    for i in range(quantity):
        words_quantity = faker.random_int(1, 3)
        words = faker.words(words_quantity)
        name = ' '.join(words)

        books_marks.append({
            '_id': f'{uuid.uuid4()}',
            'mark': faker.random_int(0, 10),
            'book_id': book_id,
            'resource_id': resource_id
        })

    write_generated_data(books_marks_repo, books_marks)
    return books_marks
