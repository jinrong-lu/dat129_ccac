import csv

def area_budgeted_amount():
    file=open('PittsCityCapitalProject.csv', newline='')
    
    reader = csv.DictReader(file)
    
    area_total={'Administration/Sub-Award':0, 
                'Engineering and Construction':0,
                'Facility Improvement':0, 
                'Neighborhood and Community Development':0,
                'Public_Safety':0,
                'Vehicles and Equipment':0}
    for row in reader:
        if row['area']=='Administration/Sub-Award':
            area_total['Administration/Sub-Award']+=float(row['budgeted_amount'])
            
        elif row['area'] == 'Engineering and Construction':
            area_total['Engineering and Construction']+=float(row['budgeted_amount'])
            
        elif row['area'] == 'Facility Improvement':
            area_total['Facility Improvement']+=float(row['budgeted_amount'])
            
        elif row['area'] == 'Neighborhood and Community Development':
            area_total['Neighborhood and Community Development']+=float(row['budgeted_amount'])
        
  
        elif row['area'] == 'Vehicles and Equipment':
            area_total['Vehicles and Equipment'] += float(row['budgeted_amount'])
            
        elif row['area'] == 'Public_Safety':
            area_total['Public_Safety'] += float(row['budgeted_amount'])
    for k in area_total:
        print('The budgeted_amount of'+k+ 'is:'+str(area_total[k]))
    
    return area_total

def computerpercent(budgeted_amountDict):
    total=0
    for k in budgeted_amountDict:
        total+=budgeted_amountDict[k]
        
    for k in budgeted_amountDict:
        perc=budgeted_amountDict[k]/total
        print("Percent of "+k+": "+"{0:.2%}".format(perc))
        
    
def main():
    

    a=area_budgeted_amount()
    computerpercent(a)
main()
    
        
            
                
            
            
    
    

