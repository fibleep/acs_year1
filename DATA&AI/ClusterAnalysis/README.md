# Cluster Analysis
## Introduction
Can be considered an Automated Data Exploration Methods, or as a form of Unsupervised (machine) Learning.

A cluster is a number of rows of a table that
"belong together" or are "similar to each other "\
column -> one dimension (note: a column is a variable)\
row -> a point in a n-dimensional space\
2 rows are similar if the points in the n-dimensional\
space are "close" to each other -> the "distance" between the 2 points must be small

## Distance
Cluster analysis requires a distance function
between points (or a similarity measure or
disimilarity measure)

### Euclidean Distance
The distance between 2 points in a n-dimensional space is the 
root of the sum of the squares of the differences between the coordinates of the points.\
in short, Pythagorean theorem.

### Manhattan Distance
The distance between 2 points in a n-dimensional space is the sum of the absolute values of the differences between the coordinates of the points.

## In Search of Clusters
### K-Means
K-Means is a clustering algorithm that is used to group similar data points together. \
It selects k number of clusters and then assigns each data point to the cluster that is closest to it.

Algorithm:
- Select k random points("centroids") 
- loop:
     - associate each point of the dataset with the centroid
    closest to it (this is how you create k clusters)\
    - calculate per cluster the "middle" and replace the
centroid by this new value
until the centroids do not change anymore
### Hierarchical Clustering
o    Single Linkage: – In single linkage the distance between the two clusters is the shortest distance between points in those two clusters.

o   Complete Linkage: – In complete linkage, the distance between the two clusters is the farthest distance between points in those two clusters.

o   Average Linkage: – In average linkage the distance between the two clusters is the average distance of every point in the cluster with every point in another cluster.

Algorithm:\
Start "at the bottom": \
each point is a cluster with 1 element in it (n clusters)
- Loop:
- find the 2 clusters that are closest to each other
- add these clusters together until only 1 cluster remains
### Density Based
K-means and hierarchical clustering are suitable for compact
and well-separated clusters but they are also severely
affected by the presence of noise and outliers in the data.


- DBSCAN algorithm is a Density based clustering method.
- Two parameters required:
- eps: radius around a datapoint that is considered as the
neighbourhood of that data point. In other words, if the
distance between two points is lower or equal to eps then they
are considered as neighbours.
- minPts: minimum number of neighbours (data points) within
eps radius.

Algorithm:
- A starting point is selected at random and it’s neighbourhood area is
determined using radius eps.
- - If there are at least minPts number of points in the neighbourhood, the
point is marked as core point and a cluster formation starts.
- - If not, the point is marked as outlier/noise.
- Once a cluster formation starts (let’s say cluster C), all the points within
the neighbourhood of the initial point become a part of cluster C. If these
new points are also core points, the points that are in the neighbourhood of
them are also added to cluster C. Etc.
- Next step is to randomly choose another point among the points that have
not been visited in the previous steps. Then same procedure applies.
- This process is finished when all points are visited.