SAR-8-241>config>router# show router interface 

===============================================================================
Interface Table (Router: Base)
===============================================================================
Interface-Name                   Adm       Opr(v4/v6)  Mode    Port/SapId
   IP-Address                                                  PfxState
-------------------------------------------------------------------------------
To-SAR-8-242                     Up        Up/Up       Network 1/1/6:11
   10.14.132.145/30                                            n/a
   2001:db8:1::1/64                                            PREFERRED
   fe80::5240:61ff:fe5b:f201/64                                PREFERRED
To-SAR-Hc-244                    Up        Up/Down     Network 1/1/1:10
   10.14.132.138/30                                            n/a
To-SAR-Hc-244-p-1-1-2            Up        Down/Down   Network 1/1/2:10
   10.14.132.129/30                                            n/a
system                           Up        Up/Down     Network system
   10.14.34.200/32                                            n/a

   
SAR-8-242>config>router# show router interface 

===============================================================================
Interface Table (Router: Base)
===============================================================================
Interface-Name                   Adm       Opr(v4/v6)  Mode    Port/SapId
   IP-Address                                                  PfxState
-------------------------------------------------------------------------------
To-IXR249                        Up        Up/Down     Network 1/1/5:0
   10.14.132.94/30                                             n/a
To-SAR-8-241                     Up        Up/Up       Network 1/1/6:11
   10.14.132.146/30                                            n/a
   2001:bd8:1::2/64                                            PREFERRED
   fe80::5240:61ff:fe5b:f601/64                                PREFERRED
To-SAR-Hc-243                    Up        Up/Down     Network 1/1/1:10
   10.14.132.142/30                                            n/a
To-SAR-Hc-243-p-1-1-2            Up        Up/Down     Network 1/1/2
   10.14.132.133/30                                            n/a
To-SAR-Hc-244                    Up        Up/Down     Network 1/1/7:14
   10.14.0.13/30                                               n/a
system                           Up        Up/Down     Network system
   10.14.34.201/32                                            n/a

SAR-Hc-243>config# show router interface 

===============================================================================
Interface Table (Router: Base)
===============================================================================
Interface-Name                   Adm       Opr(v4/v6)  Mode    Port/SapId
   IP-Address                                                  PfxState
-------------------------------------------------------------------------------
To-SAR-8-242                     Up        Up/Down     Network 1/1/4:10
   10.14.132.141/30                                            n/a
To-SAR-8-242-p-1-1-2             Up        Up/Down     Network 1/1/2
   10.14.132.134/30                                            n/a
To-SAR-Hc-244                    Up        Up/Down     Network 1/1/6:13
   10.14.0.9/30                                                n/a
system                           Up        Up/Down     Network system
   10.14.34.208/32                                            n/a

SAR-Hc-244>config>service# show router interface 

===============================================================================
Interface Table (Router: Base)
===============================================================================
Interface-Name                   Adm       Opr(v4/v6)  Mode    Port/SapId
   IP-Address                                                  PfxState
-------------------------------------------------------------------------------
To-SAR-8-241                     Up        Up/Down     Network 1/1/4:10
   10.14.132.137/30                                            n/a
To-SAR-8-241-p-1-1-2             Up        Down/Down   Network 1/1/2:10
   10.14.132.130/30                                            n/a
To-SAR-8-242                     Up        Up/Down     Network 1/1/3:14
   10.14.0.14/30                                               n/a
To-SAR-Hc-243                    Up        Up/Down     Network 1/1/6:13
   10.14.0.10/30                                               n/a
system                           Up        Up/Down     Network system
   10.14.34.209/32                                            n/a

