# Creates the data the DJ4E admin autograder checks for.
# Run from the project folder with:  python manage.py shell < load_admin_data.py
# Safe to run more than once.

from django.contrib.auth.models import User
from catalog.models import Author, Book, Genre

user, created = User.objects.get_or_create(username='dj4e', defaults={'email': 'dj4e@example.com'})
user.is_staff = True
user.is_superuser = True
user.set_password('ff5cf7a5d')
user.save()
print('Superuser dj4e', 'created' if created else 'updated')

author, created = Author.objects.get_or_create(first_name='Gursees', last_name='Laya')
print('Author', author, 'created' if created else 'already exists')

genre, created = Genre.objects.get_or_create(name='Mathematics')

book, created = Book.objects.get_or_create(
    title='How the Number 42 and Kimberly are Connected',
    defaults={
        'author': author,
        'summary': 'An exploration of the surprising links between the number 42 and Kimberly.',
        'isbn': '9780000000042',
    },
)
book.genre.add(genre)
print('Book', book, 'created' if created else 'already exists')
