## www.kirkdurbin.com
## www.blackhatacademy.org

import os
import urllib
import urllib2
import googl

def get_ip():
	ext_ip = urllib2.urlopen('http://ifconfig.me/ip').read()
	return ext_ip

def shorten_url():
	ip_addr = get_ip()
	key = "AIzaSyB_75xcjif1ZSl565PynVgH6XtFGPzrwF8"
	api = googl.Googl(key)
	generate = api.shorten(ip_addr)
	short_url = generate.get('id')
	#\print short_url
	return short_url
	
