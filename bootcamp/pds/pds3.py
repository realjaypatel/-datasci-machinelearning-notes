import pandas as pd
import numpy as np


outside =['G1', 'G1', 'G1', 'G2', 'G2','G2']
inside = [1,2,3,1,2,3]
hier_index= list(zip(outside,inside)) #-> zip the list of tuple pairs,(G1,1),(62,2)
hier_index = pd.MultiIndex.from_tuples(hier_index) #multi index
df = pd.DataFrame(np.random.randn(6,2),hier_index,['A','B']) #created a grop of grop
df.loc['G1']
df.index.names = ['Groups','Nums']#pass the list of name coz, there is no name for the index part
print(df.loc['G1']['A'][2]) #print(df.loc['G1'][2]['A']) A->2, 2->A
df.xs('G1') #cross section examplee, i want num == 1 in both the group
df.xs(1,level='Num')

