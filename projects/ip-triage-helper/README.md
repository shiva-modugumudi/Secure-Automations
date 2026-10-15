# IP Triage Helper

[Portfolio home](../../README.md) · [All automations](../README.md)

A beginner Python SOC automation project that validates an IP address and reports whether Python classifies it as globally reachable.

## Features

- Accepts an IPv4 or IPv6 address from the terminal.
- Removes leading and trailing whitespace.
- Validates the address using Python’s built-in `ipaddress` module.
- Displays a clear message for invalid input using `try` / `except ValueError`.
- Reports `Globally routable IP` or `Not globally routable IP` using `is_global`.

## Download only this script

Open [ip_triage_helper.py](ip_triage_helper.py), then select **Download raw file**. Save it in a folder and open a terminal there.

On macOS or Linux, run `python3 ip_triage_helper.py`. On Windows with the Python launcher installed, run `py ip_triage_helper.py`.

## Run

Requires Python 3. No additional packages are needed.

```bash
git clone https://github.com/shiva-modugumudi/Secure-Automations.git
cd Secure-Automations/projects/ip-triage-helper
python3 ip_triage_helper.py
```

Enter one IP address when prompted.

## Examples

| Input | Result |
| --- | --- |
| `8.8.8.8` | Globally routable IP |
| `192.168.0.11` | Not globally routable IP |
| `10.0.0.0` | Not globally routable IP |
| `8.8.8.` | Please enter a valid IP address |

## What this checks

This is a local address classification check. It does not contact the address, test actual connectivity, or check threat reputation. Global classification does not mean an address is safe. Non-global addresses include private and special-purpose addresses; they are not all private. Classification details can vary with Python versions.

The program checks one input and then exits. Run it again to check another address.

## Concepts practiced

Imports, variables, user input, strings, conditionals, indentation, IP address objects, and exception handling.
