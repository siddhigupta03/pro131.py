import pandas as pd

df = pd.read_csv("final_data.csv")

df.drop(['Unnamed: 0'],axis=1,inplace=True)

df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

radius = df["Radius"].to_list()
mass = df["Mass"].to_list()

def convert_to_si(radius,mass):
  for i in range(0,len(radius)-1):
      radius[i] = float(radius[i])*6.957e+8
      mass[i] = float(mass[i])*1.989e+30

convert_to_si(radius,mass)

gravity = []
def grav_calc(mass,radius):
  G = 6.674e-11
  for index in range(0,len(mass)):
      g= (mass[index]*G)/((radius[index])**2)
      gravity.append(g)
        
grav_calc(radius,mass)

df["Gravity"] = gravity

df.to_csv("with_gravity.csv")