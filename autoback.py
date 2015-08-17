#!/usr/bin/env python
#auto back_up system files
#by authors dty 2015
import os,sys,time
d_dir='/data/backup/'
d_files='system_back.tar.gz'
s_dir=['/tmp','/boot']
date=time.strftime('%Y-%m-%d')
r_dir=d_dir+date+'/'
r_name = r_dir+d_files
def back():
	if os.path.exists(r_dir) == False:
			os.mkdir(r_dir)
	
	else:
			print 'The Dir %s is exists'  % r_dir
	tar_cmd = 'tar -czvf %s %s' %(r_name,' ' .join(s_dir))
	if os.system(tar_cmd) == 0:
		print 'The backup Files Exec successful!'
	else:
		print 'The backup Files is Failed'
try:
			if len(sys.argv[1]) == 0:
				pass
except IndexError:
				print '\033[35mUsage:{please Exec %s help|back}\033[0m' %sys.argv[0]
try:
			if sys.argv[1]  == 'back':
 	 			print 'start_________________________________________________'
	 			back()
			else :
				print 'nonono %s should use help|back' % sys.argv[0]
except IndexError:
				pass
try:
			if sys.argv[1]=='help':
				print '\033\28mback !!!!!!11'
except IndexError:
			pass
