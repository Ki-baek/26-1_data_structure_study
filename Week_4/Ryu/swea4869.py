import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

T=int(input())

for tc in range(1,T+1):
    
    N=int(input())
    list=[0]*N
    for i in range(3,N):
        
        
        list[1]=1
        list[2]=3
       
        list[i]=list[i-2]*2+list[i-1]
        
   
    
    val=int(N/10)
    print(f"#{tc} {list[val]}")
