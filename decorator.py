#-*- encoding=UTF-8 -*-

def log(levl, *args, **kvargs):
    def inner(func):
        '''
            *args 无名字参数 hello('name',2)
            **kvargs 有名字参数  hello(name='name', age=2)
            '''

        def wrapper(*args, **kvargs):
            print levl, 'before calling', func.__name__
            func(*args, **kvargs)
            print levl, 'end calling', func.__name__
        return wrapper
    return inner


@log(levl = 'INFO')
def hello():
    print 'hello'


if __name__=='__main__':
    hello()