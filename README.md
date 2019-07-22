# survaider

1.  Create Postgres Database "survaider" with User "dbadmin" and Password "pass1234"
2.  Create a virtualenvironment with python3
3.  Install the requirements with `pip install -r requirements.txt`
4.  Migrate Database with `./manage.py migrate`
4.  Open Django shell with `./manage.py shell`
5.  The following will copy data into the database from the csv file
    - `from persons.raw_data.import_data import import_data`
    - `import_data()`
6.  Run the server with `./manage.py runserver`
7.  Check the following urls for apis
    - GET [/api/person/?sex=1&race=2&relationship=4](/api/person/?sex=1&race=2&relationship=4)
    - GET [/api/person/sex-graph/](/api/person/sex-graph/)
    - GET [/api/person/relationship-graph/](/api/person/relationship-graph/)
