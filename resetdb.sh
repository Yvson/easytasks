#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py loadmass --path conversor/measurements/mass.csv
python manage.py loadlength --path conversor/measurements/length.csv
python manage.py loadtime --path conversor/measurements/time.csv
python manage.py loadarea --path conversor/measurements/area.csv
python manage.py loadvolume --path conversor/measurements/volume.csv
python manage.py loadacceleration --path conversor/measurements/acceleration.csv
python manage.py loadforce --path conversor/measurements/force.csv
python manage.py loadvelocity --path conversor/measurements/velocity.csv
python manage.py loadtemperature --path conversor/measurements/temperature.csv
python manage.py loadpressure --path conversor/measurements/pressure.csv

