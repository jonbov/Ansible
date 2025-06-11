
#!/usr/bin/python

#import pandas as pd
#import re

print ("run ansible playbook to get json datafile: sudo ansible-playbook vrp-lldp-v4.yml")

#my_datafile = raw_input("Please enter filename with raw LLDP info: ")

my_datafile = "/etc/ansible/LLDP-to-Graph/results/LLDP-to-Graph.json"

print ("LLDP file: %s\n" % my_datafile)

#my_data=pd.read_table(my_datafile, sep=';')
#my_data=pd.read_table('sysconfig_table.csv', sep=';')
#my_data=pd.read_table('c:/Python27/Hafslund/sysconfig_table.csv', sep=';')

#print my_data
outputfile = my_datafile +'-nodes.csv'

fw = open(outputfile,'w')


# Open a file
fo = open(my_datafile, "r+")
fw.write("System names discovered:\n")

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
     localsysname = localsysname.replace(".","_")
     tempsysname = localsysname.upper()
     fw.write("%s;" %tempsysname)

   if ("Vlanif" in row and section == "true"):
     temp = row.split()
     ip = temp[1]
     fw.write("%s;\n" %ip)


fo.close()
fw.write(" \n")
fw.close()

