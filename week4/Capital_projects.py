import csv

def logMalformedproject(projects):
    with open('none_area', 'a') as log:
        log.write(projects['id'])
        log.write('\n')
        

def listprojects():
    file=open('PittsCityCapitalProject.csv', newline='')
    projects=csv.DictReader(file)
    
    
    for row in projects:
        print('name:' + row['name'])
        print('inactive:'+row['inactive'])
        
        print('fiscal_year:'+row['fiscal_year'])
        print('budgeted_amount:'+row['budgeted_amount'])
        print('task_description:' + row['task_description'])
        print('start_date:'+ row['start_date'])
        print('area:' + row['area'])
        print('asset_id:' + row['asset_id'])
        print('status:' + row['status'])
        print('id:' + row['id'])
        print('--------------------------')
        
def fill_in():
    file=open('PittsCityCapitalProject.csv', newline='')
    projects=csv.DictReader(file)
    
    
    for row in projects:
        if row['area']=='':
            logMalformedproject(row)
            
            
     

listprojects()
fill_in()
        
        
        
        

