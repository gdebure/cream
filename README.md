CREAM (Company REsources Administration and Management) is a Suite allowing you to manage several aspects of your company

It is currently composed of several modules:
* Users: allows to define attributes for employees in the company
  * Employees
* Projects: define attributes for the projects in your company
  * Projects
  * Deliverables
  * Deliverables Volumes
* Services: Define your company's service catalogue
  * Domains
  * Service Family
  * Services
* Qualifications : Define your company's skills catalogue, related jobs and positions
  * Skill Categories
  * Skills
  * Jobs
  * Positions
  * Profiles
  * Employee Skills
  * Job Profile Skills
  * Employee Positions

CREAM is written in Python, based on the Django web framework : https://www.djangoproject.com/

# Prerequisites

## Install Django

As per any web database application, Django will need:
* A web server (Apache, nginx, lighttpd...)
* A database server (Postgresql, mariadb, mySQL...)

The Django documentation lists everything you need to know to get Django running on your server.
The typically recommended setup for the server would be:
* linux
* Apache with mod_wsgiscalable vector icons
* Postgresql

Please refer to the Django documentation (https://docs.djangoproject.com/en/1.7/topics/install/) for more details

## Cream Specificities

On top of basic Django installation, CREAM needs a few more components enhancing functionality or look & Feel.

* Guardian (http://pythonhosted.org/django-guardian/) : object permissions for Django. Refer to Guardian documentation for installation instructions.
* Reversion (https://github.com/etianen/django-reversion) : version control facilities. Refer to Guardian documentation for installation instructions. 
* jquery (http://jquery.com/) : fast, small, and feature-rich JavaScript library. Download and Unzip the archive in CREAM/CREAM/static/jquery
* Bootstrap 3.x (http://getbootstrap.com/) : CSS framework for faster and easier web development.
* font-awesome (http://fontawesome.io/) : scalable vector icons. Download and Unzip the archive in CREAM/CREAM/static/font-awesome
* Datatables (http://datatables.net/) : advanced interaction controls for HTML table (sorting, filtering...). Download and Unzip the archive in CREAM/CREAM/static/datatables
* Bootstrap Datepicker (https://github.com/eternicode/bootstrap-datepicker) : A JavaScript Datepicker for bootstrap. Download and Unzip the archive in CREAM/CREAM/static/bootstrap-datepicker

# Installing CREAM

Please follow instructions on how to deploy a Django Application : https://docs.djangoproject.com/en/1.7/howto/deployment/

Once completed, proceed to the following steps.

## Settings

CREAM settings are stored in a single file located in CREAM/CREAM/settings.py. Some of the values there need to be updated for your CREAM instance :
* DEBUG : when deploying in production environment, set this to False. Refer to Django documentation for more explanation
* ADMINS : add as many email adresses you want for application administrators.
* DATABASES : update the values for your choice of database

Additionally, CREAM needs to know a mail server (SMTP) for sending the notifications. These values can be found at the end of the settings.py file :
* EMAIL_HOST : name or IP adress of the SMTP server
* EMAIL_PORT : port for the SMTP server
* EMAIL_SUBJECT_PREFIX : string added at the beginning of all email titles sent by CREAM.

## Create Database

CREAM can create automatically the tables, but it needs the Database to be manually created first. Create a database on your database server, consistent with the values defined in the settings.py file.

Once this is completed, Django can create the tables automatically by entering the following command in a shell :
    python2 manage.py migrate

Django will propose to create an administrator account, which you should accept as it will allow you accessing CREAM from your browser.

## Login and create data

Open your browser at the URL you defined for CREAM on your webserver, then login with the administrator account you just created.

**BUG**
There is currently a bug that displays an error message right after login. This is due to the fact that there is no Employee defined for the User logged in. As a workaround simply change the URL to http://yourserver.com/admin, and create a new Employee for the only existing User so far.
Later, remember to always create an Employee for every User you add to the database.

Start creating data, starting with Domains, Service Families, and Services, then Projects, Deliverables, and Deliverable Volumes