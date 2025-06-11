
#!/usr/bin/python

#import pandas as pd
#import re

print ("run ansible playbook to get json datafile: sudo ansible-playbook vrp-lldp-v4.yml")
my_datafile = raw_input("Please enter filename with raw LLDP info: ")
print ("LLDP file: %s\n" % my_datafile)

localsysname = "HEADER"
outputfile = my_datafile +'.dot'
fw = open(outputfile,'w')

section = "false"
collectinfo = "false"
lldplink = "strict graph {"
print lldplink
fw.write("%s\n" %lldplink)

fo = open(my_datafile, "r+")
localsysname = localsysname.strip('"""')
localsysname = localsysname.replace("-","_")
tempsysname = localsysname.lower()
if ("access" in tempsysname):
 localsysname = localsysname + " [shape=box, style=filled, fillcolor=cyan]"
elif ("dist" in tempsysname):
 localsysname = localsysname + " [shape=box, style=filled, fillcolor=indianred]"
elif ("_ap_" or "wlc" in tempsysname):
      localsysname = localsysname + " [shape=circle]"
elif ("core" or "bng" in tempsysname):
      localsysname = localsysname + " [shape=circle, style=filled, fillcolor=indianred]"
print ("%s;\n" %localsysname)
fw.write("%s;\n" %localsysname)
fo.close()


fo = open(my_datafile, "r+")
for row in fo.readlines():
   if "stdout_lines" in row:
      section = "true"
   elif "deprecations" in row:
      section = "false"

   if ("sysname" in row and section == "true"):
     temp = row.split()

     localsysname = temp[1]
     localsysname = localsysname.strip('"""')
     localsysname = localsysname.replace("-","_")
   elif ("has 1 neighbor" in row and section == "true"):
       collectinfo = "true"
#       print row
       temp = row.strip()
       temp = temp.strip(',')
       temp = temp.strip('"""')
       temp = temp.split()
       localinterface = temp[0]
       localinterface = localinterface.replace("GigabitEthernet","G")
#

   if ("Port ID type" in row and section == "true" and collectinfo == "true"):
#continue
       continue
   elif ("Port ID" in row and section == "true" and collectinfo == "true"):
#       print row
       temp = row.strip()
       temp = temp.strip(',')
       temp = temp.strip('"""')
       temp = temp.split()

       remoteinterface = temp[2].replace(":","")
       remoteinterface = remoteinterface.replace("GigabitEthernet","G")

#       print remoteinterface
   elif ("System name" in row and section == "true" and collectinfo == "true"):
#       print row
       temp = row.strip()
       temp = temp.strip(',')
       temp = temp.strip('"""')
       temp = temp.split()
       remotesysname = temp[2].replace("-","_")
       remotesysname = remotesysname.replace(":","")
#       print remotesysname
       lldplink = localsysname + ' -- ' + remotesysname + ' [fontsize=10, headlabel=' + '"' + localinterface + '"' + ' ,taillabel=' + '"' + remoteinterface + '"' + '];'
         #        lldplink = localsysname + " -- " + remotesysname + ";" + "[localinterface: " + localinterface + "remoteinterface: " + remoteinterface + ["];"]
       print lldplink
       fw.write("%s\n" %lldplink)
       collectinfo = "false"



row = row.strip()
row = row.strip('"""')
row = row.strip()
lldpneigbor = row.split()
#remotesysname = lldpneigbor[1].replace("-","_")
localinterface = str(lldpneigbor[0])
remoteinterface = str(lldpneigbor[2])
remotesysname = remotesysname.strip()
nosysname = remotesysname[0]
if "_" in nosysname:
    x = "x"
else:
    lldplink = localsysname + ' -- ' + remotesysname + ' [fontsize=8, headlabel=' + '"' + localinterface + '"' + ' ,taillabel=' + '"' + remoteinterface + '"' + '];'

print lldplink
fw.write("%s\n" %lldplink)

str = fo.read(50);

fo.close()
lldplink = "}"
print lldplink
fw.write("%s\n" %lldplink)
fw.close()

print ("DOT fil for Graphviz:   %s  " % outputfile)
print ("Run command - dot -Tpng %s >%s.png - on Graphviz computer " % (outputfile, outputfile))
