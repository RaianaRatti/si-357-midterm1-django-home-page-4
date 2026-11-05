# Sets up the data the DJ4E home page autograder checks for.
# Run from the project folder with:  python manage.py shell < load_admin_data.py
# Safe to run more than once.

from django.contrib.auth.models import User
from catalog.models import Author, Book, Genre

# The home page autograder takes points off if dj4e can still log in to /admin,
# so remove its staff and superuser status (left over from the admin site assignment).
removed = User.objects.filter(username='dj4e').update(is_staff=False, is_superuser=False)
print('dj4e staff/superuser status removed' if removed else 'No dj4e user to update')

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
