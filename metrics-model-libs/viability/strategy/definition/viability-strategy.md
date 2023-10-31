# OSS Project Viability: Strategy

## Why It Matters

Project Viability is an aggregate measurement of four categories: Compliance + Security, Governance, Community Engagement, and Strategy. Viability is relevant through the lens of any prospective user of a given project; specifically to provide an understanding of how viable a particular project may be for themselves. 

The strategy of a project may feel less numerically distinct than many of the metrics laid out in this model of viability. The strategy we think of for viability will be measured by factors we can observe, and by the influence that individuals and organizations might have on a project.

## User Stories

* As a developer who is evaluating a new open source project to use as a dependency, I want to understand the project's future roadmap, so that I can determine if its goals and direction match my needs.
* As a manager of a project using open source, I want to:
    * Understand the risk associated with using a project.
    * Determine if a project aligns with long term technical goals of myself/my organization.
* As a stakeholder of a project, I want to understand my opportunity to contribute to project strategy

## Metrics in the Metrics Model

* [Programming Language Distribution](https://chaoss.community/?p=3430)
* [Bus Factor](https://chaoss.community/?p=3944)
* [Elephant Factor](https://chaoss.community/?p=3940)
* [Organizational Influence](https://chaoss.community/?p=3560)
* [Release Frequency](https://chaoss.community/?p=4765)

## Data Insights

## Background of the Investigated Context

In a highly regulated industry, companies like Verizon have interest in ensuring that their dependencies are well understood and within their licensing boundaries for use across a diverse product range. Our OSPO was particularly interested in determining how “viable” a project is for different product lines that Verizon offers, from web applications to products that are shipped to a home and maintained from afar for years on end.

We broke apart the larger context of “viability” across the existing CHAOSS metrics portfolio, and created buckets for each relevant space, reflected through the lens of OSPO’s concerns in the organization. 

This model, “Strategy”, focuses on our ability to observe the project’s direction and a lineage of influence that individuals or organizations may have on a project. We can discern, from context about our project and intended direction, whether that strategy aligns with ours enough to consider the project viable.

## Insights Drawn from Metrics Model

Context before insights: “Viability” is a term that will have different thresholds for risk tolerances across organizations and industries. The Compliance and Security that does not suit a telecommunications company may be suitable for a startup emerging into a new space with limited resources and libraries that address their problems. 

Intended use of this metrics model is to feed into an overall viability determination. Every company, like with risk tolerance, will have different degrees of “viable” based on how the software is ultimately applied in a product/service.



* [Programming Language Distribution](https://chaoss.community/?p=3430)
    * For some organizations or preferences, languages will become a sticking point. For example: For an individual contributor who knows Go very well, but not Haskell, a project written in Haskell would be less viable than one written in Go. The same follows for organizations and capabilities or common applications across languages. Viability here stems from criteria specific to any evaluator.
* [Bus Factor](https://chaoss.community/?p=3944)
    * An low score on bus factor may indicate that a project is not durably maintained.. Smaller projects/organizations may feel more comfortable with a bus factor of 2, while larger organizations would expect bus factors to be much higher before they consider projects to be viable.
* [Elephant Factor](https://chaoss.community/?p=3940)
    * Like bus factor, but with some extra flavor. Certain organizations may determine that competing organizations have too much influence for them to consider a project viable. If a project is almost completely influenced by one’s competitor, you may consider using that project would introduce a high degree of business risk. .
* [Organizational Influence](https://chaoss.community/?p=3560)
    * Organizational influence rolls close to Elephant factor, but is usually highly specific to just one organization that someone is looking to avoid depending on or providing influence throughout an application portfolio.
* [Release Frequency](https://chaoss.community/?p=4765)
    * While we may not consider release frequency to be within a threshold for a specific project – we do care that a project sticks to a frequency and we can rely on it for security updates / patches within those windows. This is somewhat a proxy for LTS / release strategy.

## Contributors

- Gary White
- Eric Sorenson
- Matt Germonprez
