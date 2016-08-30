# find.restful.api

## Standing up application on OS X

#### Prerequisites

* Install/Update **Python** to version ~ 3.0 or higher
* Install/Update **Postgres** to version ~ 9.4.0 or higher
* Install/Update **Virtualenv** to version ~ 15.0.3 or higher
* **Link to blog post about setting this all up to be added later**

1. Create a development database on localhost named 'find_development'
2. Clone repository from find.restful.api master
3. Restore 'find_development' from backup
4. Inside the cloned repository
	* run `virtualenv env` 
	* run `source env/bin/activate`
    * Note: you should have a (env) at the beginning of your terminal lines to show you activated the virutal environment
5. Inside of the service directory
	* run `python manage.py migrate`
  * run `python manage.py runserver`

#### You should now be up and running on localhost:8000 -> you can check out the api docs at localhost:8000/docs