

def make_increment(inc_value):
    print(f"make_increment({inc_value})")

    def do_inc(value):
        return inc_value+value
    
    def close():
        print("close")
    return do_inc,close

def main():
    inc_function,close = make_increment(10)
    a = inc_function(5)
    print(a)# 15
    a = inc_function(6)
    print(a)# 15
    a = inc_function(7)
    print(a)# 15
    close()


if __name__=='__main__':
    main()
