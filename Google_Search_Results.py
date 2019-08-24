#Google Ranking 

import random
import arrow
from robobrowser import RoboBrowser

WebSite = 'aps-munich.com'

# Read all predefined tags
tags_list = ['aps Solutions GmbH', 'aps-munich', 'Everbeing','Mechanical Devices', 'WinWay Technology', 'Test Sockets']
#tags_list = []
#with open('aps_tags.txt', 'r') as tags_file:
#    tags_list = tags_file.read()
#print(tags_list)

now = arrow.now().format('DD.MM.YYYY HH:mm:ss')
print(now)

user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; SM-T800) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Safari/537.36']


#user_agents = []
#with open('user_agents.txt', 'r') as agents_file:
#    user_agents = agents_file.read()
print(user_agents) 

for tag in tags_list:
    browser = RoboBrowser(history=False, user_agent=random.choice(user_agents), parser='html.parser')
    #print(tag)
    browser.open('https://www.google.com/search?num=500&q='+ tag)
    links = browser.find_all('cite', {'class': 'iUH30'})
    
    Ranking = 999
    for i, link in enumerate(links):
        if WebSite in str(link):
            Ranking = i
            print(tag+" " + str(Ranking))
            break
    print(f'Ranking: {tag}, {Ranking:03d}')





