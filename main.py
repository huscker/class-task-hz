import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('zillow.csv')
beds = data['Beds'].unique()
vals = []
for i, el in enumerate(beds):
    vals.append(data[data['Beds'] == el]['Baths'].min())
print(beds)
print(vals)
plt.bar(beds,vals)
plt.show()
