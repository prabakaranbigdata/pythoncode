%matplotlib inline
import numpy as np
import pandas as pd
df=pd.read_csv("C:\\MLCourse\\PastHires.csv")
df.head()
df_new=df[["Previous employers","Hired"]][5:10]
df_new.head()
df_new.plot(kind='hist')

import numpy as np
income=np.random.normal(27000,15000,10000)
np.mean(income)

%matplotlib inline
import matplotlib.pyplot as plt
plt.hist(income,50)
plt.show()

import scipy.stats as sp
sp.mode(income)