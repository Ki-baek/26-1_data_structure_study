import sys
sys.stdin = open('input.txt', 'r')	
input = sys.stdin.readline

tc=int(input()) 

for i in range(tc):
    
    P,Pa,Pb=map(int,input().split())
    
    l=1
    r=P #전체쪽수 P
    
    c=int((l+r)/2) #중간값:c
    cnt=0
    

    while c!=Pa:
        if c < Pa:  
            l=c #중간값이 첫번째값이 됨
            c=int((l+r)/2)#중간값 구하기
            cnt+=1

        elif c>Pa:
            r=c
            c=int((l+r)/2)
            cnt+=1
        
        elif c==Pa:
            break 
           
    l=1
    r=P
    c=int((l+r)/2)
    cnt2=0
    while c!=Pb:
        if c < Pb:  
            l=c 
            c=int((l+r)/2)
            cnt2+=1

        elif c>Pb:
            r=c
            c=int((l+r)/2)
            cnt2+=1
        
        elif c==Pb:
            break
        
    if cnt<cnt2:
        print(f"#{i+1} A")
    elif cnt>cnt2:
        print(f"#{i+1} B")
    elif cnt==cnt2:
       print(f"#{i+1} 0")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


