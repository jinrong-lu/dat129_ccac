import urllib
from bs4 import BeautifulSoup

import re
import sqlite3
import os
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def getPageText(type,i):
    
    url="https://www.yelp.com/search?cflt=%s"%(str(type))+"&find_loc=Pittsburgh%2C%20PA&start="+"%s"%(str(i))
    req = urllib.request.Request(url)           
    with urllib.request.urlopen(req) as response:
   #try:
    #respone = urllib.request.urlopen(req)
        
   # except URLError as e:
        
    #    if hasattr(e, 'reason'):
     #       print('We failed to reach a server.')
      #      print('Reason: ', e.reason)
            
       # elif hasattr(e, 'code'):
        #    print('The server could not fulfill the request.')
         #   print('Error code: ', e.code)
            
        #else:
     return response.read()
    

def getRestaurantsName(type):
    
   
    pageText1 = getPageText(type,0)
    soup1 = BeautifulSoup(pageText1, 'html.parser')
    name_tag1 = soup1.find_all('a', target="")
    pageText2 = getPageText(type,30)
    soup2 = BeautifulSoup(pageText2, 'html.parser')
    name_tag2 = soup2.find_all('a', target="")
    name_tag=name_tag1 + name_tag2
    name=[]
    for tag in name_tag:
        name_str=tag.get('name')
        if name_str:
            name=name+[str(name_str)]
    
    
    return name
    
def getRestaurantsRating(type):
     
    pageText1 = getPageText(type,0)
    soup1 = BeautifulSoup(pageText1, 'html.parser')
    pageText2 = getPageText(type,30)
    soup2 = BeautifulSoup(pageText2, 'html.parser')
    stars=[]
    star_tag1= soup1.find_all('div',{'class':re.compile('i-stars*')})
    star_tag2= soup2.find_all('div',{'class':re.compile('i-stars*')})
    star_tag=star_tag1+star_tag2
    for tag in star_tag:
        stars_str=tag.get('aria-label')
        stars=stars+[stars_str.split()[0]]
    return stars
    
def getRestaurantsprice(type):
    
    pageText1 = getPageText(type,0)
    soup1 = BeautifulSoup(pageText1, 'html.parser')
    pageText2 = getPageText(type,30)
    soup2 = BeautifulSoup(pageText2, 'html.parser')
    price = []
    price_tag1 = soup1.find_all('span', {'class': re.compile('priceRange')})
    price_tag2 = soup2.find_all('span', {'class': re.compile('priceRange')})
    price_tag= price_tag1+ price_tag2
    for tag in price_tag:
        price = price + [tag.string]
    return price
    
    
    
    
def getRestaurantsReview(type):
       
    pageText1 = getPageText(type,0)
    soup1 = BeautifulSoup(pageText1, 'html.parser')
    pageText2 = getPageText(type,30)
    soup2 = BeautifulSoup(pageText2, 'html.parser')
    review=[]
    review_tag1 = soup1.find_all('span', {'class': re.compile('reviewCount*')})
    review_tag2 = soup2.find_all('span', {'class': re.compile('reviewCount*')})
    review_tag = review_tag1 + review_tag2
    for tag in review_tag:
        review = review + [tag.string]
        
        
    return review    


def write_csv(type):
        # if the file doesn't exist, create a new file
        file = 'yelp_%s'%str(type)+'.csv'
        if not os.path.exists(file):
            with open(file, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Price', 'Review_count', 'Star'])
        else:
            pass
        # check each restaurant, append its info into csv file.
       
           
        name = getRestaurantsName(type)
        price = getRestaurantsprice(type)
       
        star = getRestaurantsRating(type)
        review_count = getRestaurantsReview(type)
        
        i=0
        
        while i < 57:       
                
            with open(file, 'a',newline='') as f: # note the mode is 'a', append
                 writer = csv.writer(f)
                 
                 writer.writerow([name[i], price[i], review_count[i], star[i]])
            i+=1    

    


#Their prices are represented by a bar graph
def compare_price(type1,type2):
    def get_data(type):
        df1 = pd.read_csv('yelp_%s.csv'%(str(type)), encoding='cp1252')    
        price_value1 = df1['Price'].values
        max_type=max(price_value1)
        type1_top=df1.loc[lambda df1:df1['Price']==str(max_type)]
        print('The most expensive of %s restaurant is:'%(str(type)))
        print(type1_top)

        a1=0
        b1=0
        c1=0
        d1=0

        for value in price_value1:
            if value =='$':
                a1=a1+1
            elif value=='$$':
                b1+=1
            elif value=='$$$':
                c1+=1
            elif value == '$$$$':
                d1+=1

        price1=(int(a1), int(b1), int(c1),int(d1))
        return price1
    
    
    price1=get_data(type1)
    print(price1)
    price2=get_data(type2)
    ind = np.arange(len(price1))  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, price1, width, 
                color='SkyBlue', label='%s'%(str(type1)))
    rects2 = ax.bar(ind + width/2, price2, width, 
                color='IndianRed', label='%s'%(str(type2)))
    ax.set_ylabel('price')
    ax.set_title('price by type')
    ax.set_xticks(ind)
    ax.set_xticklabels((str('1$'), str('2$'),str('3$'), str('4$')))
    ax.legend()
        
    def autolabel(rects, xpos='center'):
        """
        Attach a text label above each bar in *rects*, displaying its height.

        *xpos* indicates which side to place the text w.r.t. the center of
        the bar. It can be one of the following {'center', 'right', 'left'}.
        """

        xpos = xpos.lower()  # normalize the case of the parameter
        ha = { 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.3, 'left': 0.7}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


    autolabel(rects1, "left")
    autolabel(rects2, "right")


    plt.show()

#Represented by histogram    
def compare_star(type1,type2):
    df1 = pd.read_csv('yelp_%s.csv'%(str(type1)), encoding='cp1252') 
    df2 = pd.read_csv('yelp_%s.csv'%(str(type2)), encoding='cp1252')    
    star_value1 = df1['Star'].values
    star_value2 = df2['Star'].values
    fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 4))

    ax0.hist(star_value1, 6, normed=1, histtype='stepfilled', facecolor='g', alpha=0.5)
    ax0.set_title('%s'%(str(type1)))
    ax1.hist(star_value2, 6, normed=1, histtype='stepfilled', facecolor='r', alpha=0.5)
    ax1.set_title('%s'%(str(type2)))
    ax0.set_xlabel('Stars')

    ax1.set_xlabel('Stars')
    fig.tight_layout()
    plt.show()
    max_type1=max(star_value1)
    max_type2=max(star_value2)
    type1_top=df1.loc[lambda df1:df1['Star']==max_type1]
    type2_top=df2.loc[lambda df2:df2['Star']==max_type2]
    print('The highest rated of %s restaurant is:'%(str(type1)))
    print(type1_top)
    print('The most expensive of %s restaurant is:'%(str(type2)))
    print(type2_top)
 
       
#represented by a bar graph
def compare_review(type1, type2):

    df1 = pd.read_csv('yelp_%s.csv'%(str(type1)), encoding='cp1252')
    df2 = pd.read_csv('yelp_%s.csv'%(str(type2)), encoding='cp1252')  
    review_type1=df1['Review_count'].values
    review_type2=df2['Review_count'].values
    max1=max(review_type1)
    max2=max(review_type2)
    min1=min(review_type1)
    min2=min(review_type2)
    mean1=review_type1.mean()
    mean2=review_type2.mean()
    median1=np.median(review_type1)
    median2=np.median(review_type2)
    review1=(max1,min1,mean1,median1)
    review2=(max2,min2,mean2,median2)
    
    ind = np.arange(len(review1))  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, review1, width, 
                color='SkyBlue', label='%s'%(str(type1)))
    rects2 = ax.bar(ind + width/2, review2, width, 
                color='IndianRed', label='%s'%(str(type2)))
    ax.set_ylabel('Review_count')
    ax.set_title('Review_count by type')
    ax.set_xticks(ind)
    ax.set_xticklabels((str('max'), str('min'),str('mean'), str('median')))
    ax.legend()
    def autolabel(rects, xpos='center'):
        """
        Attach a text label above each bar in *rects*, displaying its height.

        *xpos* indicates which side to place the text w.r.t. the center of
        the bar. It can be one of the following {'center', 'right', 'left'}.
        """

        xpos = xpos.lower()  # normalize the case of the parameter
        ha = { 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.3, 'left': 0.7}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


    autolabel(rects1, "left")
    autolabel(rects2, "right")
    

    plt.show()
    
    type1_top=df1.loc[lambda df1:df1['Review_count']==int(max1)]
    type2_top=df2[lambda df2:df2['Review_count']==int(max2)]
    print('The most reviewed %s restaurant is:'%(str(type1)))
    print(type1_top)
    print('The most reviewed %s restaurant is:'%(str(type2)))

    print(type2_top)


def main():
    type1="Chinese"
    type2="Japanese"
    write_csv(type1)
    write_csv(type2)   
    print('----------------------------------------') 
    compare_price(type1,type2)
    print('----------------------------------------') 
    compare_star(type1,type2)
    print('----------------------------------------') 
    compare_review(type1, type2)   
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    