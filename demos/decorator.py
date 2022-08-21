

def log(fun):
    def wrapper(*args,**kw):
        print(fun.__name__)
        return fun(*args, **kw)
    return wrapper


def now():
    print('2020-01-27')



print(log(now))
now = log(now)
print(now)
now1 = now()


def a():
    print("Tom is sing")


f = a
print(a.__name__)
print(f.__name__)
print(id(a))
print(id(f))