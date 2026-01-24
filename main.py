import pandas as pd
import os 

df=pd.read_csv(r"C:\Users\nice\Desktop\Mlops\DVC\data\data.csv")
new={"name":"g1",
     "country":"qatar",
      "age":45}
df.loc[len(df.index)]=new
df.to_csv(r"C:\Users\nice\Desktop\Mlops\DVC\data\data.csv", index=False)