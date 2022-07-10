a, b, h = map(int,input().split())
day = 0
hei = 0
while True:
    hei += a
    day +=1
    if hei>=h:
        print(day)
        break
    hei -= b
    
    