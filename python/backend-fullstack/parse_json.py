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
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
'''
)
# open up the file 
with open('exer1-interface-data.json', 'r') as f:
    data_dict = json.load(f)
    for data in data_dict:
        print(f'{data["dn"]}         {data["descr"]} {data["speed"]}   {data["mut"]}')

# loop and print relevant data



