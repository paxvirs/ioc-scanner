# IOC Scanner

A Python-based Indicator of Compromise (IOC) Scanner designed to identify suspicious IP addresses and domains within log files. The tool compares log data against a predefined IOC list and generates alerts when potential indicators of malicious activity are detected.

## Project Overview

Indicators of Compromise (IOCs) are pieces of forensic data that can signal a potential security incident or system compromise. Security Operations Center (SOC) analysts and threat hunters use IOC matching to identify malicious activity, investigate alerts, and support incident response efforts.

This project was developed to strengthen practical skills in threat detection, log analysis, threat intelligence concepts, and Python automation.

## Features

* Scans log files for Indicators of Compromise (IOCs)
* Detects suspicious IP addresses
* Detects suspicious domains
* Generates alerts for identified indicators
* Lightweight and easy to customize
* Supports basic threat intelligence workflows
* Demonstrates foundational SOC detection concepts

## Technologies Used

* Python
* Threat Intelligence Concepts
* Log Analysis
* Security Monitoring
* Git
* GitHub

## Project Structure

```text
ioc-scanner/
│
├── ioc_scanner.py
├── ioc_list.txt
├── sample_log.txt
├── README.md
└── screenshots/
```

## How It Works

1. Loads a predefined IOC list.
2. Reads a log file containing network or system activity.
3. Compares log entries against known indicators.
4. Generates alerts when matches are found.
5. Reports the total number of detected IOCs.

## Sample IOC List

```text
185.220.101.45
malicious-domain.com
suspicious-site.net
```

## Sample Output

```text
==================================================
IOC SCANNER
==================================================

[ALERT] IOC Detected: 185.220.101.45
[ALERT] IOC Detected: malicious-domain.com

==================================================
Total IOCs Detected: 2
==================================================
```

## Security Use Cases

* Threat Hunting
* Security Monitoring
* IOC Detection
* Log Analysis
* Incident Response Support
* Threat Intelligence Validation

## Future Improvements

* SHA256 hash detection
* URL detection
* CSV reporting
* Threat severity scoring
* External threat intelligence feed integration
* Real-time monitoring capabilities

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Threat Intelligence Fundamentals
* Indicator of Compromise (IOC) Analysis
* Detection Logic Development
* Python Automation
* Security Monitoring Concepts
* SOC Analyst Workflows

## Author

Gideon Nwachukwu (Paxvirs)

