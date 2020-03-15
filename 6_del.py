def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class CException(Exception):
    pass


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            #print('GGG')
            break
        else:
            print('......', message)
    return 'Returned from subgene()'


@coroutine
def delegator(g):
#    while True:
#       try:
#            data = yield
#            g.send(data)
#        except CException as e:
#            g.throw(e)
    result = yield from g
    print(result)