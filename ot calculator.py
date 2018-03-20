hrs = input("Enter Hours:")
h = float(hrs)
rate= input ("Enter Rate:")
r= float(rate)
pay= h*r
overtime = (40*r)+(1.5*r) * (h-40)
if hrs<=40:
    print (pay)
if hrs>40:
    print (overtime)
