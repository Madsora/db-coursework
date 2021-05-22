import uuid
from faker import Faker
from generator.utils import write_generated_data
from repo.authors_repo import authors_repo

faker = Faker()


def generate_authors(quantity=10):
    authors = []

    for i in range(quantity):

        authors.append({
            '_id': f'{uuid.uuid4()}',
            'name': faker.name(),
        })
        
    write_generated_data(authors_repo, authors)
    return authors