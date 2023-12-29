# Lesson check notificator

A django project that shows special places on the map.
Here is [example](http://notagirl.pythonanywhere.com/):

## Environment


### Requirements

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```bash
pip install -r requirements.txt
```

### Environment variables

- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS

1. Put `.env` file near `main.py`.
2. `.env` contains text data without quotes, except `ALLOWED_HOSTS`.

For example, if you print `.env` content, you will see:

```bash
$ cat .env
SECRET_KEY=django-insecure-6ya...
DEBUG=False
ALLOWED_HOSTS='127.0.0.1,'
```

#### How to get

- Download the code
- Create database with `python manage.py migrate`

### load_place

To add a new place on the map run:
```bash
python manage.py load_place <your_link.json>
```
*json must look like this:
```
{
    "title": "",
    "imgs": [
       
    ],
    "description_short": "",
    "description_long": "",
    "coordinates": {
        "lng": "",
        "lat": ""
    }
}
```

### Run

Launch on Linux(Python 3) or Windows:
```bash
python manage.py runserver
```

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).