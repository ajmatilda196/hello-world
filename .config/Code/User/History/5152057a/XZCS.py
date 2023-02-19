//how to write the simple JavaScript program?   
import PyV8
ctx = PyV8.JSContext()
ctx.enter()

js = """
function escramble_758(){
var a,b,c
a='+1 '
b='84-'
a+='425-'
b+='7450'
c='9'
document.write(a+c+b)
}
escramble_758()
"""

print ctx.eval(js.replace("document.write", "return "))


class MockDocument(object):

    def __init__(self):
        self.value = ''

    def write(self, *args):
        self.value += ''.join(str(i) for i in args)


class Global(PyV8.JSClass):
    def __init__(self):
        self.document = MockDocument()

scope = Global()
ctx = PyV8.JSContext(scope)
ctx.enter()
ctx.eval(js)
print scope.document.value




#Source: https://stackoverflow.com/questions/10136319





// how to use list in python?   
squares1 = [x**2 for x in range(1, 11)]


squares2 = list(x**2 for x in range(1, 11))




#Source: https://stackoverflow.com/questions/51861577




