from collections import deque

t = int(input())  

for i in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split()))) 
    count = 0

    while q:
        max_priority = max(q) 
        front_queue = q.popleft()
        
        m -= 1 
        
        if front_queue == max_priority:  
            count += 1 
            if m < 0:  
                print(count) 
                break
        else:
            q.append(front_queue)  
            if m < 0: 
                m = len(q) - 1 
