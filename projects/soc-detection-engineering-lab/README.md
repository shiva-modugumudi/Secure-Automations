# SOC Detection Engineering Lab

## SIEM Use Cases & Investigation Playbooks

**Status: Planned — no detection rules or validated lab results have been implemented yet.**

A practical project for developing, testing, and documenting SOC detection use cases, from suspicious activity in logs to an analyst investigation and response recommendation. Designed for students learning SOC analysis and reviewers assessing detection engineering skills.

## Goal

Build a portfolio of explainable detections with sample evidence, reproducible validation, false-positive analysis, and investigation playbooks. Automation will support repeatable log analysis and rule validation as the project develops.

## Planned starter use cases

- Repeated failed logins followed by a successful login.
- Suspicious PowerShell execution.
- Unexpected privileged account creation or group membership changes.
- AWS security group changes allowing broad inbound access.
- Potential data exfiltration based on unusual outbound transfer patterns.

These are candidate scenarios; thresholds, log requirements, and platform selection will be defined per use case.

## What each use case will include

1. Scenario, security risk, and detection objective.
2. Required log sources, fields, and collection prerequisites.
3. Detection logic and a clearly identified query language or rule format.
4. Relevant MITRE ATT&CK mapping with a rationale.
5. Synthetic or sanitized sample events and expected alerts.
6. Positive and negative validation cases, actual results, and limitations.
7. False positives, tuning guidance, and known detection gaps.
8. Investigation steps, evidence to collect, and escalation criteria.
9. Suggested containment or remediation requiring appropriate analyst authorization.

## Initial scope

Start with one authentication use case and one selected SIEM. Expand to additional scenarios and formats such as Splunk SPL, Microsoft Sentinel KQL, or Sigma after validation. Platform-specific queries will be labelled and tested separately; they are not interchangeable.

## Completion criteria for the first use case

- Log prerequisites and detection assumptions are documented.
- Detection triggers on the intended synthetic positive sample.
- Benign negative samples are tested and results recorded.
- A student can reproduce the lab and follow the investigation playbook.
- Evidence, limitations, and tuning notes are committed alongside the rule.

## Current deliverables

This README defines the project plan only. Rules, sample logs, screenshots, playbooks, and test results will be added as they are built. No production readiness, detection coverage, or performance gains are claimed.
