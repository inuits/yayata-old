# BETA

Back-End for Timesheet Application


## How to setup

    mkvirtualenv yata 
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py createsuperuser

## How to run in development

Consider changing `DEBUG=True` in `beta/settings.py` 

    workon yata
    python manage.py runserver


Currently the backend has broken interface and broken tests.
