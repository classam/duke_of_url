
What Is It?
-----------
Python & Cassandra url service. Give it a url, get some JSON. 

Why Cassandra? 
--------------
Distributed, scalable, high-performance, supports pretty easy clustering.

Why Python?
-----------
I'm most familiar with it. 

Instructions
------------

1. Install VirtualBox
2. Install Vagrant
3. `vagrant up`
4. `vagrant ssh` or configure PuTTY to communicate with Vagrant
5. `cd synced/code/`
6. `cqlsh < install.cql`
7. `ipconfig` to find the IP - because we hope to set this up as a 
    cluster, we're not using VirtualBox's built-in NAT - instead, this
    computer exists on the public network. 
8. `python main.py`
9. Open a browser and visit <ip>:5000
10. Type in <ip>:5000/url 

Todo
----

* `/<url>` is not in the spec, the spec says: `/urlinfo/1/{hostname&port}/{path}`
  * what's that 1 for? 
  * hostname & port like 'curtis.lassam.net:9999' I imagine
  * path like the path to the data on the host - 'post/2013_09_24-Cube_Drone_67__Prank.html'
* add separate 'host' and 'post' values to Cassandra
* Move config options to an external file or environment variables
* Create machine_02
* Interface for adding new URL data 
