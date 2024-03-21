import numpy as np
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()
df['col2'].unique()#return the numpy array, if you want the original array
df['col2'].nunique() #number of unique values
df['col2'].value_counts() #return number of times the value is repeating
df[df['col1']>2]
#applied mathod is one of the powerful tool

def times2(x):
    return x**2
df.apply(times2)
df.apply(lambda x:x**2) #lambda compatable
df.apply(len)
df.drop('col1',axis = 1)#to drop in column
df.columns #return all the columns
df.index #return information of index

#sorting ordering df
df.sort_values(by='col2')
df.isnull() # return boolean of the df

#for rotating the pandas thing
df.pivot_table(values='D',index=['A', 'B'],columns=['C'])


