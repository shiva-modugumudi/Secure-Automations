# Secure Automations

An evolving portfolio of SOC automation projects integrating Python, agentic AI, APIs, and security tools to reduce repetitive manual work, accelerate investigations, and improve analyst efficiency.

## About

Created by [Siva Modugumudi](https://github.com/shiva-modugumudi), a security professional with experience in SOC operations, incident response, threat hunting, and cloud security.

This portfolio grows from foundational scripts into integrated security workflows. Each project starts with a recurring analyst task and documents how automation can help. Technologies are chosen to fit the problem as the portfolio develops.

## Focus areas

- Alert enrichment and investigation support
- Log processing and event correlation
- Threat intelligence integration
- Reporting and case documentation
- Security tool and API integrations
- Agentic AI workflows with analyst review

These are areas to explore, not claims of completed implementations.

## Projects

| Project | Purpose | Status |
| --- | --- | --- |
| [IP Triage Helper](projects/ip-triage-helper/) | Validate IPv4 and IPv6 addresses and report global address classification | Working foundational project |

Each automation has its own folder under [projects](projects/README.md), containing code and usage documentation. New automations will be added to this index as the portfolio grows.

## Repository guide

| Location | Purpose |
| --- | --- |
| [projects](projects/README.md) | SOC automation implementations and their documentation |
| [Project documentation guide](docs/project-guide.md) | Consistent structure for documenting each project |

## How projects are developed

- Identify the manual task and the analyst decision it supports.
- Define inputs, expected outputs, and success criteria.
- Build a small working version using sample data.
- Validate normal inputs, invalid inputs, and failure conditions.
- Document setup, examples, limitations, and results.
- Measure time saved before reporting efficiency gains.

## Operating principles

Use synthetic or sanitized examples. Keep credentials and confidential incident data out of the repository. Document external API requirements and data sent to services. Workflows that change security controls should include appropriate authorization, review, and audit records. Treat AI outputs as investigation assistance requiring validation.
