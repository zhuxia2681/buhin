#!/bin/bash
bash clr.sh
python3 manage.py makemigrations anken
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
