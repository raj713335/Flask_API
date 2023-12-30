# Flask_API

## Docker 

```commandline
$ docker build -t rest-apis-flask-python .
$ docker run -d -p 5000:5000 rest-apis-flask-python
$ docker run -d -p 5000:5000 -w /app -v "$(pwd):/app" rest-apis-flask-python
```

## Flask

```commandline
$ flask run
$ flask db init
$ flask db migrate
$ flask db upgrade
```