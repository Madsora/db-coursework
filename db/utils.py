from repo.books_repo import books_repo
from repo.resources_repo import resources_repo
from repo.authors_repo import authors_repo
import json

backup_file = 'backup.json'


def drop():
    books_repo.drop()
    resources_repo.drop()
    authors_repo.drop()


def backup():
    data = {
        'books': books_repo.find_all(),
        'authors': authors_repo.find_all(),
        'resources': resources_repo.find_all(),
    }

    with open(backup_file, 'w+') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)


def restore():
    try:
        with open(backup_file, 'r+') as outfile:
            data = json.load(outfile)
            drop()
            books_repo.insert_all(data['books'])
            resources_repo.insert_all(data['resources'])
            authors_repo.insert_all(data['authors'])
    except:
        print('File "backup.json" is not found or damaged\n')
