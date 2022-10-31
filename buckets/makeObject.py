import pandas as pd
import numpy as np

data = {
    'data':[9,8,7,6,5,4,3,2,1,0]
}


df = pd.DataFrame(data)


bs = 5

b = np.split(df,bs)

print(b)