# Next-gen EHS 🐍
![Vue Logo](/src/assets/logo-vue.png "Vue Logo")
![Django Logo](/src/assets/logo-django.png "Django Logo")

This is the course project for CSCI-410. We built a platform that allows easy and secure storage and retrieval of **medical records** for both the patients🤕 and the doctors👨🏻‍⚕️.

With personal information and medical records digitized, we can provide a smooth workflow among departments and people that the needed information will be delivered to the right person and new information will be collected automatically to form a new record entry.

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


| Location             |  Content                                   |
|----------------------|--------------------------------------------|
| `/backend`           | Django Project & Backend Config            |
| `/backend/api`       | Django App (`/api`)                        |
| `/src`               | Vue App .                                  |
| `/src/main.js`       | JS Application Entry Point                 |
| `/public/index.html` | Html Application Entry Point (`/`)         |
| `/public/static`     | Static Assets                              |
| `/dist/`             | Bundled Assets Output (generated at `yarn build`) |

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

## Deploy

* Set `ALLOWED_HOSTS` on [`backend.settings.prod`](/backend/settings/prod.py)

### Heroku Server

```
$ heroku apps:create django-vue-template-demo
$ heroku git:remote --app django-vue-template-demo
$ heroku buildpacks:add --index 1 heroku/nodejs
$ heroku buildpacks:add --index 2 heroku/python
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set DJANGO_SETTINGS_MODULE=backend.settings.prod
$ heroku config:set DJANGO_SECRET_KEY='...(your django SECRET_KEY value)...'

$ git push heroku
```

Heroku's nodejs buildpack will handle install for all the dependencies from the [`package.json`](/package.json) file.
It will then trigger the `postinstall` command which calls `yarn build`.
This will create the bundled `dist` folder which will be served by whitenoise.

The python buildpack will detect the [`Pipfile`](/Pipfile) and install all the python dependencies.

The [`Procfile`](/Procfile) will run Django migrations and then launch Django'S app using gunicorn, as recommended by heroku.

##### Heroku One Click Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/gtalarico/django-vue-template)

## Static Assets

See `settings.dev` and [`vue.config.js`](/vue.config.js) for notes on static assets strategy.

This template implements the approach suggested by Whitenoise Django.
For more details see [WhiteNoise Documentation](http://whitenoise.evans.io/en/stable/django.html)

It uses Django Whitenoise to serve all static files and Vue bundled files at `/static/`.
While it might seem inefficient, the issue is immediately solved by adding a CDN
with Cloudfront or similar.
Use [`vue.config.js`](/vue.config.js) > `baseUrl` option to set point all your assets to the CDN,
and then set your CDN's origin back to your domains `/static` url.

Whitenoise will serve static files to your CDN once, but then those assets are cached
and served directly by the CDN.

This allows for an extremely simple setup without the need for a separate static server.

[Cloudfront Setup Wiki](https://github.com/gtalarico/django-vue-template/wiki/Setup-CDN-on-Cloud-Front)
