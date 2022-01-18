# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: 10 min

### Prerequisites:

In order to complete this tutorial, you will need to have an Ubuntu 20.04 server with a non-root sudo-enabled user account and a basic firewall. This can be configured using our initial server setup guide for Ubuntu 20.04.

1. Update the package manager cache with
    ```
    $ sudo apt update
    ```
2. Install Apache
    ```
    $ sudo apt install apache2
    ```
3. Allow traffic on port 80 with
    ```
    $ sudo ufw allow in "Apache"
    ```


### Resources
* https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04

---

Accurate as of (last update): 2022-01-13

#### Contributors:  
Ella Krechmer, pd1  
Ivan Lam, pd1  
