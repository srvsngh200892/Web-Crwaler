from BeautifulSoup import BeautifulSoup
import urllib2
import requests
import json
import time
import csv
url="https://angel.co/jobs"

page=urllib2.urlopen(url)

soup = BeautifulSoup(page.read())

#print soup

x=soup.find('div',{'class':'find g-module gray hidden shadow_no_border startup-container'})#getting the list of stratupid

x=str(x)

x=x.split(" ")

x= x[7].split("=")

list_of_startup=x[1].replace('"['," ").replace(']"'," ").split(",")

detail_of_startup=[]

for i in range(100):
    
    base_url='https://api.angel.co/1/startups/'+list_of_startup[i]
    
    response = requests.get(base_url)
    
    time.sleep(5)
    
    profile = response.json()
   
    market_list=[]
    
    mydict={}
    try:
       mydict['company_url'] =profile['company_url']
    except:
        mydict['company_url']=None

    try:
       mydict['name'] =profile['name']
    except:
        mydict['name']=None

    try:
       x =profile['company_size']
       x=x.replace("-"," to ")
       mydict['company_size']=x
    except:
        mydict['company_size']=None

    try:
        for i in range(len(profile['markets'])):
            
            l=str(profile['markets'][i]['display_name'])
            
            market_list.append(l)
            
        string = ','.join(str(x) for x in  market_list)
        
        mydict['Functional Area '] = string   
    except:
        mydict['Functional Area']=None

    try:
       mydict['location'] =profile['locations'][0]['display_name']
    except:
        mydict['location']=None

    print mydict    

    detail_of_startup.append(mydict)


out_path= "C:/Users/srv.sngh92/Music/123.csv"
out_file = open(out_path, 'wb')

fieldnames = sorted(list(set(k for d in detail_of_startup for k in d)))
writer = csv.DictWriter(out_file, fieldnames=fieldnames, dialect='excel')

writer.writeheader() # Assumes Python >= 2.7
for row in detail_of_startup:
    writer.writerow(row)
out_file.close()







