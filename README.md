# django-shop | model > serializer > endpoint 

A mini-project set by a web agency to create a basic python-django app and using the power of django rest framework to finish the build with an API endpoint.

Assumptions:

1. python v3.6.9
2. django v3.1.3


## Table of Contents

1. [Information Architecture](#information-architecture)
    * [Application Framework](#application-framework)
    * [Database Selection](#database-selection)
    * [Data Models](#data-models)
2. [Technologies Applied](#technologies-applied)
    * [Databases](#databases)
    * [Languages](#languages)
    * [Tools](#tools)
3. [Tests](#tests)
4. [Credits](#credits)
    * [Content](#content)

## Information Architecture
### Application Framework
Django application framework was a prerequisite in the design of this mini-project, according to the project brief.

### Database Selection
Django framework is fast, secure and scalable. Provides a dynamic CRUD (create, read, update and delete) interface, configured with admin models and generated via introspection. requiring SQL database 
 - SQLITE3 database was used for development of this project on my local machine  

### Data Models

#### shop app model
Name            |  Field Type          | Validation
----------------|----------------------|---------------------------------------------
Name            | CharField            | max_length=200
Address         | TextField            | blank=True
Rating          | PositiveIntegerField | default=2, blank=True, null=True


## Technologies Applied
### Databases
•	[SQLite3](https://www.sqlite.org/index.html) provided by Django for a developemnt database

### Languages
•	[HTML](https://html.spec.whatwg.org/multipage/) used as the markup language

•	[CSS3](https://www.w3.org/Style/CSS/) used to style the HTML

•	[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) used mostly for DOM manipulation

•	[Python](https://www.python.org/) used to run the backend application


### Tools
•	[AWS Cloud9](https://aws.amazon.com/cloud9/) a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser.

•	[Django](https://www.djangoproject.com/) high-level Python Web framework that encourages rapid development and clean, pragmatic design

•	[Git](https://git-scm.com/) is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

•	[GitHub](https://github.com/) is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

•	[PEP8](http://pep8online.com/) checks python code to ensure compliance with PEP8 requirements. PEP8 is the latest accepted standard code structure convention  

•	[PIP](https://pip.pypa.io/en/stable/installing/) enabling installation of tools and packages required for this project to function correctly


## Tests
Tests were written in the shop app directory. Tests were primarily built arounf equal assertion on data fields and browser rendering.

## Credits

### Content

- [django models](https://www.django-rest-framework.org/) provides information on REST framework and installation using `pip`

- [ViewSets & Routers](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/) helped with build of both `urls.py` & `views.py` files

- [model fields](https://docs.djangoproject.com/en/3.1/ref/models/fields/) reference material was useful reminder on building out my shop model.

- [ModelSerializer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer) write up is useful as a reminder on building out this model type

- [Serializer Fields](https://www.django-rest-framework.org/api-guide/fields/) was a useful reminder on the build out of the serializer model and inherent content 


*This is for educational use.* 
