def master(func):
    def inner(*a,**out):
        obj = "\tinner"
        out["lan"]="c++"
        return func(*a,**out)
    return inner

@master
def display(*a,**name):
    print(a,name)

display("python","Adsf",name="sdf",)
