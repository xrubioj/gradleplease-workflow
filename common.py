# -*- coding: utf-8 -*-
__author__ = 'eveliotc'
__license__ = 'See LICENSE'

import alfred
import sys
from subprocess import Popen, PIPE

def json_to_obj(x):
    if isinstance(x, dict):
        return type('X', (), {k: json_to_obj(v) for k, v in x.iteritems()})
    else:
        return x

def join_query(dic):
    return ' '.join(dic)

def le_result(r):
    alfred.write(r)
    sys.exit()

def xml_result(r):
    le_result(alfred.xml(r))

def empty_result():
    xml_result([])

def apple_script(scpt, args=[]):
     p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
     stdout, stderr = p.communicate(scpt)
     return stdout

def tell_alfred(what):
    apple_script('tell application "Alfred 2" to search "%s"' % what)