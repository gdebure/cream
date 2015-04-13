**CREAM** (Company REsources Administration and Management) is a Suite allowing you to manage several aspects of your company

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
* Apache with mod_wsgi, or gunicorn
* Postgresql or Mariadb (MySQL fork)

Please refer to the Django documentation (https://docs.djangoproject.com/en/1.7/topics/install/) for more details

## Cream Specificities

On top of basic Django installation, CREAM needs a few more components enhancing functionality or look & Feel.

django add-ons:
* Django-nvd3 (https://github.com/areski/django-nvd3) : html5 charts using d3.js. Refer to Django-nvd3 documentation for installation instructions.
* Django-bower (https://github.com/nvbn/django-bower) : Easy way to use bower with your django project.
  * Install node.js (http://nodejs.org/) first
  * then bower (http://bower.io/)
  * And finally django-bower

other components:
These components will be installed through django-bower, so you don't need to download them individually.
* jquery (http://jquery.com/) : fast, small, and feature-rich JavaScript library.
* Bootstrap 3.x (http://getbootstrap.com/) : CSS framework for faster and easier web development.
* font-awesome (http://fontawesome.io/) : scalable vector icons.
* Datatables (http://datatables.net/) : advanced interaction controls for HTML table (sorting, filtering...).
* Bootstrap Datepicker (https://github.com/eternicode/bootstrap-datepicker) : A JavaScript Datepicker for bootstrap. 
* respond.js (https://github.com/scottjehl/Respond) : enable responsive web designs in browsers that don't support CSS3 Media Queries - in particular, Internet Explorer 8 and under



# Installing CREAM

Please follow instructions on how to deploy a Django Application : https://docs.djangoproject.com/en/1.7/howto/deployment/

Once completed, proceed to the following steps.

## Settings

CREAM settings are stored in a single file located in CREAM/CREAM/settings.py. The values in that file won't need to be changed. Instead, you should create an instance_settings.py in the same folder. This is where  you should put your CREAM's instance settings. You may take as a reference the instance_settings_sample.py provided and change the values accordingly.

## Create Database

CREAM can create automatically the tables, but it needs the Database to be manually created first. Create a database on your database server, consistent with the values defined in the instance_settings.py file.

Once this is completed, Django can create the tables automatically by entering the following command in a shell :
    python2 manage.py migrate

Django will propose to create an administrator account, which you should accept as it will allow you accessing CREAM from your browser.

## Install additional dependencies

This step will install additional dependencies as described above. Ensure the machine is connected to Internet, and Enter the following command:
    python2 manage.py bower_install
    
Thanks to the BOWER_INSTALLED_APPS setting (in settings.py, you don't need to change that), this will call to bower to download and install all necessary components in the components folder

## Login and create data

Open your browser at the URL you defined for CREAM on your webserver, then login with the administrator account you just created.

**BUG**
There is currently a bug that displays an error message right after login. This is due to the fact that there is no Employee defined for the User logged in. As a workaround simply change the URL to http://yourserver.com/admin, and create a new Employee for the only existing User so far.
Later, remember to always create an Employee for every User you add to the database.

Start creating data, starting with Domains, Service Families, and Services, then Projects, Deliverables, and Deliverable Volumes