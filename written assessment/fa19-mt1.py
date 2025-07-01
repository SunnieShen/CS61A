def mint(y):
    return print(-2)
def snooze(e,f):
    if e and f():
        print(e)
    if e or f():
        print(f)
    if not e:
        print('naughty')
def lose():
    return -1
def alarm():
    print('Midterm')
    1/0
    print('Time')
def sim(b,a):
    while a>1:
        def sc(ar):
            a=b+4
            return b
        a,b=a//2,b-a
        print(a)
    print(sc(b-1),a)

pumbaa = lambda f: lambda x:f(f(x))
pumbaa = pumbaa(pumbaa)
rafiki = 1
timon = lambda y: y+rafiki
rafiki = -1

print(mint(print))
print(snooze(1,lose))
snooze(print(1),alarm)
sim(3,3)
pumbaa(timon)(5)

