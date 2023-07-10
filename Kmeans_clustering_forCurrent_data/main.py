import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans

df = pd.read_csv("current_data.csv")
#print(df)
# df['_time'] = df['_time'].fillna(0)
# df['_value']= df['_value'].fillna(0)
# df.replace(np.nan,0)


df['time'] = pd.to_datetime(df['_time'],errors='coerce')
time = df['time']
value = df['_value']
print(df)


plt.scatter(time,value)
plt.xlabel('Time')
plt.ylabel('Current in Amperes')
plt.show()


# time_sec = list(pd.to_timedelta(df['_time'], errors="coerce").dt.total_seconds ())
#
# data = list(zip(time_sec,value))
# hierarchical_cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
# labels = hierarchical_cluster.fit_predict(data)
# plt.scatter(time_sec, value, c=labels)
# plt.show()


# kmeans = KMeans(n_clusters=3)
# kmeans.fit(data)
#
# plt.scatter(time_sec, value, c=kmeans.labels_)
# plt.show()
