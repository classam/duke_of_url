
What Is It?
-----------
Python & Cassandra url service. Give it a url, get some JSON. 

Why Cassandra? 
--------------
Distributed, scalable, high-performance, supports pretty easy clustering.

Why Python?
-----------
I'm most familiar with it. Not for performance reasons, certainly. 

Instructions
------------

1. Install VirtualBox
2. Install Vagrant
3. Install git. 
4. Git clone this. 
5. From the git shell, navigate to `<code_location>/machine_1` 
6. `vagrant up`
7. `vagrant ssh` or configure PuTTY to communicate with Vagrant
8. `cd synced/code/`
9. `cqlsh < install.cql`
10. `ipconfig` to find the IP - because we hope to set this up as a 
    cluster, we're not using VirtualBox's built-in NAT - instead, this
    computer exists on the public network. 
11. `python main.py`
12. Open a browser and visit <ip>:5000
13. Type in <ip>:5000/http://curtis.lassam.net 

Todo
----

* make sure the response has the 'application/JSON' mimetype 
* Move config options to an external file or environment variables
* Create machine_02
* Interface for adding new URL data 
