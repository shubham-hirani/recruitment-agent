# Bot Service

## How to clone service
```
    $ git clone git@github.com:shubham-hirani/recruitment-agent.git
    $ cd recruitment-agent
```

## How to add virtual environment
```
    $ virtualenv -p /usr/bin/python3.11 venv
    $ source venv/bin/activate
```

## How to install requirements
```
    $ pip install -r requirements.txt
```

## Make sure to add below env variables
```
    OPENAI_API_KEY
    SERPAPI_KEY
```
- Add run configurations in PyCharm with .env environment file

## Setup running guidelines
```
    $ python main.py
```

## If you have your JD file name different you need to change the filename to your filename in the line number 13 in main.py

## Also if you want your output file in different name than output.cv please change the line number 67 in main.py


##