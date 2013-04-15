import xml.dom.minidom
import codecs

file = open ("Provinces.xml")  
text = file.read ()  
file.close ()

doc = xml.dom.minidom.parseString (text)

province = {}
city = {}
pids = []
cids = {}
for node in doc.getElementsByTagName("Province"):
    pid = node.getAttribute("ID")
    province[pid] = node.getAttribute("ProvinceName")
    city[pid] = {}
    pids.append (pid)
    cids[pid] = []
    
file = open ("Cities.xml")  
text = file.read ()  
file.close ()

doc = xml.dom.minidom.parseString (text)

for node in doc.getElementsByTagName("City"):
    pid = node.getAttribute("PID")
    cid = node.getAttribute("ID")
    city[pid][cid] = node.getAttribute("CityName")
    cids[pid].append (cid)

# Generate JS output
output = "var cities = new Array ();\n"
output += "var city = null;\n";

for pid in pids:
    output += "city = new Array ();\n"
    output += "cities[\"" + province[pid] + "\"] = city;\n"

    for cid in cids[pid]:
        output += "city.push (\"" + city[pid][cid] + "\");\n"

file = codecs.open ("output.js", "w", "utf-8")  
file.write (output)  
file.close ()
