#! /usr/bin/env python3

import sys, os
print(os.path.relpath(sys.argv[1], sys.argv[2]))
