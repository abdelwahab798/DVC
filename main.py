import pandas as pd
import os 

df=pd.read_csv(r"C:\Users\nice\Desktop\Mlops\DVC\data\data.csv")
new={"name":"abdelrahamn",
     "country":"qatar",
      "age":45}
df.loc[len(df.index)]=new
new2={"name":"sdf1",
     "country":"jordan",
      "age":62}
df.loc[len(df.index)]=new2
df.to_csv(r"C:\Users\nice\Desktop\Mlops\DVC\data\data.csv", index=False)