read -p "DJANGO_SECRET_KEY:" DJANGO_SECRET_KEY
read -p "DB_NAME:" DB_NAME
read -p "DB_HOST:" DB_HOST
read -p "DB_USER:" DB_USER
read -p "DB_PORT:" DB_PORT
read -p "DB_PASSWORD:" DB_PASSWORD

heroku config:add DJANGO_SECRET_KEY="${DJANGO_SECRET_KEY}"
heroku config:add DB_NAME="${DB_NAME}"
heroku config:add DB_HOST="${DB_HOST}"
heroku config:add DB_USER="${DB_USER}"
heroku config:add DB_PORT="${DB_PORT}"
heroku config:add DB_PASSWORD="${DB_PASSWORD}"
heroku config:set DISABLE_COLLECTSTATIC=1