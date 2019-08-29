import calendar
print("year")
y=int(input())
print("month")
m=int(input())
print("start")
a=int(input())
print("end")
b=int(input())
print(calendar.month(y,m))
print(calendar.calendar(y,a,1,b))

