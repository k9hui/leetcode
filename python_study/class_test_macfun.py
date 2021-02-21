class A(object):
    def __init__(self,s):
        print("in A_init")
        self.s = s
    def __str__(self):
        return "this is "+self.s
    def __new__(cls,*arg,**kwarg):
        print("A_new")
        return object.__new__(cls)



if __name__=="__main__":
    aa = A("wenhui")
    print(aa)
