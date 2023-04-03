# To install

`virtualenv homesuitehome`
`cd homesuitehome`

activate your virtual environment...

`. bin/activate`

from here, clone the repo from github, and then cd into the git repo.

install the requirements...

`pip install -r requirements.txt`

create your testing sqlite db

`python manage.py makemigrations`

create an initial super user

`python manage.py createsuperuser`

(follow prompts to create the first uer)

start your development server

`python manage.py runserver`

now go to `http://localhost:8000` in your browser and login with the superuser you created.

You are up and running!
