# iris_flask
Simple CI Pipeline for a Flask App

# Setup
docker build -t iris .
docker run --name iris -d -p 8000:5000 --rm iris:latest
curl -X POST localhost:5000
