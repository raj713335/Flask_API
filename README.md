# Flask_API

## Docker 

```commandline
$ docker build -t rest-apis-flask-python .
$ docker run -d -p 5000:5000 rest-apis-flask-python
$ docker run -d -p 5000:5000 -w /app -v "$(pwd):/app" rest-apis-flask-python

$ docker build -t rest-apis-flask-smorest-rq .
$ docker run -w /app rest-apis-flask-smorest-rq sh -c "rq worker -u <insert your Redis url here> emails"
```

## Flask

```commandline
$ flask run
$ flask db init
$ flask db migrate
$ flask db upgrade
```