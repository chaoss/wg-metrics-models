# OSS Project Viability: Compliance + Security

## Why It Matters

Project Viability is an aggregate measurement of four categories: Compliance + Security, Governance, Community Engagement, and Strategy. Viability is relevant through the lens of any prospective user of a given project; specifically to provide an understanding of how viable a particular project may be for themselves.

Compliance and Security is a model that assesses a project’s licensing fit, vulnerability risk, and ability to respond to their maintenance duties. It is important for users to comply with any responsibilities they may hold to an organization, or to the creators of an OSS project, when making use of open source. A prospective user may want to know:

* Licensing information
* Security and vulnerability response time
* What dependencies the project uses (and, consequently, a user may be held to)
* How up-to-date a project’s dependencies are

## User Stories

* As a developer, I want to:
    * Understand if a dependency is viable.
    * Investigate how well the project’s dependencies are kept up to date.
* As a manager of a project using open source, I want to understand the risk associated with using a project.
* As a technologist involved with a project leveraging open source, I want to comply with my organization’s policy using specific open source licenses.

## Metrics in the Metrics Model



* [OpenSSF Best Practices](https://chaoss.community/?p=3939)
* Licensing
    * [License Coverage](https://chaoss.community/?p=3961)
    * [OSI Approved Licenses](https://chaoss.community/?p=3962)
    * [Licenses Declared](https://chaoss.community/?p=3963)
* [Defect Resolution Duration](https://chaoss.community/?p=4727)
* [Libyears](https://chaoss.community/?p=3976)
* [Upstream Code Dependencies](https://chaoss.community/?p=3977)

## Data Insights

## Background of the Investigated Context

In a highly regulated industry, companies like Verizon have interest in ensuring that their dependencies are well understood and within their licensing boundaries for use across a diverse product range. Our OSPO was particularly interested in determining how “viable” a project is for different product lines that Verizon offers, from web applications to products that are shipped to a home and maintained from afar for years on end.

We broke apart the larger context of “viability” across the existing CHAOSS metrics portfolio, and created buckets for each relevant space, reflected through the lens of OSPO’s concerns in the organization. In this bucket, Compliance and Security, we focus on metrics that determine the relative security and compliance of a project.

## Insights Drawn from Metrics Model

Context before insights: “Viability” is a term that will have different thresholds for risk tolerances across organizations and industries. The Compliance and Security that does not suit a telecommunications company may be suitable for a startup emerging into a new space with limited resources and libraries that address their problems. 

Intended use of this metrics model is to feed into an overall viability determination. Every company, like with risk tolerance, will have different degrees of “viable” based on how the software is ultimately applied to the end users. The metrics included inform the compliance and security profile of a given application, likely a make-or-break for adoption to a given project or product.



* [OpenSSF Best Practices](https://chaoss.community/?p=3939)
    * While this is not a requirement for a project to be following best practices, federating with the OpenSSF does provide insight for thoughtful technologists to gauge the stability of open source against the risk tolerance of a project.
* Licensing
    * [License Coverage](https://chaoss.community/?p=3961)
        * Ensures that any unlicensed code can be identified for a package (or investigated, scanners aren’t always perfect)
    * [OSI Approved Licenses](https://chaoss.community/?p=3962)
        * Licenses that are found are incorporated in the OSI approved licenses framework
    * [Licenses Declared](https://chaoss.community/?p=3963)
        * Allows technologists to understand the licenses used in a project (and its dependencies) to avoid licensing issues.
* [Defect Resolution Duration](https://chaoss.community/?p=4727)
    * This gives insight into how responsive the community is to problems reported to their project.
* [Libyears](https://chaoss.community/?p=3976)
    * Per the objectives of libryear, “assist in the identification of dependencies that have a  higher probability of posing stability, security, and vulnerability risks to a project. A long-obsolete component is more likely to have publicly-known vulnerabilities”.
* [Upstream Code Dependencies](https://chaoss.community/?p=3977)
    * Understanding what projects are involved with building a project is important not just to understand their age, but owning organizations and context around projects, as well as any vulnerability and licensing problems that might result downstream (in a project a prospective user is building)

## Validated by (Optional)

## References

## Contributors

Gary White
Eric Sorenson
Matt Germonprez
