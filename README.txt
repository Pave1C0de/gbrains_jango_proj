1
delete db.sqlite3
delete migrations/0001_initial.py
2
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py fill
