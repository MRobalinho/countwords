How to Publish your API on Heroku
https://rapidapi.com/blog/how-to-build-an-api-in-python/


Documentation to deploy on Python
https://devcenter.heroku.com/categories/python-support


https://devcenter.heroku.com/articles/heroku-cli

https://devcenter.heroku.com/articles/python-runtimes

Heroku Setup
https://realpython.com/flask-by-example-part-1-project-setup/
=================

Anyone reading this: you'll need two files:

First file: requirements.txt containing something like: gunicorn==19.7.1 
or whatever the results of pip freeze > requirements.txt are.

Second file: Procfile containing something 
like: web: gunicorn app:app or potentially blank. 
Note that app:app in this example is a reference to your python filename. 
It means that every time a web process is declared, and a dyno of this type is started, 
also run the command gunicorn app:app to start your web server.

Then  $git add . 
After $git commit -m "added Procfile and requirements.txt"

Then run $git push heroku master     ( to push from your local master branch to the heroku remote.)

====================================================================
Sequencia de comendos para Deploy no HEROKU

Criando repositório git:
$ git init

Adiciona e "commitando" no repositório iniciado:
$ git add .
$ git commit -m "first commit"

Logo após:
$ heroku create
$ git push -m master

----
Notas:
De acordo com a documentação do Heroku eles apenas suportam 
as versões 3.7.1, 3.6.7 e 2.7.15 do Python. 
O projeto deve utilizar a versão 3.7.1

$ python -V    para ver a versão instalada

$pip install python==3.7.1

$cat runtime.txt
python-3.8.1
===========================================================================
Instalation/deploy log files on:
>%LOCALAPPDATA%\heroku\error.log
===========================================================================
Heroku Setup
https://realpython.com/flask-by-example-part-1-project-setup/

1. Once done, create a Procfile in your project’s root directory with this line:
   web: gunicorn app:app

2. Make sure to add gunicorn to your requirments.txt file
	$ python -m pip install gunicorn==20.0.4
	$ python -m pip freeze > requirements.txt

3. Create runtime.txt
	We also need to specify a Python version so that Heroku uses the right
	Python Runtime to run our app with. Simply create a file called runtime.txt 
	with the following code:
	
	python-3.8.1

4.Commit your changes in git (and optionally push to Github), then create two new Heroku apps.

One for production:
	a) $ heroku create wordcount-pro
	b) Add your new apps to your git remotes. Make sure to name one remote pro (for “production”) 
	   $ git remote add pro git@heroku.com:YOUR_APP_NAME.git
	c) Now we can push both of our apps live to Heroku.
	   $ git push pro master
	
--------------------
https://whispering-sierra-76906.herokuapp.com/

$heroku logs --tail     to see the errors log