
def readFile():
    apiURL='https://api.donorschoose.org/common/json_feed.html?snacks-for-better-testing/4653507/&APIKey=DONORSCHOOSE&showSynopsis=true&max=50'
    #result = getAverage(apiURL)
    #print(result)
    trans(apiURL)
    
    
import requests, json
def getAverage(url):
    rep=requests.get(url)
    runningTotal = 0
  
    avg = 0
    if(int(rep.status_code)==200):
        apiDict = json.loads(rep.text)
        proposalList = apiDict['proposals']
        for p in proposalList:
            runningTotal +=float(p['totalPrice'])
        avg=runningTotal/ len(proposalList)
        return avg


import csv
def trans(url):
    rep=requests.get(url)
    apiDict=json.loads(rep.text)
    csv_proposals=apiDict['proposals']
    with open ('keywords.txt', 'r') as keywords:
        with open('list.csv', 'w', newline='') as csvfile:
            csv_writer=csv.writer(csvfile)
            csv_writer.writerow(keywords)
    
    for p in csv_proposals:
        csv_values=[]
        for keywords in open('keywords.txt', newline='\n'):
            for key in keywords:
                csv_values+=p[key]
            
        
                with open ('list.csv', 'a+', newline='') as csvfile:
                    csv_writer=csv.writer(csvfile)
                    csv_writer.writerow(csv_values)  
readFile()       



   

    
    
    
    



