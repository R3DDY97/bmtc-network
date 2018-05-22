# bmtc-network
Explores the Bangalore bus transport Network and provides features 
to find out the bus routes  available between two bust stops


![BMTC-Netowork Map](https://raw.githubusercontent.com/R3DDY97/bmtc-network/master/pics/Screenshot-2018-5-23 SvAeYnMkAy.png)


## Requirements

- flask and WTForms modules in Python v3.x

`$ sudo pip3 install -U flask WTForms`


The map was generated using **qgis** software utilising OpenStreetMaps and Leaflet plugins


## Usage


```bash
$ git clone https://github.com/R3DDY97/bmtc-network
$ cd bmtc-network
$ pip3 install -r requirements.txt
$ cd bmtc
$ export FLASK_APP=__init__.py
$ flask run


 * Serving Flask-SocketIO app "__init__.py"
 * Forcing debug mode off
 * Serving Flask app "__init__.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
![BMTC-Search Result](https://raw.githubusercontent.com/R3DDY97/bmtc-network/master/pics/2018-05-16-024953_1366x768_scrot.png)


Open browser url `http://127.0.0.1:5000`


The data may not be accurate but, has been validated. Please use it without warranty of any kind.

### TO Do
* Make map for every search result
* Add AIRPORT Vayu Vajra support
* Deploy



