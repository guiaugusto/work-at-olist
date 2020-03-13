from django.core.management.base import BaseCommand, CommandError
from authors.models import Author


class Command(BaseCommand):
    help = 'Load a valid .csv file to populate authors'

    def add_arguments(self, parser):
        parser.add_argument('authors_file', type=str)

    def handle(self, *args, **options):
        authors_count = 0

        with open(options['authors_file']) as file:
            file.readline()
            for line in file:
                line = line.replace('\n', '')
                try:
                    Author.objects.create(
                        name=line
                    )
                    print('Author {} created!'.format(line))
                except Exception:
                    print(
                        'A problem occuried when '
                        'trying to create author {}.'.format(line)
                    )
                authors_count += 1