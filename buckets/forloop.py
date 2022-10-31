import pandas as pd

minutes = 2


data = {
   'data': [0,1,2,3,4,5,6,7,8,9]
}

df = pd.DataFrame(data)

# reverses data frame #
#df = df.iloc[::-1]

#print(df)
for i in range(0, len(df), minutes):
    print(df[i:i+minutes].max())
   # print(df['data'].max())



# for loop numbers must match #
# data = [0,1,2,3,4,5,6,7,8,9]

# data.reverse()
# for i in range(0, len(data), 4):
#     print(data[i:i+4])