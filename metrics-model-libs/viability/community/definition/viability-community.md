# OSS Project Viability: Community

## Why It Matters

Project Viability is an aggregate measurement of four categories: Compliance + Security, Governance, Community Engagement, and Strategy. Prospective users care deeply about viability - it's how they decide whether to use a project. . A key aspect of viability is community activity and adoption, because without an active community, an open source project is not likely to continue to evolve and grow. 
This metric is to measure community around a project.. Specifically, we will focus on adoption, relevance, and engagement as key dimensions of community for a project. The guiding hypothesis is that an active community surrounding a project is more likely to drive better performance, vulnerability management, and feature-completeness to ease development downstream.

## User Stories

* As a developer, I want to understand if a project has a thriving open source community, so that I have a higher degree of confidence in its viability. .
* As a project manager, I want to use projects well understood and vetted by a developer community, so that I can mitigate the business risk of adopting unsupported dependencies.

## Metrics in the Metrics Model

* [Clones](https://chaoss.community/?p=3429)
* [Forks](https://chaoss.community/?p=3431)
* [Types of Contributions](https://chaoss.community/?p=3432)
* [Change Requests](https://chaoss.community/?p=3610)
* [Committers](https://chaoss.community/?p=3945)
* [Change Request Closure Ratio](https://chaoss.community/?p=4834)
* [Project Popularity](https://chaoss.community/?p=3573)
* [Libyears](https://chaoss.community/?p=3976)

## Data Insights

## Background of the Investigated Context

Companies in highly regulated industries like Verizon have interest in ensuring that their dependencies are well-understood and within their licensing boundaries for use across a diverse product range. Our OSPO was particularly interested in determining how “viable” a project is for different product lines that Verizon offers, from web applications to products that are shipped to a home and maintained from afar for years on end.

We broke apart the larger context of “viability” across the existing CHAOSS metrics portfolio, and created buckets for each relevant space, reflected through the lens of OSPO’s concerns in the organization. 

This model, Community, reflects how well adopted and engaged a project is in a community of open source developers. This is a contrast to Governance, where we focus on the maintainer effort, because this focuseson the community / developer / user level of effort and adoption.

### Insights Drawn from Metrics Model

Context before insights: “Viability” is a term that will have different thresholds for risk tolerances across organizations and industries. Viability scores for Compliance and Security that do not suit a telecommunications company may be suitable for a startup emerging into a new space with limited resources and libraries that address their problems. 

This metrics model is intended to  feed into an overall viability determination. Every company, as with risk tolerance, will have different thresholds of “viable” based on how the software is ultimately applied to the end users.

Community metrics give an understanding of the adoption a particular project has achieved in a community, with some interest in how well the project is maintained to foster that community. Most governance is stuck in Governance, but there is reasonable overlap.



* [Clones](https://chaoss.community/?p=3429)
    * Clones are one of the only indicators we can get to see how many times the project has been yanked from the internet to be “played with”, whether that be in a POC, or to fix changes, etc. This is a good “tinkering” metric to understand how much a community around a project actually interacts with code of the project.
* [Forks](https://chaoss.community/?p=3431)
    * Contributions to most projects are done through forks. Forks could therefore indicate how many contributions are attempted, how frequently. They may also indicate how many folks use the project to learn by playing with code, or how many projects have been directly inspired from the source code of a project. All these indicators would suggest a strong/curious community.
* [Types of Contributions](https://chaoss.community/?p=3432)
    * While code contributions are the most typical, contributions are diverse. Strategy meetings, issues, event coordination, written articles, presentations, etc. Likewise, if contributions are coming in with one type only – maybe only requests with no code contributions – it could indicate an abandoned project. We will use this to further investigate a project's viability and specific ratios may create obvious patterns or raise questions.
* [Change Requests](https://chaoss.community/?p=3610)
    * Projects with very low count of change requests are unlikely to be keeping up with security updates – or with trends for development in their ecosystem. Change requests with high spikes of activity might also indicate that a project doesn’t provide sufficient checks to avoid unnecessary revisions/toil around the same feature.
* [Committers](https://chaoss.community/?p=3945)
    * “Committers” as a metric itself can be viewed in a useless way. Particularly, if we say “no projects under x committers is viable” – because the two are not related. Rather, we care about _committer trends_. I think it’s reasonable to expect that a project which has shed 90% of its committers in a three month period is “dying”, for example. The inverse could indicate a growing or stable project gaining popularity around a particular technology trend. This metric will be important to inform viability for many reasons – so it is a strong indicator of viability.
* [Change Request Closure Ratio](https://chaoss.community/?p=4834)
    * This metrics allows us to compare the trend of new requests to their rate of closure. It gives us an idea of how well the project is maintained – or if more maintainers might be needed to keep up with demand for new features. The second point is why this is a cross between “Governance” and “Community”.
* [Project Popularity](https://chaoss.community/?p=3573)
    * Popularity of a project will increase its reach and ability to access a community. It’s important to consider popularity to have a relatively appropriate understanding of viability.
* [Libyears](https://chaoss.community/kb/metric-libyears/)
    * This is a useful number to determine the overall risk profile of the project, as older code and older versions of dependencies are more likely to pose a risk to the organization. It’s worth noting that this is a shared metric with Governance, as the libyears are a shared responsibility between the dependencies themselves being updated, and that the project uses updated dependency versions.

### Contributors

- Gary White
- Eric Sorenson
- Matt Germonprez
