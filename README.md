## Readme for Logs Analysis Project

## Summary
 The logs analysis was an internal reporting tool that used information from the news database to discover what kind of articles the site's readers liked.  The program was designed to run in the command line without any input from the user. 
The report answers three questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
## Installation
1. Download and Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. Download and Install [Vagrant](https://www.vagrantup.com/downloads.html)
3. Fork or Clone this repository
4. Move news.py into the /vagrant directory of your file system
5. Download newsdate.sql and ensure it is in the /vagrant directory
6. Navigate to the /vagrant directory inside of the command line and run `vagrant up` to start the virtual machine
8. Run `vagrant ssh` to log into the virtual machine
9. Run `psql -d news -f newsdata.sql` to create the database
10. Run `python news.py` to run program

