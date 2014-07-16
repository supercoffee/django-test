**How to run this project using the built in Django server:**<br>

change to the root project directory<br>

Run the following commands:<br>

vagrant up<br>
vagrant ssh<br>
sudo apt-get update<br>
sudo apt-get install python-pip<br>
sudo pip install Django==1.6.5<br>

cd /mnt/data/testsite/<br>
//this will start the server in the VM listening on all interfaces<br>
python manage.py runserver 0.0.0.0:8000<br>

Now go back to you local machine and open a browser.<br>
Navigate to localhost:8000/adminv
Yes, it is localhost. The VM has port 8000 forwarded to your host machine's port 8000.<br>
This can be changed in the VagrantFile config.<br>

username: admin<br>
password: drowssap<br>
