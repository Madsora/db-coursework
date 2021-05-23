from generator.generate_books import generate_books
from generator.generate_authors import generate_authors
from generator.generate_resources import generate_resources
from generator.generate_books_marks import generate_books_marks

def generate_all(authors_amount, books_amount, resources_amount):
    authors = generate_authors(authors_amount)
    resources = generate_resources(resources_amount)
    all_books = []

    for a in authors:
        books = generate_books(a['_id'], books_amount)
        for b in books:
            all_books.append(b)

    for r in resources:
        for b in all_books:
            books_marks = generate_books_marks(b['_id'], r['_id'], 1)