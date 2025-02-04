# Project Engagement

# Why It Matters
Project engagement is a critical component of the sustainability of any open source project. With strong project engagement, communities can rely on community members to attend to and develop the necessary parts of an open source project. 

# User Stories
- A corporate sponsor of an open source project seeks to understand the level of project engagement for key open source projects, helping ensure long-term reliability on the project and its software. 
- A community manager wants to know how community initiatives are working with respect to attracting and retaining community members. 
- Open source foundations care about the projects they host and project engagement is a key indicator of the growth, maturity, or decline of a hosted project. 

# Metrics in the Metrics Model 

- [Change Requests Accepted](https://chaoss.community/?p=3589)
change_request_count: Accepted change requests are those that end with the corresponding changes finally merged into the code base of the project. Accepted change requests can be linked to one or more changes to the source code, those corresponding to the changes proposed and finally merged. 

- [Committers](https://chaoss.community/?p=3945)
D0_count: Contributors who have given the project a star, or are watching or have forked the repository.  
D1_count: Contributors who have created issues, made comments on an issue, or performed a code review.  
D2_count: Contributors who have created a merge request and successfully merged code.  

- [Contributors](https://chaoss.community/?p=3467)
contributor_count: People who contribute to the project in a number of different ways. 

- [Issues Closed](https://chaoss.community/?p=3633)
closed_issues_count: Issues closed are those that changed to state closed during a certain period.

- [Organizational Diversity](https://chaoss.community/?p=3464) 
org_count: Organizational diversity expresses how many different organizations are involved in a project and how involved different organizations are compared to one another.

- [Review Cycle Duration within a Change Request](https://chaoss.community/?p=3445)
code_review_frequency: A change request is based on one or more review cycles. Within a review cycle, one or more reviewers can provide feedback on a proposed contribution. The duration of a review cycle, or the time between each new iteration of the contribution, is the basis of this metric.

# Data Insights 

## Background of the Investigated Context

After two years of growth, the openEuler open source community has grown from 6 special interest groups (hereinafter referred to as SIGs) to 95 SIGs, covering various fields. How to maintain SIGs has become a problem faced by the technical steering committee (TSC). Such questions arise such as how to identify inactive SIGs to contact in a timely manner, how to identify fast-growing SIGs and motivate them in a timely manner, and how to identify problems in the operation of SIGs and provide timely guidance? These are the specific problems that the TSC needs to solve when maintaining SIGs. So, how to measure their activity of the SIGs is particularly important. 

In this regard, the [criticality score algorithm](https://github.com/ossf/criticality_score/blob/main/Quantifying_criticality_algorithm.pdf) can normalize many indicators to get a specific engagement number.



In this algorithm, Si represents the indicator (parameter) value (such as the number of pr in a year, etc.), Ti represents the maximum critical value, and ai represents the weight of the indicator (for example, the weight of the indicator pr is 3). The activity value is between 0 (least active) and 1 (most active). If a project's indicator values ​​are all greater than or equal to the critical value, the final activity value is 1. The formula solves several problems:
Because communities with many repository warehouses are likely to have higher scores than projects with small warehouses, it does not mean that projects with small warehouses have a lower overall score.
More indicators will not impact the overall score
When you only need to calculate the value for one warehouse, you need to check all the index items of all warehouses. Being affected by other warehouse index items will cause variations in a final calculation, because the numbers of other items will also change all the time.

Additionally, the problem of weights is involved in the criticality score algorithm. In order to obtain the weights and weights of each indicator more scientifically, use AHP（Analytic Hierarchy Process）to calculate the value of each weight in the criticality score algorithm. An example is provided here: 

| metric                       | geometric mean | weights     |
| ---------------------------- | -------------- | ----------- |
| A1-pull\_request\_count      | 4.304506871    | 0.209713354 |
| A2-D2\_count                 | 3.750296606    | 0.182712516 |
| A3-maintainer\_count         | 3.167104161    | 0.154299681 |
| A4-code\_review\_frequency   | 2.406366497    | 0.117236934 |
| A5-closed\_issues\_count     | 1.786633707    | 0.087043872 |
| A6-updated\_issues\_countH   | 1.430461257    | 0.069691334 |
| A7-issue\_comment\_frequency | 1.120226918    | 0.054576877 |
| A8-org\_count                | 0.805400017    | 0.039238673 |
| A9-D1\_count                 | 0.584332054    | 0.028468356 |
| A10-D0\_count                | 0.428050368    | 0.020854393 |
| A11-contribute\_count        | 0.317426014    | 0.015464831 |
| A12-meeting\_count           | 0.239445717    | 0.011665671 |
| A13-meeting\_attendee\_count | 0.185418652    | 0.009033501 |



## Insights Drawn from the Metrics Model

The current calculation method of the activity of an openEuler SIG group is as follows: 

Define the indicators required by each SIG group, and then use the AHP analytic hierarchy process algorithm to obtain the weight of each indicator according to the priority of the indicators. For our example, we used: 

| Parameter(Si)             | Weight      | Max threshold | Description                                                                                         |
| ------------------------- | ----------- | ------------- | --------------------------------------------------------------------------------------------------- |
| D0\_count                 | 0.020854393 | 1100          | Count of \[D0\](https://opensource.com/article/21/11/data-open-source-contributors) during the year |
| D1\_count                 | 0.028468356 | 700           | Count of \[D1\](https://opensource.com/article/21/11/data-open-source-contributors) during the year |
| D2\_count                 | 0.182712516 | 340           | Count of \[D2\](https://opensource.com/article/21/11/data-open-source-contributors) during the year |
| org\_count                | 0.039238673 | 15            | Count of distinct organizations that contributors belong to                                         |
| pull\_request\_count      | 0.209713354 | 2500          | Count of PR during the year                                                                         |
| code\_review\_frequency   | 0.117236934 | 4             | Count of code review per PR during the year                                                         |
| updated\_issues\_count    | 0.069691334 | 1000          | number of updated issues in the last year                                                           |
| closed\_issues\_count     | 0.087043872 | 500           | number of closed  issues in the last year                                                           |
| issue\_comment\_frequency | 0.054576877 | 2             | number of meetings in the last year                                                                 |
| contribute\_count         | 0.015464831 | 10000         | Count of contribute during the year                                                                 |
| meeting\_count            | 0.011665671 | 10            | Count of meeting during the year                                                                    |
| meeting\_attendee\_count  | 0.009033501 | 200           | Count of meeting attendee  during the year                                                          |
| maintainer\_count         | 0.154299681 | 10            | Count of maintainer during the year                                                                 | 

Apply the criticality score algorithm in openEuler with the index, combining the weight outputs in the first step to calculate the activity of each SIG according to the following formula ([0,1])


## Metric Specific Insights Drawn from the Metrics Model

![active_ranking](./images/active_ranking.jpg)

Calculated SIG active value ranking

![active_trend](./images/active_trend.jpg)

We can also dynamically view the changes in the value of the activity of each SIG. 


With the identification of SIG activity, open source community TSC committee members can easily know whether a SIG is active, and find those inactive (< 0.4) SIGs for review. Additionally, there can be a continual review where specific problems with inactive SIGs include. Additionally, TSC members can contact the SIG maintainers to help the SIG group resolve their issues. If the problem is still unsolved, inactive SIGs can be integrated with SIGs, etc. 


# References
https://docs.google.com/document/d/1Dxs7OcwzgPZYHMNQkYMduO4ZsawwsxQc3-BD1Jwb8CM/edit
Integrate open source algorithms
Implementation in openEuler

# Contributors 
Jun Zhong
Matt Germonprez
Yehui Wang 
Liang Wang


**To reference this metric in software or publications please use this stable URL: https://chaoss.community/?p=4744**
