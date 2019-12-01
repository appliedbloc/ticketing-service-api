ticketing_service_api
=============

Flask RestPlus powered ticketing service API to manage tickets, associated clients, garments and tasks within the Tailored Industries production process. This service is currently the first candidate for the workflow orchestration initiative.  

## Current startup instructions:
* Make sure you have ```Python``` (with ```Virtualenv```), ```Git``` installed on your local machine. For the purpose of this project we will utilize ```Python 3.x```.
* Clone the repository to you local working directory of choice:
```git clone https://github.com/appliedbloc/ticketing-service-api.git```
* Create a new virtual environment in the ```venv``` directory: 
    * ```virtualenv -p `which python 3` venv```
    * ```source venv/bin/activate```
    * ```(venv) $ pip install -r requirements.txt```

* Finalize development setup (as an IDE configuration or directly via a Terminal): 
    * ```(venv) $ python setup.py develop```

* Start the application: 
    * ```(venv) $ python ticketing_service/app.py```
    
    
If you are making changes to the database schema as a part of your development efforts and you want to reset the database to an empty state (or if you accidentally deleted ```db.sqlite```) use the ```reset_db.py``` script as follows:
* ```(venv) $ python reset_db.py```
* ```(venv) $ python setup.py develop```

## Current TODOs:
* Update entity deletion logic to also delete all nested entities (i.e. if the ticket was deleted all associated garment, customers and tasks need to be deleted). 
* Create validation module to sanitize ```POST``` request payloads.
* Create a fleet of fixtures in ```./conftest.py``` to be reused across unit tests.
* Replace current dummy unit tests with the actual ones.
* Integrate ```pytest-cov``` plugin to have direct access to test coverage reports.
* Integrate ```gunicorn``` instead of native Flask logging to have production-ready logging pipeline.
* Code cleanup.



