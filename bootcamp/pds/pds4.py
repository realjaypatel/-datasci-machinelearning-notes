import pandas as pd
import numpy as np
d= {'A' :[1,2,np.nan], 'B' :[5,np.nan,np.nan], 'C' :[1,2,3]}
df = pd.DataFrame(d)
df.dropna() # axis = 0 columns, here it will drop the whole row if the value is Nan #thresh = 2: if the row has two NaN then it will drop
df.fillna(value = "fil value")# fill the value with this value
df['A'].fillna(value = df['A'].mean())