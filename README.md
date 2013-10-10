
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
8. `ifconfig`. Take note of the ip. 
8. `cd synced/code/`
9. `cqlsh <ip> < install.cql` ( using the machine's IP, 
    the public 192.168.X.X one, not the private 10.X.X.X one )
11. `python main.py` .
12. Open a browser and visit <ip>:5000
13. Type in <ip>:5000/http://curtis.lassam.net 
14. To create a second machine, open machine_2/Vagrantfile
15. Replace the IP in the line `:seeds => [ '192.168.1.86' ]` 
    with the IP of the first server.  
16. `vagrant up`
17. `vagrant ssh`
18. `cd synced/code/`
19. `python main.py` . This ip is now serving the URL service as well. 
20. To create machine_3, just copy machine_2's Vagrantfile into a new folder


Todo
----

* Some kind of security? I'm like 90% sure publicly accessible DB and
   publicly modifiable URL safety data is not kosher. 
* Script to generate urls to cram down the service's throat
* Report on the service's capacity and load to determine when to create
    new services. 
* Put up servers. Take down servers. How flexible is this thing? 
