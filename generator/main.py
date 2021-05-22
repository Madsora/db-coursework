from generator.generate_books import generate_books
from generator.generate_authors import generate_authors
from generator.generate_resources import generate_resources

def generate_all(authors_amount, books_amount, resources_amount):
    authors = generate_authors(authors_amount)
    all_books = []
    book_ids = []

    for a in authors:
        books = generate_books(a['_id'], books_amount)
        for b in books:
            book_ids.append(b['_id'])
            
    resources = generate_resources(book_ids, resources_amount)