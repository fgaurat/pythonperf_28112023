


def do_log(func):
    print("do_log",func)
    def wrapper(a):
        print("LOG",a)
        r = func(a)
        print("LOG RETURN",r)
        return r
    return wrapper

@do_log
def say_hello(name):
    print(f"say_hello({name})")
    return f"Hello {name} !"

def main():

    print("before call")
    r = say_hello("fred")
    print("after call")

    print(r)

if __name__=='__main__':
    main()
