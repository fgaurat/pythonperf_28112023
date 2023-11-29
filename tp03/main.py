import traceback

# ZeroDivisionError => UpperCamelCase/PascalCase
# zeroDivisionError => camelCase
# zero_division_error => snake_case
# zero-division-error => kebab-case 

def div(a,b):
    return a/b

def call_div(a,b):
    try:
        print('OPEN LOG')
        r = div(a,b)
    finally:
        print('CLOSE LOG')
    return r

def main():
    try:
        a = 2
        # b = int(input("b : "))
        b = 2
        # c = a/b
        c = call_div(a,b)
        print(c)

    except ZeroDivisionError as e:
        print("Erreur ZeroDivisionError !")
        # traceback.print_exc()
    except TypeError as e:
        print("Erreur TypeError !")
    except ValueError as e:
        print("Erreur TypeError !")
    except Exception as e:
        print("Exception")
        print(e,type(e))
    else:
        print("pas d'erreur")

    print("le code après")
if __name__=='__main__':
    main()
