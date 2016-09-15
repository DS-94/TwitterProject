
# Comment out the print statuses and uncommment the bottom of the page to let tweets into sql

# Still need to sort automation



from twython import TwythonStreamer, Twython
import pyodbc
import json

cnxn = pyodbc.connect('DSN=kubrick')
type = 'united'

tweets = []


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if data['lang'] == 'en':
            tweets.append(data)
            print 'received tweet #', len(tweets)

        if len(tweets) >= 1:
            self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()


trackvar = "Manchester " + type


stream = MyStreamer('consumer key', 'consumer secret', 'access token', 'access token secret')
stream.statuses.filter(track = trackvar)



for statuses in tweets:

    print statuses

    #insertcmd = 'insert into dbo.Tweets (Tweets) values(?)'
#
    #cursor.execute(insertcmd, json.dumps(statuses))
    #cnxn.commit()
#