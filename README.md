# Star Wars Explorer

A simple app to explore Star Wars API data

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Ideas for improvements

- handle API and network errors
- refactor transform_and_load to conform to SRP and improve testability
- write unit / integration tests omitted due to time constraints

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy star_wars_explorer

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).


## Getting Up and Running locally

### Local Development Environment

Make sure you have the following installed on your host:

- Python 3.9
- PostgreSQL
- Development header files for PostgreSQL (`libpq-dev` package in Ubuntu)
- Development header files for Python 3.9 (`python3.9-dev` package in Ubuntu)
- Development packages for your operating system (`build-essential` package in Ubuntu)

Clone the repository and cd to the project directory.

Create a virtualenv:

    $ python 3.9 -m venv venv

Activate the virtualenv  you have just created:

    $ source venv/bin/activate

Install development requirements:

    $ pip install -r requirements/local.txt
    $ pre-commit install

Create a new PostgreSQL role and database - refer to the PostgreSQL documentation for more information.
To run tests the role must have the `createdb` privilege.

Set the environment variable for your database:

    $ export DATABASE_URL=postgres://<username>:<password>@127.0.0.1:5432/<dbname>

Apply migrations:

    $ python manage.py migrate

Start the development server:

    $ python manage.py ruunserver 0.0.0.0:8000
