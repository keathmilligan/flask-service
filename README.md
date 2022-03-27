RESTful Flask Service Quick Start
=================================

This template provides a basis for a [Flask](http://flask.pocoo.org/)-based service that exposes RESTful API endpoints.

Features:
* Flask 2.x and blueprints
* JSON Web Token (JWT) authentication
* PyTest unit-tests
* Serve in production with waitress
* Pylint and Black
* Sample Docker container

This is a "pure RESTful" service, it exposes only RESTful APIs and does not generate any HTML. It could be paired with a single-page-application (SPA) web front-end, mobile app or some other type of client and may act as a microservice component in a much larger application. If you are looking for a stand-alone web application template or a Flask example that serves HTML, consider the [Flask Application Quick-Start Template](https://github.com/keathmilligan/flask-quickstart) instead.

## Getting Started

You will need Python 3.8 or later. Use the appropriate installation method for your system to install Python and make sure it is in your path. The template currently targets Python 3.10 (recommended).

This project also uses [pipenv](https://pipenv.pypa.io/en/latest/) to manage dependencies and its virtual environment. You will need to install it if you do not already have it.

### Using the template

To use the template, click the **Use this template** button in the [Github repository](https://github.com/keathmilligan/flask-quickstart) to create a new project using this code as a basis. Alternatively, you can clone the repository locally.

### Install dependencies

> The template currently expects Python 3.10, if you need to use an older version, you will need to modify the `Pipfile`.

Use [pipenv](https://pipenv.pypa.io/en/latest/) to create a virtual environment and install the dependencies:

```
pipenv install --dev
```

The `--dev` option will also install the optional development dependencies such as `pylint` and `pytest`.

## Running

### Running in Development

To start the development server with automatic reloading, run:

Linux/MacOS:
```bash
export FLASK_APP=sample; pipenv run flask run --debugger --reload --with-threads
```

Windows Powershell
```powershell
$env:FLASK_APP = "sample"; pipenv run flask run --debugger --reload --with-threads
```

### Running in Production

To serve the app with `waitress` for production use, run:

```
pipenv run python -m sample
```

Hit `Ctrl-C` to abort.

This is just a starting point for production deployment - see the [waitress docs](https://docs.pylonsproject.org/projects/waitress/en/latest/usage.html) for more info.

## Test

Run the `pytest` unit tests with:

```
pipenv run pytest
```

## Authentication

In this template example, the service does not handle authentication/authorization itself. It assumes that some external service takes care of authenticating and authorizing all API requests through an API gateway or proxy. The authentication service issues a JWT that is passed to the service so the service only needs to validate the JWT on each request allowing it remain stateless with regard to authentication. The JWT key is validated using an asymetric algorithm (e.g. RSA256) and the only public key needs to be provisioned with the service - the service does not need the private key.

For testing purposes the `issue_jwt.py` utility is included so you can locally generate JWTs in order to make test requests.

Before you can use the utility, you will need to generate an RSA256 key pair with something like:

```
ssh-keygen -t rsa -b 4096 -m PEM -f app.key
```

The utility expects to find the private key in a file named `app.key` in the current directory and the app expects the public to be a file named `app.key.pub` in the root directory of the project.

The algorithm is selected in the `sample/__init__.py` file. You may elect to use a different algorithm or change the way the public key is handled. See [this list](https://pyjwt.readthedocs.io/en/latest/algorithms.html) of supported algorithms.

### Generate an access token for testing

Generate an access token with:

```
pipenv run python issue_jwt.py
```

Copy the access token and then use a tool like [PostMan](https://www.postman.com/) or the VSCode [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client) extension to make test requests. Set the "Authorization" type to "Bearer Token" and paste the access token into the Token field or alternatively, set the `Authorization` header to "Bearer `<access token>`".

![Test Request](/docs/images/request.png)

## Deploy in Docker

A sample `Dockerfile` is included. Build it with:

```
docker build . -t sample:latest
```

> Note that only the *public* key is deployed with the container.

Then to test it locally, run:

```
docker run -it --rm -p 127.0.0.1:8081:8080 sample:latest
```

You should now be able to reach the service at `http://localhost:8081`. Stop the service with `Ctrl-C`.
