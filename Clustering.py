# importing necessary libraries
import pandas as pd
import numpy as np
# !pip install kmodes
from kmodes.kmodes import KModes
import matplotlib.pyplot as plt
import argparse

#Function 
def Clustering(df):
    df = df.dropna()
    data2=df[['dateStart','quantity','product','language','New origin','New staffCount','JobTitle','customer']]
    data=df[['quantity','product','language','New origin','New staffCount','JobTitle']]
    # Elbow curve to find optimal K number of clusters
    cost = []
    K = range(1,5)
    for num_clusters in list(K):
        kmode = KModes(n_clusters=num_clusters, init = "random", n_init = 5, verbose=1)
        kmode.fit_predict(data)
        cost.append(kmode.cost_)
    plt.plot(K, cost, 'bx-')
    plt.xlabel('No. of clusters')
    plt.ylabel('Cost')
    plt.title('Elbow Method For Optimal k')
    plt.show()
     # Building the model with 3 clusters
    kmode = KModes(n_clusters=3, init = "random", n_init = 5, verbose=1)
    clusters = kmode.fit_predict(data)
    clusters
    data.insert(0, "Cluster", clusters, True)
    data['dateStart']=data2['dateStart']
    data['customer']=data2['customer']
    return data


if __name__== "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-source", type=argparse.FileType('r'))
    parser.add_argument('-destination', type=argparse.FileType('w', encoding='latin-1'))
    args = parser.parse_args()
    print(args.source.name)
    print(args.destination.name)
    #Import the dataset
    dataset= pd.read_csv(args.source.name,delimiter=";")
    DataWithClusters= Clustering(dataset)
    #export the new data in a csv file
    DataWithClusters.to_csv(args.destination.name)

