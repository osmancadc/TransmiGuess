"""
  @Autor: Osman Beltran Murcia
  @Date: Jue 09/May/2019
"""
import random
import math
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
def read_file(name):
  name+=".txt"
  data=pd.read_csv(name,header=0,delim_whitespace=True)
  x=data.ix[:,1]
  y=data.ix[:,0]
  return [x,y]
#end def

def rect(x,y,w,h,c):
    ax = plt.gca()
    polygon = plt.Rectangle((x,y),w,h,color=c)
    ax.add_patch(polygon)
#end def

# grafica la data del polinmio ajustado y los puntos originales
def graph_data(X,Y, cmap=plt.get_cmap("jet")):
  m=-math.inf
  plt.clf()
  for i in range (0,len(Y)):
    if(Y[i]>m):
      m=Y[i]
  #end for
  m=0.9/m

  plt.plot(X,Y,lw=0) # Plot so the axes scale correctly
  dx = X[1]-X[0]
  N = float(len(X))

  for n, (x,y) in enumerate(zip(X,Y)):
    color = cmap(Y[n]*m)
    rect(x,0,dx,y,color)
  #end for
  plt.savefig("graph.png")
  #plt.show()
#end def


#retorna el polinmoio ajustado deacuerdo a un arreglo de datos [x,y]
def get_polim(x,y):
  coef = np.polyfit(x,y,4)
  polinomio=np.poly1d(coef)
  #print(polinomio)
  return polinomio
#end def


#Retorna la cantidad de pasajeros en una hora especifica
def get_cantidad(hour,route):
    hour=int(hour)
    data = read_file(route)
    x=data[0]
    y=data[1]

    if(hour<=12):
        x=x[0:8]
        y=y[0:8]
    else:
        x=x[7:19]
        y=y[7:19]

    f=get_polim(x,y)
    return  int(f(hour))
#end def

#Retorna la diferencia de pasajeros entre dos horas "n" y "m"
def get_diferencia(n,m,route):
  data = read_file(route)
  x=data[0]
  y=data[1]

  if(n<=12):
    xn=x[0:8]
    yn=y[0:8]
  else:
    xn=x[7:19]
    yn=y[7:19]

  if(m<=12):
    xm=x[0:8]
    ym=y[0:8]
  else:
    xm=x[7:19]
    ym=y[7:19]

  fn=get_polim(xn,yn)
  fm=get_polim(xm,ym)

  final=int(fn(n))-int(fm(m))

  if(final>0):
      return "a las "+str(n)+" hay "+str(final)+" personas mas que a las "+str(m)
  elif(final<0):
      return "a las "+str(n)+" hay "+str(final*-1)+" personas menos que a las "+str(m)
  else:
      return "ambas horas seleccionadas tienen exactamente la misma cantidad de pasajeros"
#end def

def get_momento(n):
    if(n<=12):
        return 1
    elif (n<=18):
        return 2
    return 3
#end def

#1-Maniana 2-Tarde 3-Noche
def get_plot(h,route):
  data = read_file(route)
  x=data[0]
  y=data[1]
  h=int(h)
  h=get_momento(h)
  #0-7 maniana 7-13 tarde 13-18 noche
  if(h==1):
    x=x[0:8]
    y=y[0:8]
    a=x[0]
    b=x[7]
  elif(h==2):
    x=x[7:14]
    y=y[7:14]
    a=x[7]
    b=x[13]
  else:
    x=x[13:19]
    y=y[13:19]
    a=x[13]
    b=x[18]
  f=get_polim(x,y)

  x=[]
  while(a<b):
    x.append(a)
    a+=.005
  #end while
  y=f(x)
  graph_data(x,y)
#end def
"""
","", "","","",
     "","","","","","",
     "","","
"""
def get_filename(t):
    if(t=="Suba N-S"):
        return "subans"
    elif(t=="Suba S-N"):
        return "subasn"
    elif(t=="NQS-Soacha S-N"):
        return "nqssn"
    elif(t=="Auto norte N-S"):
        return "nortens"
    elif(t=="Auto norte S-N"):
        return "nortesn"
    elif(t=="Calle 80 Occ-Or"):
        return "cll80ocor"
    elif(t=="Av americas Occ-Or"):
        return "americasocor"
    elif(t=="Av americas Or-Occ"):
        return "americasoroc"
    elif(t=="Calle 80 Or-Occ"):
        return "cll80oroc"
    elif(t=="Cacacas N-S"):
        return "caracasns"
    elif(t=="Cacacas S-N"):
        return "caracassn"
    elif(t=="Calle 26 Occ-Or"):
        return "cll26ocor"
    elif(t=="Calle 26 Or-Occ"):
        return "cll26oroc"
    elif(t=="NQS-Soacha N-S"):
        return "nqsns"
#end def


#n= int(input("Ingresa la hora que quieres predecir: "))
#print(get_cantidad(n,"americasI"))
#get_plot(n,"americasV")

#n= int(input("Ingresa la hora que quieres predecir: "))
#m= int(input("Ingresa la hora que quieres comparar: "))
#print(get_diferencia(n,m,"americasI"))



#n= int(input("Ingresa el momento del dia (1,2,3): "))
