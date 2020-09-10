
#!/usr/bin/python

#import pandas as pd
#import re

import sys


def main(argv):


	print ("run ansible playbook to get json datafile: sudo ansible-playbook vrp-lldp-v4.yml")

	#my_datafile = raw_input("Please enter filename with raw LLDP info: ")

	my_datafile = "/etc/ansible/lldp-to-graph/results/lldp-to-graph.json"

	print ("LLDP file: %s\n" % my_datafile)

	#my_data=pd.read_table(my_datafile, sep=';')
	#my_data=pd.read_table('sysconfig_table.csv', sep=';')
	#my_data=pd.read_table('c:/Python27/Hafslund/sysconfig_table.csv', sep=';')

	#print my_data
	outputfile = my_datafile +'-links.csv'

	fw = open(outputfile,'w')


	collectinfo = "false"

	fw.write("\n\nConnections discovered:\n") 
	fo = open(my_datafile, "r+")
	for row in fo.readlines():
	   intfspeed = 'NULL'
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
		   continue
	   elif ("Port ID" in row and section == "true" and collectinfo == "true"):
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
		   remotesysname = remotesysname.replace(".","_")
		   ulocalsysname = localsysname.upper()
		   uremotesysname = remotesysname.upper()
	   elif ("OperMau" in row and section == "true" and collectinfo == "true"):
		   if ("10000" in row):
	 #     OperMau   :speed(1000)/duplex(Full) 
			  intfspeed = '10G'
		   elif ("1000" in row):
			  intfspeed = '1G'


		   lldplink = ulocalsysname +  ';' + localinterface + ';' + uremotesysname + ';' + remoteinterface + ';'  + intfspeed + ';'

		   fw.write("%s\n" %lldplink)
		   collectinfo = "false"

	
	str = fo.read(50);
	#print "Read String is : ", str
	# Close opend file
	fo.close()
	lldplink = " "
	fw.write("%s\n" %lldplink)
	fw.close()



if __name__ == "__main__":
   main(sys.argv[1:])
