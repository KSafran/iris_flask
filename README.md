[![Build Status](https://travis-ci.org/KSafran/iris_flask.svg?branch=master)](https://travis-ci.org/KSafran/iris_flask)
# iris_flask
Simple CI Pipeline for a Flask App

# Setup
To run locally
```
flask run
curl -X POST -H "Content-Type: application/json" localhost:5000 -d '{"data":[1, 1, 1, 1]}'
```

to build and run the docker image
```
python train_model.py
docker build -t iris .
docker run --name iris -d -p 5000:5000 --rm iris:latest
curl -X POST -H "Content-Type: application/json" localhost:5000 -d '{"data":[1, 1, 1, 1]}'
```
