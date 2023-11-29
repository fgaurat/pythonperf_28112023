class A:

    def show(self):
        print("Class A")

class B(A):

    def show(self):
        print("Class B")

class C(A):

    def show(self):
        print("Class C")

class D(C,B):

    def show(self):
        super(B,self).show()
        print("Class D")


def main():
    d = D()
    print(D.mro())
    d.show()

if __name__=='__main__':
    main()
