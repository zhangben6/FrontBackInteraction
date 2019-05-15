import time

def log_time(func):

    def _log(b):
        beg = time.time()
        res = func(b)
        print('User time:{}'.format(time.time()-beg))
        return res 
    
    return _log

@log_time
def mysleep(b):
    a = 1
    return a + b


# print(mysleep(5))

class LogTime:
    def __init__(self,use_int=False):
        self.use_int = use_int
    
    def __call__(self,func):
        def _log(*args,**kwargs):
            beg = time.time()
            res = func(*args,**kwargs)
            if self.use_int:
                print('use time:{}'.format(int(time.time()-beg)))
            else:
                print('use time:{}'.format(time.time()-beg))
            return res
        return _log

@LogTime(True)
def mysleep():
    time.sleep(2)

# mysleep()

import time
def logtime(func):
    def _log(*args,**kwargs):
        beg = time.time()
        res = func(*args,**kwargs)
        print('use time:{}'.format(time.time()-beg))
        return res
    return _log

@logtime
def mysleep():
    time.sleep(2)

mysleep()