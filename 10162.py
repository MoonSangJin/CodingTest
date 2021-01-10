#그리디

t=int(input())
#a는 300초, b는 60초, c는 10초
count1=0
count2=0
count3=0

while True:
    if (t>=300):
        count1+=(t//300)
        t=t-(300*(t//300))
        if(t==0):
            break

    if (t>=60):
        count2+=(t//60)
        t=t-(60*(t//60))
        if(t==0):
            break

    if (t>=10):
        count3+=(t//10)
        t=t-(10*(t//10))
        if(t==0):
            break

    if t>0:
        print('-1')
        break    

  
if(t==0):
    print(count1,count2,count3)
  