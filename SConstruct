#!/usr/bin/env python2
import os

import sys
print("XXX sys.path = ", sys.path)

env = Environment(
                toolpath = ['scons/site_tools'],
                tools = ['template', 'doxygen', 'configfile', 'helper', 'font', 'bitmap'],
                ENV = os.environ)

try:
	print("Trying import jinja2")
	import jinja2
except ImportError:
	print("import fail")
	Exit(1)
