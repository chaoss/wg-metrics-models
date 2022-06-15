# Ecosystem

## Context Description

Ecosystem is used to describe the health status of open source community standing from ecology context. (Note. Not all the open source communities or projects could be likened as an ecosystem, it should be able to be provided as a software platform, e.g. os, cloud infra, ide etc.)

We create three top level dimensions: Productivity, Robustness and Niche. Under each dimension,  we select metrics models from metrics-model-libs and categorize them by software artifact and social. The software artifacts aspect is about the tangible materials related to OSS projects including but not limited to source code, documents, binaries, etc. The social aspect is about the people involved in OSS projects, which focuses on the individuals, teams, organizations, their activities and interactions, social networks and communities, etc, in OSS projects.

Hierarchy depth of metrics models depends on complexity of metrics and models.

```
Ecosystem
└───Productivity
│   |   Software Artifact
|   |   |   metrics models
|   |   Social
|   |   |   metrics models
└───Robustness
│   |   Software Artifact
|   |   |   metrics models
|   |   Social
|   |   |   metrics models
└───Niche
│   |   Software Artifact
|   |   |   metrics models
|   |   Social
|   |   |   metrics models
```

## Dimensions

### **Productivity**
Definition: The efficiency with which an ecosystem converts inputs into output.

#### Software Artifact
* code-quality(example)
#### Social

### **Robustness**
Definition: The capability of an ecosystem to face and survive disruptions.

#### Software Artifact
#### Social
* [community-activity](../metrics-model-libs/community-activity)
* [community-welcomingness](https://github.com/chaoss/wg-metrics-models/tree/main/implementations/community-welcomingness)
* [funding](https://github.com/chaoss/wg-metrics-models/tree/main/implementations/funding)
### **Niche**:
Definition: The capacity to create meaningful diversity and thereby novel capabilities.
#### Software Artifact
#### Social
* community-diversity(example)
## References:
* [Open Source Community Health: Analytical Metrics and Their Corresponding Narratives](https://ieeexplore.ieee.org/abstract/document/9474775) 2021, Sean Goggins; Kevin Lumbard; Matt Germonprez
* [Measuring the health of open source software ecosystems: Beyond the scope of project health](https://www.sciencedirect.com/science/article/pii/S0950584914000871) 2014, SlingerJansen
* [Defining and Evaluating a Measure of Open Source Project Survivability](https://ieeexplore.ieee.org/abstract/document/6127835) 2012, Uzma Raja; Marietta J. Tretter
* [The Health Measurement of a Business Ecosystem](https://www.researchgate.net/profile/Erik-Hartigh/publication/288583566_Measuring_the_health_of_a_business_ecosystem/links/57b6ef7a08ae2fc031fd87d3/Measuring-the-health-of-a-business-ecosystem.pdf) 2006, Erik den Hartigh, Michiel Tol and Wouter Visscher
* [Strategy as Ecology](https://hbr.org/2004/03/strategy-as-ecology) 2004, Marco Iansiti and Roy Levien
* [Predators and prey: a new ecology of competition ](http://blogs.harvard.edu/jim/files/2010/04/Predators-and-Prey.pdf) 1993, James F. Moore

# Contributors 

* Matt Germonprez
* Sean Goggins
* Kevin Lumbard
* Liang Wang
* Jun Zhong
* Chenqi Shan
* Yehui Wang




