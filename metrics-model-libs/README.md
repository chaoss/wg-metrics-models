# Metrics Models Mindmap


![Metrics Models Mindmap](https://github.com/chaoss/wg-metrics-models/tree/main/metrics-model-libs/libs-mindmap/mindmap.svg)

# metrics-model-libs Structure

metrics-model-libs is used to store all the metrics models, following the structure as below: 

```
metric-model-libs
└───Model A 
|   |   definition
|   |   implementations
|   |   |   implementation A 
|   |   |   |   algorithm
|   |   |   |   data-insight
|   |   |   |   data
|   |   |   implementation B
|   |   |   |   algorithm
|   |   |   |   data-insight
|   |   |   |   data
└───Model B
|   |   definition
|   |   implementations
└───Model C
|   |   definition
|   |   implementations
```



# Metrics Model Definitions

The detailed definition template can be found [here](https://github.com/chaoss/community/blob/main/templates/metrics-model-template.md)

# Metrics Model Implementations

The goal of this is to implement the metrics models with real-world community data set. 
You may have multiple implementations for the same Metrics Model:
* implementation A : Implementation in field A with real world data, for exmaple linux distributions communities. 
* implementation B : Implementation in field B with real world data, for example AI platform communities.

For each implementaion, it includes three parts:
* data : real-world community data set. It should be some clean data provided by Augur or Grimoirelab(or any other data handling tools ), that is easily handled by Jupyter. 
* algorithm : For each single metric model, it would have a set of metrics. The goal of algorithm is to find a single value that represents all the metrics for a metrics model in a meanningful way.   
* data-insight : Provide text and visualizations in Jupyter notebook that describes how the unified metrics model is used to draw insights from the evaluated community or communities.


# Metrics Model Steps Forward

We believe that the model we designed is in the step 2. 

![image](https://user-images.githubusercontent.com/12421382/165404599-22e4f596-3023-4562-bba5-4bc77ab19f3b.png)


For example:
![image](https://user-images.githubusercontent.com/12421382/165404675-31eb52f4-9593-4e39-8002-a00088e278f4.png)


