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
