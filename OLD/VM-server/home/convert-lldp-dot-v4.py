#!/usr/bin/python

#import pandas as pd
#import re

print ("run ansible playbook to get json datafile: sudo ansible-playbook vrp-lldp-v4.yml")

my_datafile = raw_input("Please enter filename with raw LLDP info: ")

print ("LLDP file: %s\n" % my_datafile)

#my_data=pd.read_table(my_datafile, sep=';')
#my_data=pd.read_table('sysconfig_table.csv', sep=';')
#my_data=pd.read_table('c:/Python27/Hafslund/sysconfig_table.csv', sep=';')

#print my_data
outputfile = my_datafile +'.dot'

fw = open(outputfile,'w')

section = "false"
collectinfo = "false"
lldplink = "strict graph {"
print lldplink
fw.write("%s\n" %lldplink)
lldplink = "rankdir=LR;"
print lldplink

#create size for print A3:
fw.write("%s\n" %lldplink)
lldplink ='ratio="fill";'
fw.write("%s\n" %lldplink)
lldplink ='size="11.7,16.5!";'
fw.write("%s\n" %lldplink)
lldplink ="margin=0;"
fw.write("%s\n" %lldplink)


# Open a file
fo = open(my_datafile, "r+")
#print(fo.readlines())
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

'''
   nosysname = remotesysname[0]
   if "_" in nosysname:
      x = "x"
   else:
'''
       #        lldplink = localsysname + " -- " + remotesysname + " [fontsize=8, headlabel: """ + localinterface + """ ,taillabel: """ + remoteinterface + "];"

'''

     row = row.strip()
     row = row.strip('"""')
     row = row.strip()
#     print row
#     remotesysname = row[10:30]
#     lldpneigbor = row.split(" ")
     lldpneigbor = row.split()
#     print lldpneigbor
#     print lldpneigbor[1]
#     print lldpneigbor[0]
#     print lldpneigbor[2]
     remotesysname = lldpneigbor[1].replace("-","_")
     localinterface = str(lldpneigbor[0])
     remoteinterface = str(lldpneigbor[2])
     remotesysname = remotesysname.strip()
#     print localsysname
#     print remotesysname
     nosysname = remotesysname[0]
     if "_" in nosysname:
        x = "x"
     else:
#        lldplink = localsysname + " -- " + remotesysname + " [fontsize=8, headlabel: """ + localinterface + """ ,taillabel: """ + remoteinterface + "];"
        lldplink = localsysname + ' -- ' + remotesysname + ' [fontsize=8, headlabel=' + '"' + localinterface + '"' + ' ,taillabel=' + '"' + remoteinterface + '"' + '];'

#        lldplink = localsysname + " -- " + remotesysname + ";" + "[localinterface: " + localinterface + "remoteinterface: " + remoteinterface + ["];"]
        print lldplink
        fw.write("%s\n" %lldplink)
#	       print ("\n")

'''
str = fo.read(50);
#print "Read String is : ", str
# Close opend file
fo.close()
lldplink = "}"
print lldplink
fw.write("%s\n" %lldplink)
fw.close()
print ("DOT fil for Graphviz:   %s  " % outputfile)
print ("Run command - dot -Tpng %s >%s.png - on Graphviz computer " % (outputfile, outputfile))
