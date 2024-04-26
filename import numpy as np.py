import numpy as np

import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Downloads\is-the-traffic-collision-fatal\Train.csv")
df.head()


df.info()



df.isna().mean()




df.describe()

import matplotlib.pyplot as plt

df.hist(bins=60,figsize=(20,20))

import seaborn as sns







