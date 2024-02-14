# OSS Project Viability Starter

## Why It Matters

Project Viability is an aggregate measurement of four categories: Compliance + Security, Governance, Community Engagement, and Strategy. Viability is relevant through the lens of any prospective user of a given project; specifically to provide an understanding of how viable a particular project may be for themselves. 

The aggregate of four metrics, containing 24 distinct metrics in itself, may be more effort than can be reasonably expected on experiments to measure viability for interested products. Given that many successful projects start with experiments, we've created this starter model 

## User Stories

* As a developer who is evaluating a new open source project to use as a dependency, I want to understand the project's future roadmap, so that I can determine if its goals and direction match my needs.
* As a developer, I want to understand if a project has a thriving open source community, so that I have a higher degree of confidence in its viability.
* As a developer, I want to:
    * Understand if a dependency is viable.
    * Investigate how well the project’s dependencies are kept up to date.
* As a project manager, I want to use projects well understood and vetted by a developer community, so that I can mitigate the business risk of adopting unsupported dependencies.
* As a manager of a project using open source, I want to:
    * Understand the risk associated with using a project.
    * Determine if a project aligns with long term technical goals of myself/my organization.
* As a stakeholder of a project, I want to understand my opportunity to contribute to project strategy

## Metrics in the Metrics Model

* [Bus Factor](https://chaoss.community/?p=3944)
* [Elephant Factor](https://chaoss.community/?p=3940)
* [Change Requests](https://chaoss.community/?p=3610)
* [Change Request Closure Ratio](https://chaoss.community/?p=4834)
* [Libyears](https://chaoss.community/?p=3976)
* [OSI Approved Licenses](https://chaoss.community/?p=3962)

## Data Insights

## Background of the Investigated Context

In a highly regulated industry, companies like Verizon have interest in ensuring that their dependencies are well understood and within their licensing boundaries for use across a diverse product range. Our OSPO was particularly interested in determining how “viable” a project is for different product lines that Verizon offers, from web applications to products that are shipped to a home and maintained from afar for years on end.

We took the larger, comprehensive model to capture Viability in a product, and distilled some of the most intuitive and important metrics to this starter model. It collects at least one metric from each pillar:
* Community
* Compliance/Security
* Governance
* Strategy

This should provide a simpler basis to experiment with Viability and prove value in organizations curious about the framework for scrutinizing their open source dependencies.

## Insights Drawn from Metrics Model

Context before insights: “Viability” is a term that will have different thresholds for risk tolerances across organizations and industries. The Compliance and Security that does not suit a telecommunications company may be suitable for a startup emerging into a new space with limited resources and libraries that address their problems. 

Intended use of this metrics model is to feed into an overall viability determination. Every company, like with risk tolerance, will have different degrees of “viable” based on how the software is ultimately applied in a product/service.



* [Bus Factor](https://chaoss.community/?p=3944)
    * An low score on bus factor may indicate that a project is not durably maintained.. Smaller projects/organizations may feel more comfortable with a bus factor of 2, while larger organizations would expect bus factors to be much higher before they consider projects to be viable.
* [Elephant Factor](https://chaoss.community/?p=3940)
    * Like bus factor, but with some extra flavor. Certain organizations may determine that competing organizations have too much influence for them to consider a project viable. If a project is almost completely influenced by one’s competitor, you may consider using that project would introduce a high degree of business risk.
* [Change Requests](https://chaoss.community/?p=3610)
    * Projects with very low count of change requests are unlikely to be keeping up with security updates – or with trends for development in their ecosystem. Change requests with high spikes of activity might also indicate that a project doesn’t provide sufficient checks to avoid unnecessary revisions/toil around the same feature.
* [Change Request Closure Ratio](https://chaoss.community/?p=4834)
    * This metrics allows us to compare the trend of new requests to their rate of closure. It gives us an idea of how well the project is maintained – or if more maintainers might be needed to keep up with demand for new features. The second point is why this is a cross between “Governance” and “Community”.
* [Libyears](https://chaoss.community/?p=3976)
    * Per the objectives of libryear, “assist in the identification of dependencies that have a  higher probability of posing stability, security, and vulnerability risks to a project. A long-obsolete component is more likely to have publicly-known vulnerabilities”.
* [OSI Approved Licenses](https://chaoss.community/?p=3962)
    * Licenses that are found are incorporated in the OSI approved licenses framework. A good proxy for usable licenses within an organization.


## Contributors

- Gary White

**To reference this metric in software or publications please use this stable URL: https://chaoss.community/?p=5417**