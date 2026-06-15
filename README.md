IOC Scanner

A Python-based Indicator of Compromise (IOC) Scanner designed to detect suspicious IP addresses and domains within log files and text-based data sources. The tool compares observed indicators against a predefined threat intelligence list and generates alerts when matches are found.

Project Overview

Indicators of Compromise (IOCs) are pieces of information that may indicate malicious activity within a system or network. Security Operations Center (SOC) analysts and threat hunters use IOC matching to identify potentially malicious communications, compromised hosts, and suspicious activity.

This project was developed to gain practical experience with threat detection, threat intelligence concepts, log analysis, and Python automation.

Features
 Detects suspicious IP addresses
 Detects suspicious domains
 Scans log files for indicators of compromise
 Generates security alerts for detected IOCs
 Supports threat intelligence-based detection workflows
Technologies Used
Python
Threat Intelligence Concepts
Log Analysis
Git
GitHub
Security Use Cases
Threat Hunting
IOC Detection
Security Monitoring
Log Analysis
Incident Investigation
Threat Intelligence Validation
Project Structure
ioc-scanner/

├── ioc_scanner.py
├── ioc_list.txt
├── sample_log.txt
├── README.md
└── screenshots/
Sample Output
[ALERT] Suspicious IP detected: 185.220.101.45

[ALERT] Suspicious Domain detected: malicious-domain.com
Future Improvements
IOC feed import support
Hash detection
URL detection
CSV reporting
Threat severity scoring
Real-time log monitoring
Learning Objectives

This project was built to strengthen understanding of:

Threat Intelligence
Indicator of Compromise (IOC) Analysis
Security Monitoring
Threat Hunting
Log Analysis
Python Automation
Author

Gideon Nwachukwu (Paxvirs)