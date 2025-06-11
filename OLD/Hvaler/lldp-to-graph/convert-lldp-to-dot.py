
#!/usr/bin/python

#import pandas as pd
#import re
import sys
from datetime import datetime

#def main(argv, label):
def main():

#    print ("run ansible playbook to get json datafile: sudo ansible-playbook vrp-lldp-v4.yml")
    make_subgraph =  sys.argv[1]
    dateTimeObj = datetime.now()
    timeStr = dateTimeObj.strftime("%d %b %Y   %H %M %S")
    print('Current Timestamp : ', timeStr)

    label = sys.argv[2] + "   " + timeStr
    print ("Make subgraph for locations: %s \n" % make_subgraph)
    label = label.replace(" ","_")
    print ("label: %s \n" % label)

    #my_datafile = raw_input("Please enter filename with raw LLDP info: ")

    my_datafile = "/etc/ansible/lldp-to-graph/results/lldp-to-graph.json"

#    print ("LLDP file: %s\n" % my_datafile)

    #my_data=pd.read_table(my_datafile, sep=';')
    #my_data=pd.read_table('sysconfig_table.csv', sep=';')
    #my_data=pd.read_table('c:/Python27/Hafslund/sysconfig_table.csv', sep=';')

    #print my_data
    outputfile = my_datafile +'.dot'

    fw = open(outputfile,'w')

    section = "false"
    collectinfo = "false"
    lldplink = "strict graph {"
#    lldplink = "graph {"
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
    
    
  #  fw.write("label=%s;\n" % label)
    fw.write("labelloc=top;\n")
    fw.write("labeljust=left;\n")
    fw.write("labelfontsize=24;\n")
    fw.write("label=%s;\n" % label)


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
         localsysname = localsysname.replace(".","_")
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
       elif ("System name" in row and section == "true" and collectinfo == "true"):
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
              intfspeed = '10G'
              linkcolor = 'green'
           elif ("1000" in row):
              intfspeed = '1G'
              linkcolor = 'red'
           elif ("40000" in row):
              intfspeed = '40G'
              linkcolor = 'blue'
           else:
              intfspeed = 'Unknown'
              linkcolor = "gray"


           if (('DIST' in ulocalsysname and 'DIST' in uremotesysname) or ('BNG' in uremotesysname) or  ('CORE' in uremotesysname)):
              pen = '6'
           else:
              pen = '1'


           lldplink = ulocalsysname + ' -- ' + uremotesysname + ' [penwidth="' + pen + '", color="' + linkcolor + '", label="'  + intfspeed + '", fontsize=8 ];'
    #      lldplink = ulocalsysname + ' -- ' + uremotesysname + ' [penwidth="' + pen + '", color="' + linkcolor + '", label="'  + intfspeed + '", fontsize=8, headlabel=' + '"' + localinterfa$

           print lldplink
           fw.write("%s\n" %lldplink)
           collectinfo = "false"


    str = fo.read(50);
    fo.close()



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
         tempsysname = localsysname.upper()
         labellocation = 'bottom'
         if ("ACCESS" in tempsysname):
               icon = 'icons/accesswitch.gif'
         elif ("DIST" in tempsysname):
               icon = 'icons/distswitch.gif'
         elif ("CORE" or "BNG" in tempsysname):
               icon = 'icons/router.gif'
         elif ("_AP_" or "WLC" in tempsysname):
               icon = 'icons/wifi.gif'
         localsysname = tempsysname + '[shape=none, label="' + tempsysname +'", labelloc="' + labellocation +'"fontsize = 9, image="' + icon +'"]'
         print ("%s;\n" %localsysname)



         if ('yes' in make_subgraph):
           pos = tempsysname.rfind('_') + 1
           clusteras =  tempsysname[pos:]
           fw.write("subgraph cluster_%s {\n" %clusteras)
           fw.write("%s;\n" %localsysname)
           fw.write("label = %s;\n" %clusteras)
           fw.write("fontsize = 20;\n")
           if ('DIST' in tempsysname):
             fw.write("color=grey;\n")
             fw.write("style=filled;\n")
           fw.write("}\n")
         else:
           fw.write("%s;\n" %localsysname)
    fo.close()

    fw.write("}\n")
    fw.close()
    print ("DOT fil for Graphviz:   %s  " % outputfile)
    print ("Run command - dot -Tpng %s >%s.png - on Graphviz computer " % (outputfile, outputfile))



if __name__ == "__main__":
#   main(sys.argv[1:])
   main()
