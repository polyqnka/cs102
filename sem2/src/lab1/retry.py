import time
from functools import wraps

def retry(attempts, delay, exceptions=None):
    def retry_decorator(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            last_exception = None
            opt_dict = {'attempts': attempts, 'delay': delay}
            while opt_dict['attempts'] > 0:
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    msg = "Exception: {}, Retrying in {} seconds...".format(e, delay)
                    print(msg)
                    time.sleep(opt_dict['delay'])
                    opt_dict['attempts'] -= 1
            return last_exception

        return f_retry

    return retry_decorator

@retry(attempts=3, delay=2, exceptions=ValueError)
def main():
    print('Выполняется...')
    string = chr(-15)
    return string

if __name__ == '__main__':
    main()