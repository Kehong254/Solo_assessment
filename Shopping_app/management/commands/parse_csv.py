import csv
import os
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from Shopping_app.models import Volcano


class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def handle(self, *args, **options):
        Volcano.objects.all().delete()
        print("Table dropped successfully.")

        try:
            base_dir = Path(__file__).resolve().parent.parent.parent.parent
            with open(str(base_dir) + '/Shopping_app/Shopping_datas/The_Volcanoes_Of_Earth2.csv', newline='', encoding='iso-8859-1', errors='ignore') as csv_file:
                reader = csv.DictReader(csv_file, delimiter=",")
                for row in reader:
                    print(row)

                    All_data = Volcano.objects.create(
                    Volcano_ID=row['Volcano_ID'],
                    Volcano_Name=row['Volcano_Name'],
                    Volcano_Image=row['Volcano_Image'],
                    Volcano_Type=row['Volcano_Type'],
                    Country=row['Country'],
                    epoch_period=row['epoch_period'],
                    Latitude=row['Latitude'],
                    Longitude=row['Longitude'],
                    price=row['price'],
                    quantity=row['quantity']
                    )

                    All_data.save()

            self.stdout.write(self.style.SUCCESS('Data imported successfully.'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found.'))

        except csv.Error as e:
            self.stdout.write(self.style.ERROR(f'Error reading CSV file: {e}'))
