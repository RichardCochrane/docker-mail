# Docker Mail

Mail service for testing the Docker implementations.

This service has just one API endpoint:
- /api/create: accept the details necessary to send a mail

## Installation (local development)

1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `FLASK_APP=run.py flask run --host=0.0.0.0 --port=5657`

## Installation (docker)

1. Ensure that docker server is installed
2. Build image: `docker image build -t d_mail .`
3. Run container as part of network of Docker Main project: `docker container run -it -p 5657:5657 -e FLASK_APP=run.py --rm --name docker_mail --network d_test d_mail`
