import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from repo.books_repo import books_repo
from repo.authors_repo import authors_repo
from repo.resources_repo import resources_repo
from repo.books_marks_repo import books_marks_repo

graphics_path = 'results/graphics/'


def create_avarage_book_mark():
    data = {}
    books = books_repo.find_all()

    for b in books:
        book_id = b['_id']
        book_name = b['name']
        book_marks = books_marks_repo.get_book_marks(book_id)
        mean_value = np.mean(list(map(lambda m: m['mark'], book_marks)))
        data[book_name] = mean_value

    save_figure('average_book_mark', lambda: plt.bar(data.keys(), data.values()))


def create_worst_book_mark():
    data = {}
    books = books_repo.find_all()

    for b in books:
        book_id = b['_id']
        book_name = b['name']
        book_marks = books_marks_repo.get_book_marks(book_id)
        min_value = np.nanmin(list(map(lambda m: m['mark'], book_marks)))
        data[book_name] = min_value

    save_figure('worst_book_mark', lambda: plt.bar(data.keys(), data.values()))

def create_best_book_mark():
    data = {}
    books = books_repo.find_all()

    for b in books:
        book_id = b['_id']
        book_name = b['name']
        book_marks = books_marks_repo.get_book_marks(book_id)
        max_value = np.nanmax(list(map(lambda m: m['mark'], book_marks)))
        data[book_name] = max_value

    save_figure('best_book_mark', lambda: plt.bar(data.keys(), data.values()))


def create_avarage_author_books_marks(name):
    data = {}
    books = books_repo.find_books_by_author(name)

    for b in books:
        book_id = b['_id']
        book_name = b['name']
        book_marks = books_marks_repo.get_book_marks(book_id)
        mean_value = np.mean(list(map(lambda m: m['mark'], book_marks)))
        data[book_name] = mean_value

    save_figure('average_author_books_marks', lambda: plt.bar(data.keys(), data.values()))


def save_figure(image_name, create_figure=None, plot=None):
    fig = plt.figure() if plot is None else plot.get_figure()
    fig.set_figwidth(14)
    if create_figure is not None:
        create_figure()
    fig.savefig(graphics_path + image_name + '.png', dpi=fig.dpi)
