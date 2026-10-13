# natural-faculty-site

`natural-faculty-site` is an educational project for web programming discipline in NaUKMA which shows how could have looked site for natural faculty in NaUKMA.

## Instalation

Use **git** to install natural-faculty-site.

```bash
git clone https://github.com/VSidd976/myplaces.git
```

### Dependencies

* **Python 3.12 or later**
* **Django**

Create **virtual env** and use **pip** to install dependencies.

```bash
pip install -r requirements-dev.txt
```

## Migrating

Execute following command to apply migrations for your data base.

```bash
python manage.py migrate
```

## Adding data

Execute following command to fill data base with sample data.

```bash
python manage.py loaddata faculty/fixtures/data.json
```

## Executing

Execute following command to run server.

```bash
python manage.py runserver
```

Ctrl/command + left click on the local address to open ui in browser.

## AI usage

For this project I used AI for generating UI and as a consultant for backend development.
