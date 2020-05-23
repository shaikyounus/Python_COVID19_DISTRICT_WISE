import json
from jsonpath_rw import parse
from urllib.request import urlopen
with urlopen("https://api.covid19india.org/districts_daily.json") as response:
    source=response.read()
# print(source)

data=json.loads(source)
# print(json.dumps(data, indent=2))
# print(len(data['raw_data']))
filename="districtdata.csv"
f=open(filename,"w")
headers="District ID, State ID,Date,confirmed,deceased,recovered,totalconfirmed,totaldeceased,totalrecovered \n"
f.write(headers)
confirmedsum=0
recoveredsum=0
deceasedsum=0
for item in data['districtsDaily']['Andaman and Nicobar Islands']:
        active=data['districtsDaily']['Andaman and Nicobar Islands']['North and Middle Andaman'][0]['active']
        active=data['districtsDaily']['Andaman and Nicobar Islands']['North and Middle Andaman'][1]['active']
        
        


print(active)
        
        
        
       


                
                
        
        











###

    ##for i in data['districtsDaily']:
   ## confirmedsum=confirmedsum+i['confirmed']
##for i in data['districtsDaily']:
   ## deceasedsum=deceasedsum+i['deceased']
##for i in data['districtsDaily']:
   ## recoveredsum=recoveredsum+i['recovered']

    ##f.write(districtcode +","+ statecode +","+date +","+confirmed+" ," +deceased+","+ recovered +","+confirmedsum +","+deceasedsum+","+recoveredsum+"\n")
    # print(patientnumber, statecode, statepatientnumber, nationality,
    # detectedcity, dateannounced, age, gender, currentstatus)
##f.close()
###
