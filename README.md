# Log-Analysis


### Project Overview

>This project explores large database with over a million rows by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. 

## Quick Start

### Prerequisites:

  * Should have version of python **3** or above , Installed in computer ([Download Python](https://www.python.org/downloads/))
  * Should have Vagrant installed in Computer ([Download Vagrant](https://www.vagrantup.com/))
  * Should have Vitual-box installed in Computer([Download VirtualBox](https://www.virtualbox.org/))

### Setup Project:

  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4. Unzip this file after downloading it. The file inside is newsdata.sql.
  
### Launching the Virtual Machine:

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant and look around with ls.
  
### Setting up the database and Creating Views:

  1. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.
  
  2. Use `psql -d news` to connect to database.
  
  3. Create vier error_log_view using:
  ```
    create view error_log_view as select date(time),round(100.0*sum(case log.status when '200 OK' 
    then 0 else 1 end)/count(log.status),2) as "Percent Error" from log group by date(time) 
    order by "Percent Error" desc;
  ```
  | Column        | Type    |
  | :-------      | :-------|
  | date          | date    |
  | Percent Error | float   |
  
### Running the queries:
  1. From the vagrant directory inside the virtual machine,run reportingtool.py using:
  ```
    $ python3 reportingtool.py
  ```
  2. Enter (1 , 2 or 3), For respective queries .
  3. Again run reportingtool.py for running any other option .

### Download or Use 

  *  Github Repositories : [Log-Analysis](https://github.com/david-singh/Log-Analysis/)

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
