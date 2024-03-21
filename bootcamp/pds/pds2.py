import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5,4),['A','b','c','d','e'],['w','x','y','z'])

df[df>0] #conditional selection, like numpy
df[df['w']>0] #you will get only the row where it happens to be true
df[df['w']>0]['x'] #-> since that return the dataframe, i can use it like a dataframe
# and -> & 
# or -> |
df[(df['w']>0) & (df['x']<0)] #multiple operation we use & here
df.reset_index() #add a column named index with the index values you specify

#adding a new column with custom data
df['state'] = 'ca ba da as df'.split()
df.set_index('States') #return the index values converted to the states



