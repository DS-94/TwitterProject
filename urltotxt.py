import json
from pandas import DataFrame, Series
import pandas
import numpy
import urllib
import urllib2

url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/310013?res=daily&key=841095cd-32d4-4984-9026-f21e9fdf90b2'
response = urllib2.urlopen(url)
with open('mannyweathoutput.txt', 'w') as f:
    f.write(response.read())