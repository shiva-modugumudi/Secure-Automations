# IP Threat Intelligence Enrichment

**Status: Planned — implementation has not started.**

## Goal

Reduce repeated manual IP lookups by collecting results from multiple threat intelligence sources and presenting a clear investigation summary.

## Initial scope

- Accept an IP address and validate its format.
- Classify the address locally and skip external reputation lookups for private or special-purpose addresses.
- Integrate VirusTotal and AbuseIPDB, subject to available API access.
- Summarize each source separately, including available timestamps and lookup time.
- Show unavailable sources, authentication errors, timeouts, and rate limits explicitly.

## Planned workflow

IP input → local validation and classification → supported threat intelligence API lookups → source-by-source summary.

## Expected summary

| Source | Information to display when available |
| --- | --- |
| VirusTotal | Malicious, suspicious, harmless, and undetected vendor verdict counts; analysis timestamp |
| AbuseIPDB | Abuse confidence score, report count, and last report timestamp |
| Lookup status | Whether each source responded successfully or why it could not be checked |

Vendor verdict counts and abuse report counts represent different evidence and will not be added together. If nothing is flagged, the summary should say “No malicious indicators found in the checked source results,” rather than declaring the IP safe. Incomplete lookups must remain visible.

## Requirements to confirm during development

API access for each service, account limits, supported address types, dependencies, and environment variable configuration. API keys will be kept outside source code. External lookups send the queried IP address to the selected service.

## Validation plan

Use sample responses first, then authorized live lookups. Check valid IPv4 and IPv6 input, malformed input, private and special-purpose addresses, missing keys, empty results, timeouts, authentication failures, rate limits, and partial source availability.

## Implementation and results

No runnable enrichment code or measured time savings yet. Setup commands and sample output will be added after implementation and validation.
