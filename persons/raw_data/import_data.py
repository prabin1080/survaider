import csv
import json
import os
import re

from persons.models import Person

RAW_DATA_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_FILE_PATH = os.path.join(RAW_DATA_DIR, 'adult_dataset.csv')

JSON_FILE_PATH = os.path.join(RAW_DATA_DIR, 'adult_dataset_meta.json')


relationship_indexes = {'Husband':1, 'Wife':2, 'Own-child':3, 'Other-relative':4, 'Not-in-family':5, 'Unmarried':6}
sex_indexes = {'Male':1, 'Female':2}
race_indexes = {'White':1, 'Black':2, 'Asian-Pac-Islander':3, 'Amer-Indian-Eskimo':4, 'Other':5}

def import_data():
    with open(CSV_FILE_PATH) as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader):
            for key, value in row.items():
                row[key] = value.strip()
            print(index, row)
            row['relationship'] = relationship_indexes[row['relationship']]
            row['sex'] = sex_indexes[row['sex']]
            row['race'] = race_indexes[row['race']]
            row['salary_range'], row['salary'] = re.match(r'([<>]=?|==)(\d+)', row['salary']).groups()
            Person.objects.create(**row)


def get_meta_info():
    data = {"sex":[], "race":[], "relationship":[]}
    with open(CSV_FILE_PATH) as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader):
            for key, value in row.items():
                row[key] = value.strip()
            print(index, row)
            if not row['sex'] in data['sex']:
                data['sex'].append(row['sex'])
            if not row['race'] in data['race']:
                data['race'].append(row['race'])
            if not row['relationship'] in data['relationship']:
                data['relationship'].append(row['relationship'])
    with open(JSON_FILE_PATH, 'w') as outfile:
        json.dump(data, outfile)


# from persons.raw_data.import_data import get_meta_info