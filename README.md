
# Fatal Accident Reporting System (FARS)
FARS is an official count of fatal motor vehicle crashes that occurred within the 50 States, the District of Columbia, and Puerto Rico since 1975. To qualify as a FARS case, the crash had to involve a motor vehicle traveling on a trafficway customarily open to the public, and must have resulted in the death of a motorist or a non-motorist within 30 days of the crash. 

This code will download FARS data into a local postgres database for simple querying. 

### Dependencies 
You will need to have Python 2.7.8 and Postgres installed. The python dependecies can be found in `requirements.txt`. sas7bdat,numpy,pandas,sqlalchemy
### Data
FARS data is esoteric and follows its own logic that is only decipherable by combing through upwards of 1400 pages of documentation.  This documentation is found on an open NHTSA FTP server at ftp.nhtsa.dot.gov.  The general structure is that each accident/vehicle/person has nearly 50 variables associated with it.  These values of these variables are coded numerically, where each number corresponds to a precise definition. For instance if the vehicle “MODEL” variable is set to 850, this typically means the vehicle is a motorhome. 

Before diving into the data it is important to get a sense of what you will be looking at.  This is the documentation that I found helpful:
1. ftp://ftp.nhtsa.dot.gov/fars/FARS-DOC/Analytical%20User%20Guide/FARS%20Analytical%20Users%20Manual%201975-2016-822447.pdf
2. ftp://ftp.nhtsa.dot.gov/fars/FARS-DOC/Coding%20and%20Validation%20Manual/2016%20FARS%20CRSS%20Coding%20and%20Validation%20Manual-812449.pdf



### Installation
1. Clone this repository 
1. `cd fars`
1. `createdb fars`
1. `pip install -r requirements.txt`
1. FARS published its data to an open FTP server located here: ftp://ftp.nhtsa.dot.gov/FARS. Find the folders for the years you are looking to import and download the SAS zip file.  eg: ftp://ftp.nhtsa.dot.gov/FARS/2000/SAS/
1. rename your downloaded folder `fars` and move it to the corresponding `data/year` folder in this repository. 

### Usage
1. `python import.py "POSTGRES_CONNECTION_URL" YEARS` 
1. `psql fars`
#### Example
1. `python import.py "postgresql://USERNAME@localhost:5432/fars" 2015 2014`
### Extension
If you want tables in your postgres database to decipher location and body type codes run `psql fars < db/extension.sql`.  This will allow you to look up cities states, counties, or vehicle body types based on the FARS data.
### Useful Queries
1. `select * from accident join vehicle ON accident."YEAR" = vehicle."ACC_YEAR" and vehicle."ST_CASE" = accident."ST_CASE"` Notes: You can join the accident and the vehicle table using the ST_CASE and the ACC_YEAR columns. 
1. `select "City Code" from location where "City Name" = 'NEW YORK'`