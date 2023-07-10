import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


df = pd.read_csv("current_data.csv")
df['_time'] = pd.to_datetime(df['_time'],errors='coerce')
df['_time']= df['_time'].dt.hour + df['_time'].dt.minute/60

scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)
kmeans = KMeans(n_clusters=3, random_state=0, init="k-means++")
kmeans.fit(scaled_data)
df["clusters"] = kmeans.labels_

print(df)

plt.scatter(df['_time'], df['_value'], c=df["clusters"])
plt.show()
