1. In this section, we discussed superclasses and subclasses. Which is the general 
class, and which is the specialized class?
superclasse == general
subclasses = specialized
2. 	 What does it mean to say there is an “is a” relationship between two objects?
heritence
subclass is a superclass
3. What does a subclass inherit from its superclass?
data attributes and methds
4. 	 Look at the following code, which is the first line of a class definition. What is the
name of the superclass? What is the name of the subclass?
class Canary(Bird):

superclass = bird
subclass = Cananry

5. Look at the following class definitions:
class Vegetable:
 def __init__(self, vegtype):
 self.__vegtype = vegtype
 def message(self):
 print("I'm a vegetable.")
class Potato(Vegetable):
 def __init__(self):
 Vegetable.__init__(self, 'potato')
 def message(self):
 print("I'm a potato.")
 Given these class definitions, what will the following statements display?
v = Vegetable('veggie')
p = Potato()
v.message() # I'm a vegetable
p.message()# I'm a potato

