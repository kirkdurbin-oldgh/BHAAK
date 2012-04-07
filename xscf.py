### XSCF Script for BHAAK
### www.kirkdurbin.com
### www.blackhatacademy.org
### Thanks to hatter, ohdae, and m4tr1c3s for the help

import os
import sys

if os.geteuid() != 0:
	sys.exit('You are not root!')
else:
	from src import cloner, server
