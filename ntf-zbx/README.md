# ntf_zbx
Zabbix or cmd line  Notification tiny project Written in python  

## Main Idea 

Code like 

from nft_zbx import trap
trap("Message to send") ## Will send Trap  to zabbix  using `zabbix_sender` or any other configured tool to send it


    from ntf_zbx.cmdsender import call_action
    res = call_action(item="itemName", text="text to transmit here")
    assert res ==0


##todo: добавить нормальные ָalias для импортов 
