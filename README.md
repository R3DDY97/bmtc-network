# bmtc-network
- Explores the Bangalore bus transport Network and provides features 
to find out the bus routes  available between  bus stops
Info about any bus route , bus stop, KIA - Vayu vega services......

- Can visualise the entire BMTC-network in dynamic map 

- To directly use without local setup  [click to open web-app](https://bmtc-network.herokuapp.com/)



![BMTC-Netowork Map](https://raw.githubusercontent.com/R3DDY97/bmtc-network/master/pics/Screenshot-2018-5-23_bmtc_qgs.png)


## Requirements

- flask, WTForms, gunicorn modules in Python v3.x


The map was generated using **qgis** software utilising OpenStreetMaps and Leaflet plugins
and no dependencies to run or use it . All required data to support it to work offline is stored in static folder

## Usage


```bash
$ git clone https://github.com/R3DDY97/bmtc-network
$ cd bmtc-network
$ pip3 install -r requirements.txt
$ cd bmtc
$ gunicorn app:app 

```
![BMTC-Search Result](https://raw.githubusercontent.com/R3DDY97/bmtc-network/master/pics/Screenshot-2018-5-23_SvAeYnMkAy.png)


Open browser url `http://127.0.0.1:8000` or `localhost:8000` to use the  application 


The data may not be accurate but, has been validated. Please use it without warranty of any kind.

### TO Do
* Make map for every search result

*~~Add AIRPORT Vayu Vajra support~~

*~~Deploy~~



