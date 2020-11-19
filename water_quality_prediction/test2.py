import pandas as pd

df = pd.DataFrame(data=[
  {'Name': "panda", 'Age': 5,},
  {'Name': "usagi", 'Age': 11,},
  {'Name': "koara", 'Age': 45}
])
df.to_excel("test.xlsx", index=False, startrow=1)