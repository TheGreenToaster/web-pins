web-pins
========

This is a simple interface for reading and controlling the GPIO pins on the Raspberry Pi

There are a few steps needed.

Installation
============

Install LAMP

>sudo su

>apt-get update && apt-get upgrade

>apt-get install apache2 php5 mysql-client mysql-server tomcat6 vsftpd

>cd /var/www



Install GPIO  Python library

>wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.1.0.tar.gz

>tar zxf RPi.GPIO-0.1.0.tar.gz

>cd RPi.GPIO-0.1.0

>sudo python setup.py install



While in the www directory clone the web-pins folder

>wget https://github.com/TheGreenToaster/web-pins.git

In order to allow the PHP to use the Python scripts the PHP user needs to be added to the sudoers file.

To enter the sudoers file use the command

>sudo visudo

Next add the fallowing line to the end of the file and save it

>www-data ALL=(ALL) NOPASSWD: ALL

Usage
=====

In order to read the 0 pin the url is.

>raspberrypiaddress/pi-read.php?pin=0

Simply replace the "0" with and number 0-7 to read that pin.


In order to set the value of pin 0 to high the url is.

>raspberrypiaddress/pi-write.php?io=1&pin=0

To set value to low change 

>io=1

to

>io=0

The "raspberrypiaddress"should be changed to the IP address of your pi.

