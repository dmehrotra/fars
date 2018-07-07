
from sas7bdat import SAS7BDAT
import sys
import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame, Index
from sqlalchemy import create_engine

engine = create_engine(sys.argv[1])

years = sys.argv[2:]
vheaders= ['STATE','ST_CASE','VEH_NO','REG_STAT','MAKE','MODEL','MAK_MOD','BODY_TYP','MOD_YEAR','VIN','TRAV_SP','DEATHS',"DR_SF1", "DR_SF2", "DR_SF3", "DR_SF4", "P_CRASH2","ACC_YEAR"]
aheaders=['STATE','ST_CASE','COUNTY','CITY','DAY','MONTH','YEAR','HOUR','MINUTE','NHS','ROUTE','FATALS',"LATITUDE","LONGITUD"]

for year in years:
	print("importing "+year)

	accident_data = SAS7BDAT("data/"+str(year)+'/fars/accident.sas7bdat')
	vehicle_data = SAS7BDAT("data/"+str(year)+'/fars/vehicle.sas7bdat')
	accident = accident_data.to_data_frame()
	vehicle = vehicle_data.to_data_frame()
	vehicle["ACC_YEAR"] = year
	accident[aheaders].to_sql('accident', con=engine,if_exists='append') 
	vehicle[vheaders].to_sql('vehicle', con=engine,if_exists='append')
	