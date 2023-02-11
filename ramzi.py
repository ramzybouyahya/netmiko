from netmiko import ConnectHandler

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.8.2",
    username="cisco",
    password="cisco",
)

output = net_connect.send_command(
    "show ip arp"
)
print(output) 
