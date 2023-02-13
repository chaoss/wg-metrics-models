# Collaboration Development Index

Keyword Tag: Metrics Model
Context Tags: Community, Software, Ecosystem, Contributor

# Why It Matters
Open source projects, as a typical manifestation of human group intelligence, the ability to establish collaborative development management is a key element contributing to the success of the project. And code, as the final output of a project, is the essence of the entire community's contribution. So we evaluate how well the development process is managed and how well the community does collaborative development around a series of indirect metrics related to code contribution.

# User Stories
As a community manager, I want to observe the trend of software quality with version changes and what the root cause (good or bad reasons) may be in these changes. 
As an OSPO or a program manager from a company, I want to collaborate with communities, which have capabilities to produce high quality software continuously. This is especially important, when I have multiple projects to choose from. 
As a user, I want to choose high quality software artifacts to meet the requirement. 

# Metrics in the Metrics Model

- [Contributors](https://chaoss.community/metric-contributors/)  
-- Determine how many active change request creators, code reviewers, commit authors there are in the past 90 days.
- Downloads  
-- Determine the number of downloads of software artifacts per week.  
-- Determine the number of hosts downloading software artifacts per week.
- [Code Changes Commits](https://chaoss.community/metric-code-changes-commits/)  
-- Determine the average number of commits per week in the past 90 days.  
-- Percentage of weeks with at least one code commit in the past 90 days.  
-- Percentage of code repositories with at least one code commit in the last 30 days.  
- CI Test  
-- Determine if the most recent (~30) commits contain CI tests  
- Code Commit linked with Change Request  
-- Percentage of new code commits linked with change requests in the last 90 days.  
- Ratio of Issues to Change Requests  
-- Percentage of new change requests linked with issues in the last 90 days.  
- [Change Request Reviews](https://chaoss.community/metric-change-request-reviews/)  
-- Percentage of recent 90-day code commits with at least one reviewer who is not the change request creator)  
-- Percentage of individuals merging change requests and individuals who authored change requests who are not the same person in the last 90 days.  
- [Technical Fork](https://chaoss.community/metric-technical-fork/)  
-- Determine the average number of fork counts per week in the past 90 days.  
- [Code Changes Lines](https://chaoss.community/metric-code-changes-lines/)  
-- Determine the average number of lines touched (lines added plus lines removed) per week in the past 90 days.  

# Data Insights

## Background of the Investigated Context
We chose two communities to evaluate the effectiveness of the code quality guarantee metric model. We anonymized these two communities, so as to not pass judgment on which community is better. In this example, we simply turn results into insights and provide a comparison of two communities to better understand the metric model. Both communities are open source machine learning frameworks. They all have many repositories in their project, but in our example we selected one repository for each community, which is the most critical component to make up the ML framework. We marked Community A purple and Community B blue. Both communities open source their projects almost at the same time, at the latest boom stage of machine learning. 

## Insights Drawn from the Metrics Model
We counted metric model values every week, the value range is between 0-1. At the beginning, the score of Community A is much higher than Community B. Community B's score has been steadily increasing upwards, until Sept 2020, when its score exceeds Community A. At that time, Community A's score starts to decline. In order to get deeper insights, we checked the result of each metric.

![Metrics Model Insights](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/collaboration-development-index/images/1.jpg)

## Metric Specific Insights Drawn from the Metrics Model

### Contributor Count
In this metric, we put attention on the group of contributors that closed within change request and code commit efforts. Contributor count was further explored through filters on the [activity_dates_and_times](https://chaoss.community/?p=3444) metric. 

Community A (purple) attracts many change request contributors at the beginning , the count is much more than Community B (blue). But both communities’ change request contributors count increased until around Sept 2020. From that time, active change request contributor count declined in Community A. Perhaps people left Community A and joined Community B. 

![Metrics Model Contributor Count](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/collaboration-development-index/images/2.jpg)

## Commit Frequency 
If we check the graphs of contributor count and commit frequency together, we find there are strong correlations. Commit frequency can be determined using an aggregation of the [code_changes_commits](https://chaoss.community/?p=4707) metric.

![Metrics Model Commit Frequency](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/collaboration-development-index/images/3.jpg)

### Is Maintained 
In this metric we explored the percentage of weeks with at least one code commit in the past 90 days. Because the repositories we choose are the key component, we find both repositories keep a high maintenance frequency. 

![Metrics Model Is Maintained](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/collaboration-development-index/images/4.jpg)

### Commit and Change Request Linked Ratio

In this metric, we would notice that many code commits are merged through change requests, or force push to the main branch. Over the last three years, Community B has significantly increased the transparency of its code contributions, as this ratio was always above 40%.

![Metrics Model Commit and Change Request Linked Ratio](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/collaboration-development-index/images/5.jpg)

### Change Request and Issues Linked

In this metric, we introduce a new community C as the third reference, which is a young machine learning open source community, marked with red. We could find that both Community A and Community B did not have a regular rule about change requests and issues being linked in the contribution guideline. 

![Metrics Model Change Request and Issues Linked](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/collaboration-development-index/images/6.jpg)

### Code Review Ratio 

If we check the graphs of change requests and issues linked with code review ratio, we could find their strong correlations. But does it really mean that Community A and Community B do not pay any attention to code review? We should also consider that both Community A and Community B are initialized by two companies that make most of the code contributions. So before they create change requests on the public code host platform, internal code reviews are likely to be completed. 

![Metrics Model Code Review Ratio](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/collaboration-development-index/images/7.jpg)

### Code Merge Ratio 
There are not so many differences between Community A and Community B, as both of them take this metric seriously. This may indicate the importance of this metric as related to code quality guarantee. 

![Metrics Model Code Merge Ratio](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/collaboration-development-index/images/8.jpg)

### Lines of Code Frequency
The number of lines of source code correlates strongly with workload, but it correlates less with value created. Also, what form of code can be counted in lines of code is uncertain as we do not focus on the code form, but only use it to describe the workload, and its weight is low in the overall metric model.

![Metrics Model Lines of Code Frequency](https://github.com/chaoss/wg-metrics-models/blob/main/metrics-model-libs/collaboration-development-index/images/9.jpg)

# References
- https://github.com/ossf/scorecard/blob/main/docs/checks.md 

# Contributors
- Yehui Wang
- Liang Wang
- Chenqi Shan
- Jun Zhong
- Matt Germonprez
- Sean Goggins
- Vinod Ahuja
