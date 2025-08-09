import pandas as pd
import numpy as np


df = pd.read_csv('/dataset/mydataset.csv')
print(df.head())
print(df.info())
print(df.describe())

