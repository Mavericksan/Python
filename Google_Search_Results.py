#Google Ranking 


import random
import arrow
from robobrowser import RoboBrowser

WebSite = 'www.aps-munich.com'

# Read all predefined tags
#tags_list = ['aps Solutions GmbH', 'aps-munich', 'Everbeing','Mechanical Devices', 'WinWay Technology', 'Test Sockets']
#print(tags_list[0])

tags_list = []

with open('aps_tags.txt', 'r') as tags_file:
    tags_list_str = tags_file.readline()
    tags_file.close()
        
#print(tags_list_str)
# String in Liste umwandeln
tags_list = list(tags_list_str.split(';'))

#for tag in tags_list:
#    print(tag)

    

now = arrow.now().format('DD.MM.YYYY HH:mm:ss')
#print('\n', now, '\n')

#user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; SM-T800) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Safari/537.36']
#for agents in user_agents:
#    print(agents)

user_agents = []
with open('user_agents.txt', 'r') as agents_file:
    user_agents_str = agents_file.readline()
    agents_file.close()
#print(user_agents_str)
#print()

#Convert String in List
user_agents = list(user_agents_str.split('\t'))
for agents in user_agents:
    print(agents)


for tag in tags_list:
    browser = RoboBrowser(history=False, user_agent=random.choice(user_agents), parser='html.parser')
    #browser = RoboBrowser(history=False, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36', parser='html.parser')
    #print(tag)
    browser.open('https://www.google.de/search?num=500&q='+str(tag))
    links = browser.find_all('cite', {'class': 'iUh30'})
    #print(links)
    with open('links_aps.log', 'a') as links_file:
        links_file.write(f'{tag}\n {links}\n\n')
        links_file.close()
    Ranking = 999
    for i, link in enumerate(links):
        if WebSite in str(link):
            Ranking = i+1
            print(tag+'\t\t' + str(Ranking))
            break
    print(f'Ranking: {tag}, {Ranking:03d}')
    with open('ranking_aps.log','a') as results_file:
        results_file.write(f'{now};{tag};{Ranking:03d}\n')
        results_file.close()
        
