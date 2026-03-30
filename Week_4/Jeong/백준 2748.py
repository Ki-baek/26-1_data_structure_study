import sys					
sys.stdin = open('input.txt', 'r')					
input = sys.stdin.readline  #속도위해 필수	
	
 

i=int(input())

my_list=[0]*(i+1)

if i>=0:
    my_list[1]=1

for a in range(2,i+1):
    my_list[a]=my_list[a-2]+my_list[a-1]
    
print(my_list[i])
