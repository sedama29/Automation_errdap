import sqlite3
connection = sqlite3.connect("D:\database_new\gcoos_data_v3.sqlite")
connection2 = sqlite3.connect("D:\database_new\gcoos_data_v2.sqlite")
connection3 = sqlite3.connect("D:\database_new\gcoos_data_v1.sqlite")
crsr = connection.cursor()
crsr2 = connection2.cursor()
crsr3 = connection3.cursor()
crsr.execute('''SELECT rowId, sensorTypeId from sensor where lastObsDate = "" or lastObsDate = NULL''')
ans = crsr.fetchall()
print(ans[1])
# g,h =[],[]
# q,r=0,0
# for k in ans:
#     g.insert(q,k[0])
#     q=q+1
# for x in ans:
#     h.insert(r,x[1])
#     r=r+1
# print(h)

k,l,m,n,o,p=0,0,0,0,0,0
a,b,c,d,e,f=[],[],[],[],[],[]
# x = ['waterTemperature','airPressure', 'airTemperature','winds','salinity','waterLevel','relhumidity','dewPoint','chlorophyll','dissolvedOxygen','turbidity','wave','oceanCurrents']
# for i in x:
#     for j in g:
#         crsr.execute("select sensorId, max(observationDate) from '" + i + "' where sensorId ==?",(j,))
#         ans2 = (crsr.fetchall())
#         # print(ans2[0][0])
#         if ans2[0][0] == None:
#             a.insert(k,j)
#             k=k+1
#         else:
#             b.insert(l,j)
#             l=l+1
#     print('sensorIds of missing last observation dates found in '+i+' table of v3 version are:',b)
#     for j in a:
#         crsr2.execute("select sensorId, max(observationDate) from '" + i + "' where sensorId ==?",(j,))
#         ans3 = (crsr2.fetchall())
#         if ans3[0][0] == None:
#             c.insert(m,j)
#             m=m+1
#         else:
#             d.insert(n,j)
#             n=n+1
#     print('sensorIds of missing last observation dates found in '+i+' table of v2 version are:',d)

#     for j in c:
#         crsr3.execute("select sensorId, max(observationDate) from '" + i + "' where sensorId ==?",(j,))
#         ans4 = (crsr3.fetchall())
#         if ans4[0][0] == None:
#             e.insert(o,j)
#             o=o+1
#         else:
#             f.insert(p,j)
#             p=p+1
#     print('sensorIds of missing last observation dates found in '+i+' table of v1 version are:',f)
#     print('sensorIds of missing last observation Date are',e)
#     g = e
#     a,b,c,d,e,f = [],[],[],[],[],[]
#     k,l,m,n,o,p = 0,0,0,0,0,0






    
