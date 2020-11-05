# Target-Breach-Case-Study
A Case Study of the 2013 Target cybersecurity breach

**Code Fellows 401 Mid-term Project**</br>
November 6, 2020

## Abstract
 
On December 19, 2013, Target Corporation issued a press release admitting the company was “aware of unauthorized access to payment card data that may have impacted certain guests making credit and debit card purchases in its U.S. stores,” acknowledging 40 million credit and debit card records had been stolen. One month later, the company confirmed that an additional 70 million data records had been stolen. Forensic investigation led researchers to conclude there were multiple facts that led to this data loss: third-party vendors were subject to phishing attacks, attackers were able to exploit broken access control of default accounts, network segregation was weak, point of sale systems were vulnerable to memory scraping malware, and detection strategies either failed or were dismissed by Target executives. 

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

## Resources & assets
 
**Applications**</br>
Oracle VirtualBox
	Kali Linux 20.20 virtual machine - attack mechanism
	Windows 7 - target of evaluation
Microsoft Threat Modeling Tool
GitHub
Google Docs & Slides
 
**Tools & coding languages**</br>
Metasploit
NMap
Fernet key encryption
Windows Defender Firewall
Microsoft Security Essentials
Python 2.7.18
Python 3.8.4
Windows Command Line
 
**Additional resources**</br>
MITRE ATT&CK framework
Atomic Red Team
Lockheed Martin Cyber Kill Chain
NIST Risk Management Framework

## Team Members

### Bubacarr Darboe
Bubacarr is a Semiconductor Engineering Technician with an entrepreneurial mindset and a degree in Technology Management. A current Cybersecurity Engineering student at Code Fellows.

[Bubacarr's GitHub profile](https://github.com/bdarboe)</br>
[Bubacarr's LinkedIn profile](https://www.linkedin.com/in/bdarboe/)

### Courtney Hans
Courtney is an operations and cybersecurity professional with deep history in the experiential product space. She has a knack for understanding customer pain points and delivering creative, effective solutions. She integrates security operations with business needs, bridging gaps in communication between the two, and shepherding initiatives from ideation to implementation. In short, Courtney simplifies complexity to drive decisions, action, and results.

[Courtney's GitHub profile](https://github.com/CourtHans)</br>
[Courtney's LinkedIn profile](https://www.linkedin.com/in/courtney-hans/)

### Domonic Moore
Domonic is a Tech Enthusiast and Problem Solver with a background in Business, Product Design and Cybersecurity. He has a history of balancing business goals with user needs. 

[Domonic's GitHub profile](https://github.com/sneakerheadz1)</br>
[Domonic's LinkedIn profile](https://www.linkedin.com/in/dommo-12/)

