# find.restful.api

## Standing up application on OS X

### Prerequisites

* Install/Update **Python** to version ~ 3.0 or higher
* Install/Update **Postgres** to version ~ 9.4.0 or higher
* Install/Update **Virtualenv** to version ~ 15.0.3 or higher
* **Link to blog post about setting this all up to be added later**

1. Create a development database on localhost named 'find_development'
2. Clone repository from find.restful.api master
3. Restore 'find_development' from backup
4. Configure the `settings.py` file
5. Inside the cloned repository
	* run `virtualenv env`
	* run `source env/bin/activate`
    * Note: you should have a (env) at the beginning of your terminal lines to show you activated the virutal environment
  * run `pip install -r requirements.txt`
6. Inside of the service directory
	* run `python manage.py migrate`
  * run `python manage.py runserver`

#### You should now be up and running on localhost:8000 -> you can check out the api docs at localhost:8000/docs

## CentOS

### Prerequisites

* Python 3.5+
* Git

### Running on CentOS

The process after cloning is done in a linux [screen](https://linux.die.net/man/1/screen) so it will run without terminating when you close your ssh connection. (NOTE this is not best practice should explore other options like systemd, containers, etc.)

```
git clone https://github.com/USStateDept/find.restful.api.git
screen
cd find.restful.api
pyvenv <environment-directory>
source <environment-directory>/bin/activate
pip install -r requirements.txt
gunicorn -b 127.0.0.1:8001 service/service.wsgi
```

To exit the screen you press **CTRL+A** then **D**
