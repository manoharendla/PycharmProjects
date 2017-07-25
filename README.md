# Python Tutorial

### 1. What is **__init__** method in python

Init method of a class comes into picture when a class is initialized . When an object instatiation operation is invoked with `x=MyClass(value1,valu2)` the object x is instantiated with specific initial state with values of value1 and value2.

**Example of car class:**

```Python
class Car:
    def __init__(self,color,type):
        self.c=color
        self.t=type
    def speed(self,kmph)
    print "Speed of the car self.type is", kmph
    

swift = Car(red,hatchback)
swift.speed(100)
ciaz = Car(blue,sedan)
ciaz.speed(150)
 
``` 

### What is pass in python ?

Pass is a keyword which is used to perform  *No Operation*.

Lets say you wanted to create a class in which you defined methods without any body

```Python
class Pass:
    def firstMethod(self):
        pass

    def secondMethod(self):
        pass

t=Pass()
t.firstMethod()

```

If a method is defined without  a pass keyword an Indentation Error is seen. So in such cases we usually prefer pass to perform a safe no operation.

```Python
    def secondMethod(self):
      ^
IndentationError: expected an indented block

```