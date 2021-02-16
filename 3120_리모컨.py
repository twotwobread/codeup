a, b = map(int, input().split())
count = 0

for i in range(40):
    if a<b:
        if abs((a+10)-b) <= abs((a+5)-b) and abs((a+10)-b) <= abs((a+1)-b):
            count+=1
            a+=10
            continue
        elif abs((a+5)-b) < abs((a+10)-b) and abs((a+5)-b) <= abs((a+1)-b):
            count+=1
            a+=5
            continue
        elif abs((a+1)-b) < abs((a+5)-b) and abs((a+1)-b) < abs((a+10)-b):
            count+=1
            a+=1
            continue
    elif a>b:
        if abs((a-10)-b) <= abs((a-5)-b) and abs((a-10)-b) <= abs((a-1)-b):
            count+=1
            a-=10
            continue
        elif abs((a-5)-b) < abs((a-10)-b) and abs((a-5)-b) <= abs((a-1)-b):
            count+=1
            a-=5
            continue
        elif abs((a-1)-b) < abs((a-5)-b) and abs((a-1)-b) < abs((a-10)-b):
            count+=1
            a-=1
            continue
    else:
        break
print(count)
    
