This is an API developed in Flask, SqlAlchemy and Sqlite
To use it locally,

clone the app
got to project folder
create virtual env using 'python{your-version) -m venv env'
Activates the virtual environment using 'source env/bin/activate'
Install all dependencies
pip install -r requirements.txt


Start Server using 'python run.py

Endpoints:

Get Categories : 
URI	http://127.0.0.1:5000/api/Category

Post/Create Category: 
URI:	http://127.0.0.1:5000/api/Category
BODY:	{
	"name":"category5"
	}

Create/Post Comment:
URI:	http://127.0.0.1:5000/api/Comment
BODY:	{
	"category_id":2,
	"comment":"comment2"
	}

Full Detail is given here:
https://www.codementor.io/dongido/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx
