# encoding=UTF-8

# Copyright © 2007-2015 Jakub Wilk <jwilk@jwilk.net>
#
# This package is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This package is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

from __future__ import division

if __name__ != '__main__':
    raise ImportError('This module is not intended for import')

import djvu.sexpr
import os

proc_status = '/proc/{pid}/status'.format(pid=os.getpid())
scale = dict(kB=1024)

def mem_info(key='VmSize'):
    try:
        file = open(proc_status)
        for line in file:
            if line.startswith('{key}:'.format(key=key)):
                _, value, unit = line.split(None, 3)
                return int(value) * scale[unit]
    finally:
        file.close()

try:
    range = xrange
except NameError:
    pass

step = 1 << 17
while True:
    mb = mem_info() / (1 << 20)
    print('{mb:.2f}M'.format(mb=mb))
    [djvu.sexpr.Expression(4) for i in range(step)]

# vim:ts=4 sw=4 et
