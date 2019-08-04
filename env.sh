read -p "SECRET_KEY:" SECRET_KEY
read -p "NAME:" NAME
read -p "HOST:" HOST
read -p "USER:" USER
read -p "PORT:" PORT
read -p "PASSWORD:" PASSWORD

heroku config:add SECRET_KEY="${SECRET_KEY}"
heroku config:add NAME="${NAME}"
heroku config:add HOST="${HOST}"
heroku config:add USER="${USER}"
heroku config:add PORT="${PORT}"
heroku config:add PASSWORD="${PASSWORD}"
heroku config:set DISABLE_COLLECTSTATIC=1