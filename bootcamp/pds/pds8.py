#csv
#html
#sql
#excel

#sqlalchemy
#lxml
#html5lib
#BeautifulSoup4


pd.read_csv('file.csv')
pd.read_excel('file.xlsx',sheetname = 'Sheet1')
data = pd.read_html('http://www.google.com/') # return list -> panda return all the table elements of the page, df of each table of the html page
data[0].head() #->first table

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory')
df.to_sql('my_table',engine)
sqldf = pd.read_sql('my_table',con=engine)



df.to_csv('output',index=False)#index=False is important because, it will give the output normal, or it will also save the index
df.to_excel('output.xlsx',sheetname = 'new Sheet')