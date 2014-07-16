How to run this project using the built in Django server:

change to the root project directory

Run the following commands:

vagrant up
vagrant ssh
sudo apt-get update
sudo apt-get install python-pip
sudo pip install Django==1.6.5

cd /mnt/data/testsite/
//this will start the server in the VM listening on all interfaces
python manage.py runserver 0.0.0.0:8000

Now go back to you local machine and open a browser.
Navigate to localhost:8000/admin
Yes, it is localhost. The VM has port 8000 forwarded to your host machine's port 8000.
This can be changed in the VagrantFile config.

username: admin
password: drowssap
