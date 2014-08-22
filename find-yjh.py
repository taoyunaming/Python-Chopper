#coding = utf-8
import os
import re
import glob
all_file = []
re1 = '\<\?php(.+eval.*)'
re2 = r'\@\$\_\=(.*)'
def fun( path ):
     for fn in glob.glob( path + os.sep + '*' ):
         if os.path.isdir( fn ):
             fun( fn )
         else:
             all_file.append( fn )
             
if __name__ == "__main__":
	path = os.path.split( os.path.realpath( __file__ ) )[0]
	fun( path )
	all_file = [i for i in all_file if i.endswith(".php")]
	for i in all_file:
		rf = open(i);data = rf.read();rf.close();x = re.search( re1, data );y = re.search( re2, data );
		if x:print i,x.group(0);
		if y:print i,y.group(0);
