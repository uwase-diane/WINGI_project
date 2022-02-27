# Application name

# WINGI STORE


# Author

Uwase Diane

## Description

This application is an ecomerce platform where merchants can create their own store and share therir products to their consumers. the merchants can then edit these products.

## Dependencies

asgiref==3.5.0
beautifulsoup4==4.10.0
bootstrap4==0.1.0
certifi==2021.10.8
cffi==1.15.0
charset-normalizer==2.0.12
cryptography==36.0.1
defusedxml==0.7.1
Django==4.0.2
django-allauth==0.49.0
django-bootstrap4==21.2
django-crispy-forms==1.14.0
idna==3.3
oauthlib==3.2.0
Pillow==9.0.1
pycparser==2.21
PyJWT==2.3.0
python3-openid==3.2.0
requests==2.27.1
requests-oauthlib==1.3.1
soupsieve==2.3.1
sqlparse==0.4.2
tzdata==2021.5
urllib3==1.26.8

## Setup/Installation Requirements
Clone this repository and navigate to the folder. Run the following commands to allow functionality of the app:-
 you need to have python3.9 installed, it not install it.
on windows machine

set your virutal environment:
py -m venv virtual
.\virtual\Scripts\activate

install Django:

pip install Django

Install the project dependencies:

pip install -r requirements.txt

then run:

python manage.py makemigations
python manage.py migrate
python manage.py createsuperuser

to start the development server:
python manage.py runserver


# User stories

merchants

create an account by signing up then login
they are able to add their products
they are able to remove their products
they are able to update their products
they are able to search products by their title

customers

create an account to be able to add/remove products in their cart
they are add a product in the create
they are able remove the all products in the cart
they are able to remove a single product in a cart

## Technologies Used
Python 3.9
Bootstrap
Django Framework


## Support and contact details
email: diane.uwase13@gmail.com

## License

Copyright 2022 Uwase Diane
