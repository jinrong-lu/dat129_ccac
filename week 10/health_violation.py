import numpy as np
import pandas as pd

violationsdf = pd.read_csv('foodinspectionviolations_alghcnty.csv')


#What types of health violations are most common in the municipal area
def most_common_violation(municipalArea):
    area=str(municipalArea)
    
    df=violationsdf.loc[lambda violationsdf:violationsdf['municipal']==area]

    common_list=df['description_new'].value_counts()
    print('The most common type of health violations in %s is:'%(area))
    print(common_list.head(1))
    
 
#Which types of violations are mostly only considered "high" severity
def  high_severity_violation():
    highseverity=violationsdf.loc[lambda violationsdf:violationsdf['high']=='T']
    common_list=highseverity['description_new'].value_counts()
    print('The mostly only considered "high" severity violation is:')
    print(common_list.head(1))
    

#Which classification of restaurant has the most "high" severity violations
def restaurant_high_severity():
    highseverity=violationsdf.loc[lambda violationsdf:violationsdf['high']=='T']
    common_list=highseverity['description'].value_counts()
    print('The restaurant which has the most "high" severity violations is:')
    print(common_list.head(1))
    
def main():
    most_common_violation('Robinson')
    print('---------------------------------------------------------------')
    most_common_violation('Oakmont')
    print('---------------------------------------------------------------')
    most_common_violation('Pittsburgh-104')
    print('---------------------------------------------------------------')
    high_severity_violation()
    print('---------------------------------------------------------------')
    restaurant_high_severity()

main()
