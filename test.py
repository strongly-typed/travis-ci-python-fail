#!/usr/bin/env python2

import sys
print(sys.path)

try:
	import jinja2
	print("import ok")
except ImportError:
	print("import fail")
	Exit(1)
