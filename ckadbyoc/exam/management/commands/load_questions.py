from csv import DictReader
from datetime import datetime
import random
from django.core.management import BaseCommand

from exam.models import Questions
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

phonetics = ["alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india","juliet","kilo","lima","mike","november","oscar","papa","quebec","romeo","sierra","tango","uniform","victor","whiskey","x-ray","yankee","zulu"]
sphonetics = ["alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india","juliet","kilo","lima","mike","november","oscar","papa","quebec","romeo","sierra","tango","uniform","victor","whiskey","x-ray","yankee","zulu"]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the q data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from q_data.csv into our q model"

    def handle(self, *args, **options):
        if Questions.objects.exists():
            print('question data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading questions into DB")
        for row in DictReader(open('./q_data.csv')):
            q = Questions()
            q.name_short = row['name_short']
            q.category = row['category']
            q.nscontext = random.choice(phonetics)
            phonetics.remove(q.nscontext)
            q.context = random.choice(sphonetics)
            sphonetics.remove(q.context)
            q.question = row['question']
            q.workdir = row['workingpath']
            raw_submission_date = row['submission date']
            submission_date = UTC.localize(
                datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            q.submission_date = submission_date
            q.save()
