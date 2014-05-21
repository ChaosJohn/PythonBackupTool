#!/usr/bin/python
# Filename: backup_tar.py

import os
import time

source = ['/home/chaos/net.py', '/home/chaos/bin']

target_dir = '/home/chaos/backup/'

today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment --> ')
if len(comment) == 0:
	target = today + os.sep + now + '.tar'
else:
	target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.tar'

if not os.path.exists(today):
	os.mkdir(today) 
	print 'Successfully created directory', today

zip_command = 'tar -cvzf %s %s' % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'Successfully backup to', target
else:
	print 'Backup Failed'
