from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from stocksbasic.models import Stock, Note, Exchange
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'


EXCHANGE_NAMES = [
    'NASDAQ',
    'NYSE'
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the stocks data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from stock_data.csv into our Stock model"

    def handle(self, *args, **options):
        if Note.objects.exists() or Stock.objects.exists():
            print('Stock data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        print("Creating note data")

        exchange_object = Exchange(ticker='NASDAQ')
        exchange_object.save()


        print("Loading pet data for pets available for adoption")
        for row in DictReader(open('./stocks_db_initial.csv')):

            
            stock = Stock()
            stock.ticker = row['Ticker']
            stock.company = row['Company']
            stock.updater = row['Updater']
            stock.price = row['Price']
            stock.exchange = exchange_object
            stock.save()
            


            raw_stocks_notes = row['Notes']
            all_notes_array = raw_stocks_notes.split(' & ')
            print(all_notes_array)

            for anote in all_notes_array:
              note_details = anote.split(' | ')
              note_title = note_details[0]
              note_body = note_details[1]
              note_body_array = note_body.split(' $ ')
              note_real_body = note_body_array[0]
              raw_note_time = note_body_array[1]
              note_time = UTC.localize(
                datetime.strptime(raw_note_time, DATETIME_FORMAT))

              newnote = Note(title=note_title, note_text=note_real_body, submition_date=note_time)
              newnote.save()

              stock.notes.add(newnote)
 
            stock.save()
