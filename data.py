import pandas as pd
df = pd.read_html('https://erddap.tamucc.edu/erddap/tabledap/COAPS_N7.htmlTable?time%2Cdepth&time%3E=2000-03-04T13%3A06%3A06Z&time%3C=2016-07-01T21%3A00%3A00Z')[1]
car_df = pd.DataFrame(df)
df2= car_df['depth']
n = len(pd.unique(df2['m']))
print(n)
# df = pd.read_csv("D:\ERRDAP\dataset-ERDDAP2.csv")
  
# # updating the column value/data
# df.loc[68, 'Count_depth'] = 'SHIV CHANDRA'
  
# # writing into the file
# df.to_csv("D:\ERRDAP\dataset-ERDDAP2.csv", index=False)
  
# print(df)