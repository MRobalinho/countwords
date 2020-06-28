# countwords

Count words from a text and calcule the seconds to read this text.

API to deploy at HEROKU

Anyone reading this: you'll need 3 files:
1.First file: requirements.txt containing something like: gunicorn==19.7.1 
or whatever the results of pip freeze > requirements.txt are.

2.Second file: Procfile containing something 
like: web: gunicorn app:app or potentially blank.  (Note that app:app in this example is a reference to your python filename. )
It means that every time a web process is declared, and a dyno of this type is started, 
also run the command gunicorn app:app to start your web server.

3.Can inform the python version on runtime.txt with a text: python-3.8.1

NOW THE DEPLOY:
a)  $ git add . 
b) $ git commit -m "added Procfile and requirements.txt"
c) $ git push heroku master     ( to push from your local master branch to the heroku remote.)

