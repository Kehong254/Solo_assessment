# Volcano Shopping Website
This is a shopping site for volcanoes based on the Django framework. Users can select their favourite volcanoes on the site, add them to their shopping cart and finally place their orders.

The site consists of two main applications: *accounts and Shopping_app*。

## Database
The site, with data from Kaggle, contains a detailed list of every volcano that has ever existed on Earth.<https://www.kaggle.com/datasets/deepcontractor/the-volcanoes-of-earth>

## Function
Users can access the site at login or as a visitor. The website includes the following features:

### Registration
New users can register an account on the website and once registered, users can create their own shopping cart.

### Search
The site supports searches by volcano name, country and type of volcano so that users can quickly find the volcano they are looking for.

### Shopping Cart
Users can add their favourite volcanoes to the shopping cart, view the name, quantity, price and total price of the items, and change the number of items in the cart.

### Place an order
The user can place an order in the shopping cart and enter their address so that the merchant can deliver the goods to the address specified by the user. Once the order is submitted, the order details are displayed, including the order number, product name, product quantity, product price and total price.

## How our Project Application was Created
Clone this warehouse locally to: <git@github.com:Kehong254/Solo_assessment.git>
````
pyenv local 3.10.7 # this sets the local version of python to 3.10.7
python3 -m venv .venv # this creates the virtual environment for you
source .venv/bin/activate # this activates the virtual environment
pip install django==4.1.2
````
Created a website for my application using the django management tool with the following command;
````
django-admin startproject Shopping_app, accounts
````


ALLOWED_HOSTS is one of the security settings for Django applications, and is used to restrict the hostnames or IP addresses allowed to access the application. CSRF_TRUSTED_ORIGINS, on the other hand, is the code used in Django to configure CSRF protection, specifying which sources are trusted to access the application.
````
ALLOWED_HOSTS = ['faxnylon-opinionvitamin-8000.codio-box.uk']
CSRF_TRUSTED_ORIGINS = ['https://faxnylon-opinionvitamin-8000.codio-box.uk']
````


Load the application in INSTALLED_APPS：
````

    'Shopping_app',
'accounts',
````
This code is the configuration for setting the path to the static file in a Django project, and it tells Django where to look for the static file. In this example, the static files are stored in the Shopping_app/static folder in the root of the project, and STATIC_URL is the URL path used to access the static files in HTML。
````
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Shopping_app', 'static')
]
````
To configure our database, this command was run in the terminal
````
python3 manage.py migrate 
````
Once you have done all of the above, start the server in a terminal with the following command:
````
python3 manage.py runserver 0.0.0.0:8000
````
## Web Application Creation
After creating the 'Shopping_app' a folder containing our downloaded data file 'The_Volcanoes_Of_Earth.csv' was created in it. It was used to develop our application.

My application 'Shopping_app' was added to the settings.py located under 'INSTALLED_APP'. This makes it possible to know that such an application exists.
````
from django.db import models
from django.conf import settings

class Volcano(models.Model):
  Volcano_ID = models.IntegerField(primary_key=True, unique=True)
  Volcano_Name = models.CharField(max_length=100)
  Volcano_Image = models.URLField(max_length=100)
  Volcano_Type = models.CharField(max_length=100)
  Country = models.CharField(max_length=100)
  epoch_period = models.CharField(max_length=100)
  Latitude = models.CharField(max_length=50)
  Longitude = models.CharField(max_length=50)
  price = models.FloatField()
  quantity = models.PositiveIntegerField()
  

  def __str__(self):
      return f'{self.Volcano_ID}, {self.Volcano_Name}, {self.Volcano_Type}, {self.Country}, {self.Latitude}, {self.Longitude}'
````
Now, to generate a migration file for Django to use it loads the model into the schema, we need to ask Django to read the model.py file, generate a migration file and finally run the generated migration with the below commands by running them one after the other:
````
python3 manage.py makemigrations Shopping_app 

python3 manage.py migrate Shoppings_app
````

## Application Views Creation
To visualise my app tables and other tables, we made some inputs in 'urls.py' under 'Shopping_app'. The urls.py file under our 'mysite' was created for the urls path fixed within 'urls.py' of 'Shopping_app' to facilitate communication between the two URLS. In addition, a views.py file was created with the information details to be passed to the urls.py file for the Shopping_app. This makes it possible and very easy to display the front end of the HTMLs table.

### My templates have the following HTML files
cart.html
checkout.html
create_empty_cart.html
error.html
main.html
order_confirmation.html
store.html
volcano_detail.html
login.html
register.html

### CSS and Bootstrap
I used Bootstrap to provide the basis for the styling of the application. We also used CSS to enhance the styling.

### Test

behave is a Python testing framework for Behavior-Driven Development (BDD). behave_test refers to test cases written using the behave framework.

BDD is an agile software development methodology that helps project team members better understand requirements and accurately determine whether system behaviour meets expectations by analysing and describing system behaviour. behave framework applies BDD thinking to a Python testing framework, providing a structured way to write and run test cases. Using behave_test, developers can more easily write more readable test cases and better maintain and extend test cases.

## Running the application
#### Codio
This application can be run directly in Codio using the following commands in the terminal:
````
cd Solo_assessment/
source .venv/bin/activate
python3 manage.py runserver 0.0.0.0:8000
````
Clicking the 'Box URL' tab at the top of the screen should launch the homepage of the application in a new browser tab.

#### render
Link: <https://kehong-assessment.onrender.com>


