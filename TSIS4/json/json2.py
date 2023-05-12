import json

x = open('sample-data.json').read()

y = json.loads(x)

print(
    "Interface Status \n================================================================================\nDN                                                 Description           Speed    MTU  \n-------------------------------------------------- --------------------  ------  ------"
)

imdata = y["imdata"]
for i in imdata:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    desc = i["l1PhysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]["fecMode"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    print("{0:50} {1:21} {2:8} {3:6}".format(dn, desc, speed, mtu))

