
#Query Phish.net API via Python 3.

import urllib.request
import urllib.parse
import json
import sys

url='https://api.phish.net/'
js='api.js'

apikey = '<Your API Key>'
format = 'json'
apiver = '2.0'
method = 'pnet.shows.setlists.latest'

#Build parameters to send via GET to api.js
params = urllib.parse.urlencode({
  'api':apiver,
  'method':method,
  'format':format,
  'apikey':apikey
  })

#Attempt to open a connection and get the JSON formated data
try:
  f = urllib.request.urlopen(url + js + "?%s" % params)

#Do this for invalid URL
except IOError:
  print 'Error: Unable to connect. Invalid URL.'
  sys.exit(1)

#Get the response code
rsp = f.getcode()

#If the HTTP response is 200 (OK) then proceed 
if rsp == 200:

  #Read the data	
  data =  f.read()

  #Decode the data as JSON
  decoded = json.loads(data)
  
  #Print the Decoded JSON 
  print 'DECODED: ', decoded

  #Print an individual JSON Record
  print 'GET INDIVIDUAL RECORD: ', decoded[0]['showdate']

else:
  #Do this if the not an HTTP response of 200
  print 'Error: ',  rsp


#close the connection
f.close()

