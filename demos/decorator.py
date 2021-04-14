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
print(now1)