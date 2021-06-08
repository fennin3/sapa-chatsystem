#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/sapauser/sapachat/")

from chat import app as application
application.secret_key = '@\xdf\xa5\x1b{\xd0\x14\x16G\x99\xb7X\xcd\xc4C\xf1'
