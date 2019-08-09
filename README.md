# what is ?
Sample app for using [pytest](https://github.com/pytest-dev/pytest).

# Requirement
* python: 3.7.4
* pip: 19.2.1
* pipenv: version 2018.11.26

# Setup
* Build

```
$ pipenv install --dev
```

* Set Environmental variables

| Environmental variable name | Default        | Description                                                                                                       |
|-----------------------------|----------------|-------------------------------------------------------------------------------------------------------------------|
| SECRET_KEY                  | None(Required) | Please read [a official docs](https://flask.palletsprojects.com/en/1.0.x/quickstart/#sessions)|

# Start server

```
$ pipenv run start
```

# Lint / Formatter
flake8(Lint) and autopep8(Formatter) were installed in this application.

```
# Run Lint
$ pipenv run lint

# Run Formatter
$ pipenv run format
```
