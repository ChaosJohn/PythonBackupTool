#!/usr/bin/python
# Filename: backup_temp.py

import os
import time

source = ['/home/chaos/net.py', '/home/chaos/bin']

target_dir = '/home/chaos/backup/'

today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment --> ')
if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
	os.mkdir(today) 
	print 'Successfully created directory', today

zip_command = "zip -r %s %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'Successfully backup to', target
else:
	print 'Backup Failed'
