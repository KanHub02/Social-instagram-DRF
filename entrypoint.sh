python3 manage.py makemigrations --noinput
python3 manage.py migrate 
python3 manage.py collectstatic
python3 manage.py create_adminuser
python3 manage.py create_users 
python3 manage.py create_posts
python3 manage.py add_like 
python3 manage.py add_comment 
gunicorn config.wsgi.application --reload 0.0.0.0:8888