
# secretmsg.ml

A system where anyone can send message to their friends anonymously using link sharing

## 🔗 Live Links
[![live](https://img.shields.io/badge/Live-Check%20Live-brightgreen)](https://secretmsg.ml/)

## Deployment

To deploy this project, Download the repository and open the project folder

```bash
  pip -r install requirements.txt
```
```bash
  py manage.py makemigrations
```
```bash
  py manage.py migrate
```
```bash
  py manage.py runserver
```

### to get Admin panel access

You need to create super admin

```bash
  py manage.py createsuperuser
```

Then put all the credentials as par your wish and run the project and visit admin path that is specified in the urls.py file



## Tech Stack

**Client:** HTML, CSS, BOOTSTRAP, JAVASCRIPT

**Server:** Django, SQlite

  
