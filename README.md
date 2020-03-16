1- `sudo apt-get update && sudo apt-get -y upgrade`
2- `sudo apt-get install python3`
and Check if you have python3
`python3 -V`
Then, install pip3
Run `sudo apt-get install -y python3-pip`
Check from installation of pip3
Run `pip3 -V`

install virtualenv
Run `pip3 install virtualenv`

Run `virtualenv env`

Then run `env/bin/activate` To active ENV
after activate it now install django `pip3 install django`

Go to project dir
Now the projects Can run
RUN server `python3 manage.py runserver` 

To open admin panel
run the command `python3 manage.py createsuperuser`
Type name, skip Email and type password

Now RUN server `python3 manage.py runserver` 
Go to the link on server

Now go to admin page from homepage and write your name and password

