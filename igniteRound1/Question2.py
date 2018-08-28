import json
from pprint import pprint

data = []

# parsing the JSON file given, I would like to add that the format of searches.json is a bit different and as such it took me a bit of 
# time to understand that.  

with open('searches.json') as f:
        for line in f:    
            data.append(json.loads(line))

searchCount_A = 0
searchCount_B = 0

loginCount_A = 0
loginCount_B = 0

for i in data:
    num = i['uid']
   # print(i['search_count'])
    if(num%2 == 0):
        searchCount_A = searchCount_A + i['search_count']
        loginCount_A = loginCount_A + i['login_count']
    else:
        searchCount_B = searchCount_B + i['search_count']
        loginCount_B = loginCount_B + i['login_count']



if( searchCount_B > searchCount_A ):
    print("A larger number of users used the search feature in the new design (B)")
else:
    print("A larger number of users used the search feature in the new design (A)")

# "more often" would mean greater frequency of search, i.e. number of search per login. However this can easily be done "per-user" as well.

searchFrequency_A = searchCount_A/loginCount_A
searchFrequency_B = searchCount_B/loginCount_B

if(searchFrequency_B>searchFrequency_A):
    print("Users searched more often in the new design(B).")
else:
    print("Users searched more often in older design(A).")

