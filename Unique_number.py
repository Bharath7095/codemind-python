a=int(input())
ans0=0
ans1=0
ans2=0
ans3=0
ans4=0
ans5=0
ans6=0
ans7=0
ans8=0
ans9=0
while(a!=0):
    r=a%10
    if(r==0):
    	ans0+=1
    if(r==1):
    	ans1+=1
    if(r==2):
    	ans2+=1
    if(r==3):
    	ans3+=1
    if(r==4):
    	ans4+=1
    if(r==5):
    	ans5+=1
    if(r==6):
    	ans6+=1
    if(r==7):
    	ans7+=1
    if(r==8):
    	ans8+=1
    if(r==9):
    	ans9+=1
    a=a//10
if(ans0>1 or ans1>1 or ans2>1 or ans3>1 or ans4>1 or ans5>1 or ans6>1 or ans7>1 or ans8>1 or ans9>1):
	print('Not Unique Number')
else:
	print('Unique Number')