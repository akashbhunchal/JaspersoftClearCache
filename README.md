JaspersoftClearCache
====================

On demand Ad hoc cache clearing using Django and Selenium

Project to clear/build Jaspersoft Adhoc Cache through an HTTP endpoint. The webframework is Django and Selenium is used to simulate user behavior like login, opening repositories. It contains both Windows and Linux port. Note that we need a desktop environment to run it on Linux. It would not work on Linux with no Desktop environment.

### Important Files

####urls.csv
This file is used to create cache build selenium script. If you want to prewarm your cache for the reports, then put them (report urls) here one below the other. For eg the file would look something like:

<url1>,10000
<url2>,10000
......


10000 is the number of milliseconds selenium script would wait for the report to load. One good feature of Jaspersoft is that db query is not killed even if the user exits the reports url. Do not put it below 10000 as sometime the page load itself takes about 10 secs. Increase it if you see cache miss.

####properties.py

Contains some Jasperserver Info. The comments in the script are self explainatory.

####web_app/settings.py

The only variable to be modified here are 

BASE_PATH
ROOT_DOMAIN

Example paths are already there in the source.

### How to use

##### Create the cache build script

1) Enter all the report urls as explained above in urls.csv
2) python build_cache_script.py

##### Start the Django server
I tried using an app server like uwsgi, but somehow the server was not able to launch selenium server. So I go with development server itself.

python manage.py runserver 0.0.0.0:8000

##### End point to call to clear cache

<domain>:8000/clear_cache

##### End point to monitor the web application

<domain>:8000/status

#Windows port coming soon :)
