import uuid
from faker import Faker
from generator.utils import write_generated_data
from repo.resources_repo import resources_repo

faker = Faker()


def generate_resources(books_ids, quantity=10):
    resources = []

    for i in range(quantity):
        words_quantity = faker.random_int(1, 3)
        words = faker.words(words_quantity)
        name = ' '.join(words)
        books = []

        for i in range(len(books_ids)):
            books.append({
                '_id': books_ids[i],
                'mark': faker.random_int(0, 10),
            })

        resources.append({
            '_id': f'{uuid.uuid4()}',
            'resource_name': name,
            'books': books
        })

    write_generated_data(resources_repo, resources)
    return resources