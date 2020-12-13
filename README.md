# Next-gen EHS 🐍
![Vue Logo](/src/assets/logo-vue.png "Vue Logo")
![Django Logo](/src/assets/logo-django.png "Django Logo")

This is the course project for CSCI-410. We built a platform that allows easy and secure storage and retrieval of **medical records** for both the patients🤕 and the doctors👨🏻‍⚕️.

![Booking Appointment](/public/static/appointment.png "Booking Appointment")

![working schedule](/public/static/schedule.png "View my working schedule")

With personal information and medical records digitized, we can provide a smooth workflow among departments and people that the needed information will be delivered to the right person and new information will be collected automatically to form a new record entry.

![working schedule](/public/static/record.png "View my patient's medical record")

![Diagnosis](/public/static/diagnosis.png "Diagnose my patient")


At the bottom level, all the account information and record data are encrypted. We will also implement an access control mechanism to ensure certain information is only visible to specific user groups.

### Major Dependency
Backend side
* Django
* Django REST framework
* Django Whitenoise, CDN Ready

Frontend side
* Vue CLI 3
* Vue Router
* Gunicorn
* Configuration for Heroku Deployment


### Project Stricture

- 📂 __django\-vue\-template__
   - 📄 [README.md](README.md)
   - 📄 [app.json](app.json)
   - 📂 __backend__
     - 📂 __api__
       - 📄 [\_\_init\_\_.py](backend/api/__init__.py)
       - 📄 [admin.py](backend/api/admin.py)
       - 📄 [apps.py](backend/api/apps.py)
       - 📄 [models.py](backend/api/models.py)
       - 📄 [serializers.py](backend/api/serializers.py)
       - 📄 [tests.py](backend/api/tests.py)
       - 📄 [views.py](backend/api/views.py)
     - 📂 __settings__
       - 📄 [\_\_init\_\_.py](backend/settings/__init__.py)
       - 📄 [dev.py](backend/settings/dev.py)
       - 📄 [prod.py](backend/settings/prod.py)
     - 📄 [urls.py](backend/urls.py)
     - 📄 [wsgi.py](backend/wsgi.py)
   - 📄 [database\_models.png](database_models.png)
   - 📄 [db.sqlite3](db.sqlite3)
   - 📄 [manage.py](manage.py)
   - 📄 [package.json](package.json)
   - 📄 [requirements.txt](requirements.txt)
   - 📂 __src__
     - 📄 [App.vue](src/App.vue)
     - 📂 __assets__
     - 📂 __components__
       - 📄 [AccountInput.vue](src/components/AccountInput.vue)
       - 📄 [DashInfo.vue](src/components/DashInfo.vue)
       - 📄 [Dashboard.vue](src/components/Dashboard.vue)
       - 📄 [InfoBoard.vue](src/components/InfoBoard.vue)
       - 📄 [Interview.vue](src/components/Interview.vue)
       - 📄 [ListAppointment.vue](src/components/ListAppointment.vue)
       - 📄 [LoginForm.vue](src/components/LoginForm.vue)
       - 📄 [MakeAppointment.vue](src/components/MakeAppointment.vue)
       - 📄 [Med.vue](src/components/Med.vue)
       - 📄 [Page404.vue](src/components/Page404.vue)
       - 📄 [Person.vue](src/components/Person.vue)
       - 📄 [RecordCreate.vue](src/components/RecordCreate.vue)
       - 📄 [RecordEdit.vue](src/components/RecordEdit.vue)
       - 📄 [RecordFilter.vue](src/components/RecordFilter.vue)
       - 📄 [RecordUpload.vue](src/components/RecordUpload.vue)
       - 📄 [RecordView.vue](src/components/RecordView.vue)
       - 📄 [RegForm.vue](src/components/RegForm.vue)
       - 📄 [Schedule.vue](src/components/Schedule.vue)
     - 📄 [main.js](src/main.js)
     - 📄 [router.js](src/router.js)
   - 📄 [vue.config.js](vue.config.js)



## Prerequisites

Before getting started you should have the following installed and running:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install)
- [X] Vue CLI 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3 - [instructions](https://wiki.python.org/moin/BeginnersGuide)
- [X] Anaconda - [instructions](https://www.anaconda.com/products/individual)

## Setup Codebase

**Step 1** : Clone the repo to local machine

```
$ git clone https://github.com/Boyan-Org/full-stack-integration
$ cd full-stack-integration
```

**Step 2** : Install JavaScript dependencies
```
$ yarn install
```
**Step 3** : Initialize python virtual environment ([why?](https://stackoverflow.com/questions/41972261/what-is-a-virtualenv-and-why-should-i-use-one))
```
$ conda create -n venv
$ conda activate venv
```
**Step 4** : Install Python dependencies
```
$ pip install -r requirement.txt
```
**Step 5** : Initialize sqlite database
```
$ python manage.py migrate
```
- To inspect sqlite database from GUI, install [Sqlite Browser](https://sqlitebrowser.org/dl/)

## Running Development Servers

**Step 1** : Run Django server
```
$ python manage.py runserver
```
- The Django API and static files will be served from [`localhost:8000`](http://localhost:8000/).

**Step 2** : Run Vue.js server (in another tab)
```
$ yarn serve
```
- The Vue application will be served from [`localhost:8080`](http://localhost:8080/)

Note:
- The dual dev server setup allows you to take advantage of
webpack's development server with hot module replacement.

- Proxy config in [`vue.config.js`](/vue.config.js) is used to route the requests back to Django's API on port `8000`.

- If you would rather run a single dev server, you can run Django's
development server only on `:8000`, and you have to build the Vue app first and the page will not reload on changes.

```
$ yarn build
$ python manage.py runserver
```
