# Welcome to find.restful.api

To see our repository on GitHub visit [here](https://github.com/USStateDept/find.restful.api).

## Data We Provide

Data we supply is derived from a collection of publicly-available third-party sources – World Bank,
United Nations, Freedom House, etc. -- about the state of countries around the world. For instance,
you can use our API to determine maternal mortality rates in a particular country, or to find out 
how many people in a set of countries have access to credit.

You can retreive all kinds of data pertaining to categories, countries, indicators, and regions.
With the data you want from each country and region you can then retreive data value for each
indicator you specify and for which year or years.

## Passing Parameters through the URL

Our API can handle many types of GET requests that will return a broad range of public data.
However you want to requests and retreive that data will be based on the parameters you pass through the URL.
Each endpoint we have provided will allow you to pass through specific fields and value in query string format.
For each end point here are the fields the endpoint looks for:

    - categories/?category=<value1>&subcategory=<value2>
    - countries/?country=<value1>
    - countries/data/?country<value1>&indicator<value2>&year=<value3>
    - indicators/?indicator=<value1>
    - regions/?region=<value1>
    - regions/data/?region=<value1>&indicator=<value2>&year=<value3>

A quick thing to note is that when you are requesting multiple values for a specific field in the URL you must use a | **(pipe)**.
This will allow you to GET multiple countries `/?country=<value1>|<value2>`, etc.  Also note that when you are requesting the endpoints
at countries/data/ and regions/data/ to get data for **all** the years you do not need to specify a year field - it will default to 'all'.

## API Endpoints

    categories/
        list/
    countries/
        list/
    countries/data/
    indicators/
        list/
    regions/
        list/
    region/data/

## Signing Up For Tokens

To register an account and receive a token you must first go to the registration page and enter a requested username, your email, and a password
for your account.  Once you sign up you will receive a verification email.  Once you have verified your account you can then login using your 
credentials.  After you successfully log in you will see a token that is unique to your account.  This token will expire in **90 days** - to get a
new token you can either refresh your token or you can login again with your credentials.