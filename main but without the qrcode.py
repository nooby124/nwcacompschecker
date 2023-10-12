import requests
import time
import pycountry_convert
import os
import platform
osname = platform.system()
inputcountry = input("input country by the 2 letter code (for example: BE for belguim, US for the united states): ")
thing = 'https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/competitions/' + inputcountry + '.json'
r = requests.get(thing)
countryconverted = pycountry_convert.country_alpha2_to_country_name(cn_name_format="default", country_2_code=inputcountry)
if "size" in str(r.text) and ":1000" in str(r.text):
    print("no comps found")
else:
    if " " in countryconverted:
        print("found comps but your country has a space in its name so no link!")
        time.sleep(5)
        exit()
    print("found comps! check https://www.worldcubeassociation.org/competitions?region=" + countryconverted + "&search=&state=present&year=all+years&from_date=&to_date=&delegate=&display=list")
time.sleep(3)
