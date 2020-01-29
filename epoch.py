


import time


#tim=time.time_ns()
#print(tim)
tim=1580228895861227600
micro=tim/1000000000
mod=tim%1000000000
print(mod)
print(micro)
mod=str(mod)
list=([str(mod)[i:i+3] for i in range(0, len(str(mod)), 3)])
milisec=(list[0])
microsec=(list[1])
nanosec=(list[2])
day=time.strftime("%a",time.localtime(micro))
date=time.strftime("%d",time.localtime(micro))
month=time.strftime("%b",time.localtime(micro))
year=time.strftime("%Y",time.localtime(micro))
hours=time.strftime("%H",time.localtime(micro))
minute=time.strftime("%M",time.localtime(micro))
sec=time.strftime("%S",time.localtime(micro))

print(day)
print(date)
print(month)
print(year)
print(hours)
print(minute)
print(sec)
print(milisec)
print(microsec)
print(nanosec)

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

