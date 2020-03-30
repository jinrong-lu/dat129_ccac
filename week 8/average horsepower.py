#Compare the average horsepower of SUV and Mid-Size Truck

import urllib
from bs4 import BeautifulSoup



def getSearchURL(term):
    url="https://www.kbb.com/%s/"%(str(term))
    return url

def getPageText(url):
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return response.read()

def caculateHorsepower(term):
    url = getSearchURL(term)
    pageText = getPageText(url)
    soup = BeautifulSoup(pageText, 'html.parser')
    horsepowertags = soup.find_all('div', title="Horsepower")
    
    total_horsepower=0
    total_cars=0
    for cars in horsepowertags:
        cars_horsepower=cars.find('div').string
        total_horsepower+= int(cars_horsepower)
        total_cars= total_cars+1
  
    average_horsepower=total_horsepower/total_cars
    return average_horsepower

def compare(a,b):
    term1=str(a)
       
    average1='{:.2f}'.format(caculateHorsepower(term1))
    print('the average horsepower of %s is: '%(str(term1)), average1)
    term2=str(b)
    average2='{:.2f}'.format(caculateHorsepower(term2))
    print('the average horsepower of %s is: '%(str(term2)), average2)
    if average1 > average2:
        print('%s has more average horsepower!'%str(term1))
    elif average1 < average2:
        print('%s has more average horsepower!'%str(term2))
    else:
        print('They have same average horsepower!')
        
    
def main():
    a="suv"
    b="pickup-truck"
    compare(a,b)

main()