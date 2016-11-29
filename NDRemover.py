import os
def dirlist():
	dirlist = os.listdir("Your Directory Address Here")
	dirlist.sort();
	lenli=len(dirlist)
	running=True
	index=0
	for index, item in enumerate(dirlist):
		tem=item[:-4]
		tem2 = dirlist[(index+1)%lenli]
		tem2=tem2[:-4]
		if(tem == tem2):
			dirlist[index]='0'
			dirlist[(index+1)%lenli]='0'
		print(tem,tem2)
	count1=0
	for index, item in enumerate(dirlist):
		
		if(item!='0'):
			tem="Your Directory Address Here"+item
			count1+=1;
			os.remove(tem)
		
	if (count==0):
		print("no single files found")
	
dirlist()
raw_input()
