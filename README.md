# Target-Breach-Case-Study
**Code Fellows 401 Mid-term Project**

A Case Study of the 2013 Target cybersecurity breach</br>
November 6, 2020

## Abstract
 
On December 19, 2013, Target Corporation issued a press release admitting the company was “aware of unauthorized access to payment card data that may have impacted certain guests making credit and debit card purchases in its U.S. stores,” acknowledging 40 million credit and debit card records had been stolen. One month later, the company confirmed that an additional 70 million data records had been stolen. Forensic investigation led researchers to conclude there were multiple factors that led to this data loss: third-party vendors were subject to phishing attacks, attackers were able to exploit broken access control of default accounts, network segregation was weak, point of sale systems were vulnerable to memory scraping malware, and detection strategies either failed or were dismissed by Target executives. 

## Project Overview

Our project examines the comprehensive failures in Target’s system that allowed attackers to secure and maintain access and exfiltrate sensitive customer data for sale on the black market, as well as how Target may have been able to disrupt the cybersecurity “Kill Chain” at each stage of the attacker’s campaign. The contributive effects of social engineering and human failure will also be examined and addressed.
 
Using the MITRE ATT&CK and Atomic Red Team framework and methodology, our tabletop scenario recreates the attacker’s exploitation of broken access control and brute force attack. Our defensive demonstration illustrates the protection offered by system hardening, data loss prevention techniques, intrusion detection systems, and workforce training.

## Tabletop Scenario

During our tabletop scenario exercise, we demonstrate the following attack as outlined by MITRE ATT&CK:

**[Privilege Escalation:](https://attack.mitre.org/tactics/TA0004/)**</br>
[T1078.001 - Default Accounts](https://attack.mitre.org/techniques/T1078/001/)</br>
“Adversaries may obtain and abuse credentials of a default account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion...”

**[Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)**</br>
[Test Attack:](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.001/T1078.001.md)</br> 
Enable Guest account with administrative privileges and RDP (Remote Desktop Protocol) capability 

## Additional Project Links

[Target Breach Case Study Documents](https://drive.google.com/drive/folders/1iDkCdurUHcoqqfZ4bWqGkqM_dGhb-8o0?usp=sharing) - a Google Drive Project Folder containing the following documents:
* [Target Case Study Presentation Deck](https://docs.google.com/presentation/d/1ddUeIlRmyHvDC4Yo6ujIqOqfGnuaH-SXDM-mqlQY6FI/edit?usp=sharing)
* [Case Study Overview](https://docs.google.com/document/d/1i4Xf-IkzW03aPbHfCXP4FdWRW7RcOQfOF-Z4M5gg0UI/edit?usp=sharing)
* [Security Assesment Report (SAR)](https://docs.google.com/document/d/1UT0hK7sl0kyav4l-UkI7mlNupaiaqgtaX47PqWuma3U/edit?usp=sharing)
* [STRIDE & DREAD Analysis](https://docs.google.com/document/d/1UW-fdUYpUmPAmnP-hOy1da82q9Q9Zuk0yBCHlWqPrh4/edit?usp=sharing)
* [Threat Model Technical Report](https://docs.google.com/document/d/1OpmNvYWt9Pc9Y5VdkGzd91oBXhRmnpZzhZSiZrs0gD8/edit)
* [NIST Risk Management SOP](https://docs.google.com/document/d/17W0rZUiGXvjDZ5rNSKKURSOc8i53MZvwih7Z61E7nAA/edit?usp=sharing)

## Resources & assets
 
**Applications**</br>
Oracle VirtualBox</br>
*Kali Linux 20.20 virtual machine* - attack mechanism</br>
*Windows 7 virtual machine* - target of evaluation</br>
Microsoft Threat Modeling Tool</br>
GitHub</br>
Google Docs & Slides</br>
 
**Tools & coding languages**</br>
Metasploit</br>
NMap</br>
Fernet key encryption</br>
Windows Defender Firewall</br>
Microsoft Security Essentials</br>
Python 2.7.18</br>
Python 3.8.4</br>
Windows Command Line</br>
 
**Additional resources**</br>
MITRE ATT&CK framework</br>
Atomic Red Team</br>
Lockheed Martin Cyber Kill Chain</br>
NIST Risk Management Framework</br>

## Team Members

### Bubacarr Darboe
Bubacarr is a Semiconductor Engineering Technician with an entrepreneurial mindset and a degree in Technology Management. A current Cybersecurity Engineering student at Code Fellows.

[Bubacarr's GitHub profile](https://github.com/bdarboe)</br>
[Bubacarr's LinkedIn profile](https://www.linkedin.com/in/bdarboe/)

### Courtney Hans
Courtney is an operations and cybersecurity professional with deep history in the experiential product space. She has a knack for understanding business and customer pain points and delivering creative, effective solutions. She integrates security operations with business needs, bridging gaps in communication between the two, and shepherding initiatives from ideation to implementation. In short, Courtney simplifies complexity to drive decisions, action, and results.

[Courtney's GitHub profile](https://github.com/CourtHans)</br>
[Courtney's LinkedIn profile](https://www.linkedin.com/in/courtney-hans/)

### Domonic Moore
Domonic is a Tech Enthusiast and Problem Solver with a background in Business, Product Design and Cybersecurity. He has a history of balancing business goals with user needs. 

[Domonic's GitHub profile](https://github.com/sneakerheadz1)</br>
[Domonic's LinkedIn profile](https://www.linkedin.com/in/dommo-12/)

