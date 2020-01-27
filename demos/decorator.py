def log(fun):
    def wrapper(*args,**kw):
        print(fun.__name__)
        fun()
        print('test')
    return wrapper

@log
def now():
    print('2020-01-27')

now()