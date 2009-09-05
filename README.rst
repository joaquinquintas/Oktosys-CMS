OCBC CYCLE SINGAPORE 2010
=========================

This project is mainly written in Python using the Django framework.

Environment Setup
-----------------

Prerequisites: Python, Git, Subversion and virtualenv.

#. Setup virtual environment and activate it::

    virtualenv cycle
    cd cycle; source bin/activate

#. Install pip and mercurial inside the virtualenv::
    
    easy_install pip mercurial

#. Clone the github project into src::
    
    git clone git@github.com:kennyshen/Oktosys-CMS.git src

#. Install the project requirements, this will install Django and the
   required apps::

    pip install -r src/requirements.txt

#. Go to the project directory::

    cd src/myproject

#. Create a local settings file::

    touch local_settings.py

Edit it to reflect your settings, at least:
DATABASE_ENGINE, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD

#. Create database, validate and smile::

    ./manage.py syncdb
    ./manage.py validate
 
