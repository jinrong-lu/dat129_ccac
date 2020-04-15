

import numpy as np
import pandas as pd

Pittsburgh_trees=pd.read_csv('City of Pittsburgh Trees.csv')
print(Pittsburgh_trees['common_name'].value_counts())

most_numerous_trees=Pittsburgh_trees.loc[lambda Pittsburgh_trees: Pittsburgh_trees['common_name']=='Maple: Norway']
average_high=np.mean(most_numerous_trees['height'])
print('The average height of "Maple: Norway" is:',average_high)
print('------------------------------------------------')


energy_benefits_electricity=np.sum(most_numerous_trees['energy_benefits_electricity_dollar_value'])
energy_benefits_gas=np.sum(most_numerous_trees['energy_benefits_gas_dollar_value'])
total=energy_benefits_electricity+energy_benefits_gas
print('The total money from energy benefits is:', total)
print('------------------------------------------------')


