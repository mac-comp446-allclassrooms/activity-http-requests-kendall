import json
import urllib.request
import ssl

# this line tackles a urllib ssl certificate error noted here:
# https://stackoverflow.com/questions/68275857/urllib-error-urlerror-urlopen-error-ssl-certificate-verify-failed-certifica
ssl._create_default_https_context = ssl._create_stdlib_context

contents = urllib.request.urlopen(urllib.request.Request(
    "https://api.github.com/orgs/vuejs/members",
    headers={"Accept": 'application/vnd.github.full+json"text/html'}
)).read()

#python has package called json which you can use to work with json data, json is used for storing and exchanging data
#parse it and convert it for analysis
#use json.loads method helps parse it and can turn into a dictionary
#you can do the opposite and Convert Python objects into JSON strings
json_data = json.loads(contents.decode('utf-8'))

# print logins wrapped in html <ul> tag
print('<ul> Logins')

# loop through data and grab length and tease apart id and login into separate variables
for i in range(len(json_data)):
    log = json_data[i]['login']
    myID = json_data[i]['id']
    # print(log, myID)
    print('<li> ' + log + '</li>')
    print("*********************")
    print('<ol><li> ' + str(myID) + '</li></ol>')


# end the logins print in closing <ul> tag
print('</ul> ')
print("========================")
print(json_data)