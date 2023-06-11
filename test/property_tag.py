t1={"name":"Rajiv"}
t2={"name":"shweta"}

class test():

    @property
    def obj(self):
        return t2;

t3=test()
print(t3.obj)

print(t3.__getattribute__("obj"))