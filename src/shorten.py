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
	api = googl.Googl()
	generate = api.shorten("http://" + ip_addr)
	short_url = generate.get('id')
	return short_url
	
shorten_url()
