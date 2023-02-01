# Community Service and Support

# Why It Matters
Community Service and Support measures the quality of services and support provided by the community as directly perceived by a developer during the contribution process.

# User Stories
- As a community manager, I want to know if my community provides good enough service and support to the contributors, including issue response, infrastructure services and outreach activities. 
- As a new community member, I want to know if I get adequate support from the community.
- As a community software user, I want to know if I can get a quick answer when I have problems. 
- As an OSPO or a program manager, I want to work with a community, and understanding community service and support can improve my ability to better understand such an engagement. 
- As an existing community member, I may want to identify areas where community service and support is lacking in an effort to provide support where needed. 

# Metrics in the Metrics Model

- [Issue Response Time](https://chaoss.community/?p=3631)
Average/Median first comments response (in days) for new issues created in the last 90 days. This excludes bot responses, the creator's own comment, or an action assigned by the issue. If the issue has been unanswered, the first response time is not counted.
- [Issue Age](https://chaoss.community/?p=3629)
Average/Median time (days) that issues have been opened for issues created in the last 90 days. 
- [Issue Resolution Duration](https://chaoss.community/?p=3630)
Average/Median processing time (days) for new issues created in the last 90 days, including issues closed with and without resolution
- Number of Issue Comments
The average number of comments per issue created in the last 90 days
- [Issues Active](https://chaoss.community/?p=3632)
Number of issue updates in the last 90 days.
- CI Build Time
The time it takes for a contribution to build
- [Change Requests Duration](https://chaoss.community/?p=3587)
What is the duration of time between the moment a change request starts and the moment it is accepted or closed?
- Change Request Age
Average/Median processing time (days) for new change requests created in the last 90 days, including closed/accepted change requests and unresolved change requests.
- [Change Request Reviews](TBD)
The average number of review comments per pull request created in the last 90 days
- [Change Requests Declined](https://chaoss.community/?p=3588)
Number of change requests declined in the last 90 days.
- [Change Requests Accepted](https://chaoss.community/?p=3589)
Number of change requests accepted in the last 90 days.
- [Collaboration Platform Activity](https://chaoss.community/?p=3484)
Number of new mail topics created in the last 90 days
- Event Count
The number of online and offline events held in the past 90 days, including conferences, meet-ups

# Data Insights

## Background of the Investigated Context
We chose two communities to evaluate the effectiveness of the community service and support metric model. We anonymized these two communities, so as to not pass judgment on which community is better. In this example, we simply turn results into insights and provide a comparison of two communities to better understand the metric model.

Both communities are open source machine learning frameworks. They both have many repositories in their project, but in our example we select one repository for each community, which is the most critical component to make up the ML framework.  

We mark Community A blue and Community B red. In this example, Community A has been running for over 6 years, Community B 2 years.

## Insights Drawn from the Metrics Model
We counted metric model values every week, the value range is between 0 and1. We can see that Community A‘s score is very stable in general, but with some slight downward trend. If we check metrics that make up this model below, we could find that as this community becomes older, its capability of service and support can not catch up with its growth in time.  

Community B, as a young community, shows fast growth from community service and support perspective, but still there are some gaps compared to Community A. In order to get deeper insights, we needed to check the result of each specific metric.

![Insights from Metric Model](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/community-service-and-support/images/1.jpg)

# Metric Specific Insights Drawn from the Metrics Model

## Updated Issues Count

There are two reasons that promote us to choose updated issues count instead of closed issues. First, issues have many different types, like bugs, feature requirements, users’ questions, and CVEs. Only specific types of issues have to be resolved very quickly, like CVEs. For the rest of the types of issues, we need to communicate with issue creators several times to better understand the detailed information. Also, if it is a requirement, from accept to solve, it is following the release plan, which would take a couple of months. Second, from the issues updated count, we can monitor the activity of issue handling service and support. Issue updates can also include reopening of issues, indicating attentiveness to changes in understanding of issues. Community A’s (blue) updated issue count keeps increasing in the past 6 years, showing a steady state of prosperity. Community B (red) shows fast growth of updated issue count. 

![Metrics Model Updated Issues Count](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/community-service-and-support/images/2.jpg)

## Change Requests Accepted and Change Requests Declined 
The more code contributions, the more change requests that can be  closed (accepted or declined). This indicates that the communities are actively attending to change requests. Both communities have a large number of accepted or declined changed requests in each period. From this point of view, both communities are doing very well.  

![Metrics Model Change Requests Accepted and Change Requests Declined](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/community-service-and-support/images/3.jpg)

## Issue Response Time  
When we observe the issue's first response average time, we found a negative correlation of this metric with updated issue counts. So we put two graphs together to make it more clear. The shorter the response time, the greater the number of issue updates. Many other communities also show such negative correlation between these two metrics. 

![Metrics Model Issue Reponse Time](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/community-service-and-support/images/4.jpg)

## Issue Age
Average/Median processing time (days) for new Issues created in the last 90 days, including closed issues and unresolved issues. In this metric, we focus on the bug/cve related issues that should be solved ASAP. But how to distinguish these kinds of bugs in the different communities is a problem that is unsolved. Usually they are not using the common labels to mark the issue types. So for this metric, we are not going to analyze these two communities for now. 

![Metrics Model Issue Age](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/community-service-and-support/images/5.jpg)

## Change Request Open Time
We are seeking for the change request fast close, including code merged or rejected. Otherwise the longer it takes for a change request to be resolved, the greater the risk that merge-conflict will occur, while other change requests that depend on it will also be stalled. From the graph below, we can see Community B has a big room for improvement in the terms of pr open time. 

![Metrics Model Change Request Open Time](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/community-service-and-support/images/6.jpg)

# Issue Comment Count and Change Request Reviews
We put these two metrics together, that do not take the author into account. They are all related to contributors' involvement.

![Metrics Model Issue Comment Count and Change Request Reviews](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/community-service-and-support/images/7.jpg)

![Metrics Model Issue Comment Count and Change Request Reviews](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/community-service-and-support/images/8.jpg)

# Contributors
- Yehui Wang
- Liang Wang
- Chenqi Shan 
- Shengbao Li
- Matt Germonprez
- Sean Goggins
