# Car Finder / Viewer

Search vehicle by ID and pull available information and an image of it

## Introduction

Backend uses python pandas for the dataframe/database and hug.rest for a lightweight REST API server
Frontend uses vue as the framework with axios for the easy REST API calls and bulma css for the layout

Frontend is completely decoupled with the backend development, only the necessary endpoints are
needed by the server.

### Prerequisites

First, install the pip requirements/virtualenvironment found in the project root folder. 

```
$ pip install -r requirements.txt
```

### Sample runs

First run the API, assumes to be run on a local server as http://localhost:8000

```
$ hug -f src/backend.api.py
```

Then open the frontend page, works even if opened as it is or hosted in a www/htdocs folder

```
file:///home/goliath/projects/vehiclefinder/src/frontend/index.html
```

## Deployment

To use a WSGI-compatible server, we can use uWSGI

```
$ uwsgi --http 0.0.0.0:8000 --wsgi-file src/backend/api.py --callable __hug_wsgi__
```

## Built With

* [Python pandas](https://pandas.pydata.org/)
* [VueJS](https://vuejs.org/)
* [Axios](https://github.com/axios/axios)
* [hug REST](http://www.hug.rest/)
* [Bulma CSS](https://bulma.io/)

## Authors

* **Ariel D. Cercado** - *Initial work*

## License

For use with Chrysalis Solmotive (tech exam)