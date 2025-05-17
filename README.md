# Bot Service

## How to clone service
```
    $ git clone git@github.com:wotnotbot/bot-service.git
    $ cd bot-service
```

## How to add virtual environment
```
    $ virtualenv -p /usr/bin/python3.9 venv
    $ source venv/bin/activate
```

## How to install requirements
```
    $ pip install --upgrade pip==20.2.4
    $ pip install -r requirements.txt
```

## How to copy sample.env & to use env file in Pycharm to run project
```
    $ cp sample.env local.env
```
- Add run configurations in PyCharm with .env environment file

## Setup running guidelines
```
    $ python run.py
```

## Third parties to connect from Development environment for the service to run locally

- https://wotnot.atlassian.net/wiki/spaces/EN/pages/516718597/Public+Dev+Environment

## Pre commit hooks

- Install pre-commit hooks

    ```bash
    $ pip install -r requirements_dev.txt
    $ pre-commit install
    ```

## Cronjob/Scheduler

|         **Schedular name**         |                      **Endpoint**                     | **Method** | **execution timing** | **Timeout** | **Active/Suspended** | **Retry on failure** |
|:----------------------------------:|:-----------------------------------------------------:|------------|----------------------|-------------|----------------------|----------------------|
| bot-service-contact-data-scheduler | http://bot-service:5009/api/v1/contact-data-scheduler | GET        | Every 30 minute      | 30s         | Suspended            | Yes                  |
