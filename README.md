# Test task for adjust

### Installation:
1. `virtualenv ./backend/venv`
2. `sh run.sh` (it completes build and run stages)

### Preparation:
You should prepopulate your dataset in db.
To complete this just go to [http://127.0.0.1:8000/api/debug/load_dataset/](http://127.0.0.1:8000/api/debug/load_dataset/).

When it's returned **200 OK** you can go to queries =)

### Extras:
You can watch docs.
Use this link - [http://127.0.0.1:8000/api/redocs/](http://127.0.0.1:8000/api/redocs/)

### Common use-cases:

|Number|Task|link|
|:---:|:---:|:---:|
|1|Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.|[http://127.0.0.1:8000/api/dataset/?select=channel&select=country&select=impressions&select=clicks&date_to=2017-06-01&group_by=channel&group_by=country&sort=clicks&order=1](http://127.0.0.1:8000/api/dataset/?select=channel&select=country&select=impressions&select=clicks&date_to=2017-06-01&group_by=channel&group_by=country&sort=clicks&order=1)|
|2|Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.|[http://127.0.0.1:8000/api/dataset/?select=installs&select=date&select=os&date_from=2017-05-01&date_to=2017-05-30&group_by=date&sort=date&os=ios](http://127.0.0.1:8000/api/dataset/?select=installs&select=date&select=os&date_from=2017-05-01&date_to=2017-05-30&group_by=date&sort=date&os=ios)|
|3|Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.|[http://127.0.0.1:8000/api/dataset/?select=revenue&select=os&date_from=2017-06-01&date_to=2017-06-30&group_by=os&sort=revenue&order=1](http://127.0.0.1:8000/api/dataset/?select=revenue&select=os&date_from=2017-06-01&date_to=2017-06-30&group_by=os&sort=revenue&order=1)|
|4|Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.|[http://127.0.0.1:8000/api/dataset/?select=spend&select=country&count_cpi=true&group_by=channel&country=CA&sort=cpi&order=1](http://127.0.0.1:8000/api/dataset/?select=spend&select=country&count_cpi=true&group_by=channel&country=CA&sort=cpi&order=1)|

### Description:
There are some core framework I used to code this task:
- FastAPI (request framework, love this one)
- SQLAlchemy (orm)
- Pydantic (for data validation)
- databases (to make sqlalchemy **asynchronous**)