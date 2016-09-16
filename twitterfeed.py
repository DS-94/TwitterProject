


###  Change track in status filter to trackvar2 for George, trackvar3 for Nihir




import json
from pandas import DataFrame, Series
import pandas
import numpy
import urllib
import urllib2

resp = open('mannyweathoutput.txt', 'r')
data = json.loads(resp.read())
ManGeo = {'lat': u'53.479', 'lon': u'-2.2465', 'name': u'MANCHESTER'}
Man5Data = []
ManInd = []

datar = data['SiteRep']['DV']['Location']['Period']
for i in datar[:]:

   ManInd.append(i['value'][:-1])


datar = data['SiteRep']['DV']['Location']['Period']
for i in datar[:]:
    x = i['Rep'][0]
    Man5Data.append({'Feels Like Max (C)':x['FDm'], 'Daily Max (C)':x['Dm'], 'Noon RH (%)':x['Hn'], 'Wind Speed (mph)':x['S'], 'Weather Type':x['W'], 'Precip Prob_day (%)':x['PPd'] })


ManFrame = DataFrame(Man5Data)

ManFrame.index=ManInd


weatherdict = {'NA': ['Not available', 'sunny', 'raining', 'windy'], 0: ['Clear night', 'cold', 'windy', 'stars']\
, 1: ['Sunny day', 'sunny', 'hot', 'boiling'], 2: ['Partly cloudy (night)', 'cloudy', 'gloomy', 'overcast' ], 3: ['Partly cloudy (day)', 'cloudy', 'gloomy', 'overcast'],\
 4: 'Not used', 5:['Mist', 'mist', 'misty', 'foggy'], 6: ['Fog', 'fog', 'foggy', 'misty'], 7:['Cloudy', 'cloudy', 'overcast', 'raining'],\
8:['Overcast', 'overcast', 'cloudy', 'raining'], 9:['Light rain shower (night)', 'rain', 'raining', 'drizzle'], 10:['Light rain shower (day)', 'rain', 'raining', 'drizzle']\
 ,11: ['Drizzle', 'drizzle', 'rain', 'rain'], 12:['Light rain', 'rain', 'raining', 'drizzle'], 13:['Heavy rain shower (night)', 'rain', 'raining', 'pouring']\
,14:['Heavy rain shower (day)', 'raining', 'pouring', 'rain'], 15:['Heavy rain', 'rain', 'raining', 'pouring'], 16:['Sleet shower (night)', 'sleet', 'raining', 'snow'] \
, 17: ['Sleet shower (day)', 'sleet', 'raining', 'snow'], 18:['Sleet', 'sleet', 'raining', 'snow']\
, 19:['Hail shower (night)', 'hail', 'stormy', 'raining'], 20:['Hail shower (day)', 'hail', 'raining', 'stormy']\
, 21: ['Hail', 'hail', 'raining', 'stormy'], 22:['Light snow shower (night)', 'snow', 'sleet', 'raining']\
, 23:['Light snow shower (day)', 'snow', 'sleet', 'raining'], 24: ['Light snow', 'snow', 'snowing', 'raining']\
, 25:['Heavy snow shower (night)', 'snow', 'snowing', ''], 26:['Heavy snow shower (day)', 'snow', 'snowing', ''],\
27:['Heavy snow', 'snow', 'snowing', ''], 28:['Thunder shower (night)', 'thunder', 'lightning', 'raining'],\
29:['Thunder shower (day)', 'thunder', 'lightning', 'raining'], 30:['Thunder', 'thunder', 'lightning', 'raining']}



from twython import TwythonStreamer, Twython
import pyodbc
import json

cnxn = pyodbc.connect('DSN=kubrick')
type = ManFrame.loc['2016-09-16', 'Weather Type']

tweets = []


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if data['lang'] == 'en':
            tweets.append(data)
            print 'received tweet #', len(tweets)

        if len(tweets) >= 2400:
            self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()



import datetime


today = str(datetime.date.today())


Type = ManFrame['Weather Type'][today]

wtype = Type.encode('utf-8')

wt = int(wtype)

wtoday = weatherdict[wt][1:]
print wtoday


trackvar1 = "Manchester " + str(wtoday[0:1])
trackvar2 = "Manchester " + str(wtoday[1:2])
trackvar3 = "Manchester " + str(wtoday[2:3])

print trackvar1
print trackvar2
print trackvar3

stream = MyStreamer(consumer key, consumer secret, access toke, access token secret)
stream.statuses.filter(track = trackvar1)

with open('C:\\Users\\student03\\Desktop\\TiwtterProject\\TwitterProject\\savedtweets.json', 'a') as outfile:
    json.dump(tweets, outfile)



