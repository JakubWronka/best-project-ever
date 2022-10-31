echo "Inside docker-entrypoint script"

python manage.py makemigrations
python manage.py migrate
# to have the same initial state of database it will be loaded from file "dumped_db.json":
echo "In a moment initial state of database will be loaded"
python manage.py loaddata dumped_db.json
echo "Initial state of database from file 'dumped_db.json has been loaded"
python manage.py runserver 0.0.0.0:8000

echo "Finishing docker-entrypoint script"