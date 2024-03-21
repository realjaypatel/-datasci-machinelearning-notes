import pandas as pd
import numpy as np

#groupby allows you to group together rows, ans show you the sum, perfomr an aggregate of the values
data= {'Company' : ['GOOG' , 'GOOG', 'MSFT', 'MSFT','FB','FB'],
'Person' : ['Sam', 'Charlie', 'Amy' , 'Vanessa' , 'Carl', 'Sarah'],
'Sales ' : [200, 120, 340, 124,243,350]
}

df = pd.DataFrame(data)
bycomp = df.groupby('Company')
bycomp.mean()
bycomp.sum()
bycomp.std()
df.groupby('company').sum().loc['FB']
df.groupby('company').count()
df.groupby('company').max()
df.groupby('company').describe() #.transpose give in a single line #bohooottt important, give every details of the data

