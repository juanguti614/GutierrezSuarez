import pandas as pd
import matplotlib as plt
import numpy as np
import matplotlib.pyplot as plt


fcbk =['Facebook',41214,2142,2215,True]
twtr= ['Twitter',22514,22541,666,False]
instgr=['Instagram',66523,22546,2254,True]
snpch= ['Snapchat',332511,22514,66524,False]
d= [fcbk,twtr,instgr,snpch]
#creacion de dataframe
t=pd.DataFrame(d,columns=['Nombre','Cantidad','Likes','Ranking','Recomendable'])
print(t)
plt.bar(t['Nombre'],t['Cantidad'])
plt.show()

plt.bar(t['Nombre'],t['Cantidad'],color=['r','m','c','k','b','g'])
plt.show()

plt.title("Cantidad de usuarios")
Datos = [41214,22514,66523,332511]
nombres = ["Facebook","Twitter","Instagram","Snapchat"]
plt.pie(Datos,labels=nombres, autopct="%0.1f %%")
plt.show()


plt.title("Crecimiento en el ranking de Instagram")
plt.plot([0,2254],'#9370DB')
plt.show()

fig, ax = plt.subplots()
plt.title("Cantidad de likes")
ax.barh([1,2,3,4 ], [2142, 22541,22546, 66524])
plt.show()



