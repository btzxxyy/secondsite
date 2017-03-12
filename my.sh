uwsgi --http :8001 --chdir /home/Crescent/py_code/myProject/secondsite/ --wsgi-file secondsite/wsgi.py --master --processes 4 --threads 2 --stats 0.0.0.0:8080
