import requests
import json

response = requests.get('https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=2a78e0379eef39a33645c52de90a')

dataDict = json.loads(response.text)
# dataDict is now a python dictionary



visitorIdList = []
for i in range(len(dataDict['events'])):
    if dataDict['events'][i]['visitorId'] not in visitorIdList:
        visitorIdList.append(dataDict['events'][i]['visitorId'])
    else:
        pass
#list of all visitor Ids with no repeats





visitorIdDict = {}
for i in range(len(visitorIdList)):
    visitorIdDict[visitorIdList[i]] = []

# what I meant to do is create dictionary with format {visitor id (string), [{url: xxx, timestamp: xxx}]} in order to categorize each visit by
# visitor id
# but I ran into a bug -- it would only append to the list that corresponds to the first key in the dictionary
# when debugging, I saw that the timeAndUrl & the visitorIdKey were iterating over the data fine, so I wasn't sure why I couldn't access the rest of the keys
# in the dictionary using this same variable


for j in range(len(dataDict['events'])):
    timeAndUrl = {'url': dataDict['events'][j]['url'], 'timestamp': dataDict['events'][j]['timestamp']}
    visitorIdKey = dataDict['events'][j]['visitorId']
    visitorIdDict[visitorIdKey].append(timeAndUrl)

print(visitorIdDict)
poster = requests.post('https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=2a78e0379eef39a33645c52de90a', data = json.dumps(visitorIdDict))
print(poster)




#notes:
# group the events (page visits) by visitor
# group the visitor events (page visits) in chron order
# if  < 10 mins (600000 ms) between two visits, its good data and is in the session
# want session to include 'duration', 'pages', 'startTime'
# if only one visit in a session, start time is 0
# make sure urls for each session in cron order



