'''
Write a program that creates  the following output by parsing this [JSON response](https://raw.githubusercontent.com/chrhobbs/exercise-python-json-parsing/master/exer1-interface-data.json):
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
'''
import json

# Display static content
print(
'''
Interface Status                                                                                                                               ========================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
'''                                                
)
# open up the file 
# Display requested data from JSON file
with open('exer1-interface-data.json', 'r') as f:
    json_data = json.load(f)
    items_list = json_data["imdata"]
    for item in items_list:
        item_details = item['l1PhysIf']['attributes']
        # print(
        #     f'{item_details["dn"]}         {item_details["descr"]} {item_details["speed"]}   {item_details["mtu"]}')
        print("%-45s %20s %15s %15s" %
              (item_details["dn"], item_details["descr"], item_details["speed"], item_details["mtu"]))





