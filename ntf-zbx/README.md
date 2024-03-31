# ntf_zbx
Zabbix or cmd line  Notification Python tiny project 

## Main Idea 

code like 

from nft_zbx import trap
trap("Message to send") ## Will send tyrasd to zabbix  using `zabbix_sender` or an y other configured tool to send it
'''
if zabbix sender not congurd or not installed - nothing happends
'''