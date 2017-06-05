import os
os. environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore_base.settings')

import django
django.setup()

import random
from books.models import Book
from faker import Faker

fakegen = Faker()

def pop_books(N=5):
    for entry in range(N):
        fake_ISBN = fakegen.isbn13(separator="-")
        fake_title = fakegen.sentence(nb_words=6, variable_nb_words=True)
        fake_description = fakegen.sentences(nb=3)
        fake_price = random.randint(2,8)
        fake_author = fakegen.name_female()

        books = Book.objects.get_or_create(ISBN=fake_ISBN,title=fake_title,description=fake_description,price=fake_price,author=fake_author)

if __name__ == '__main__':
    print("Populating Books")
    pop_books(20)
    print("Done Populating")
