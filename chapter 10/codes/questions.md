### Some notes
1. What's an object
An object is a software 
entity that contains both data and procedures.
2. What is encapsulation?

Encapsulation refers to the combining of data and code into a single object. Data 
hiding refers to an object’s ability to hide its data attributes from code that is outside the 
object.

3. Why is an object’s internal data usually hidden from outside code?

the data attributes are protected from accidental 
corruption. In addition, the code outside the object does not need to know about the format 
or internal structure of the object’s data.


4. What are public methods? What are private methods?

Methods that can be accessed by entities outside the object are known as public 
methods.

private methods, which are part of the object’s private, internal 
workings

5. You hear someone make the following comment: “A blueprint is a design for 
a house. A carpenter can use the blueprint to build the house. If the carpenter 
wishes, he or she can build several identical houses from the same blueprint.” 
Think of this as a metaphor for classes and objects. Does the blueprint represent 
a class, or does it represent an object?

class

6. In this chapter, we use the metaphor of a cookie cutter and cookies that are 
made from the cookie cutter to describe classes and objects. In this metaphor, are 
objects the cookie cutter, or the cookies

cookies

7. What is the purpose of the _ _init_ _ method? When does it execute?

initialize the data attributes of an instance
when the object is create

8. What is the purpose of the self parameter in a method?
It represent the current object

9. In a Python class, how do you hide an attribute from code outside the class?
Use the __

10. What is the purpose of the _ _str_ _ method?
return the state of an object

11. How do you call the _ _str_ _ method?
when calling the class with print of str function

12. 10.12 What is an instance attribute?
Attribute belonging to the object created

13. A program creates 10 instances of the Coin class. How many _ _sideup
attributes exist in memory?

10

14. What is an accessor method? What is a mutator method

accessor: method for accessing/getting the value of an attribute
mutator: method for mutating/setting the value of an attribute

15. The typical UML diagram for a class has three sections. What appears in these 
three sections?

* the name of the class
* the attributes
* the methods.

16. What is a problem domain?
The problem domain is the set of real-world objects, parties, and major events related to the 
problem

17. When designing an object-oriented application, who should write a description of 
the problem domain?

person who understand the nature of the problem (that can be the developper)

18. How do you identify the potential classes in a problem domain description?
* identify the nouns as potential classes
* identify classes that are related to the problem
19. What are a class’s responsibilities?
* what a class can know
* what a class can do
20. What two questions should you ask to determine a class’s responsibilities?
A class’s responsibilities are:
•	 the things that the class is responsible for knowing.
•	 the actions that the class is responsible for doing.
21. Will all of a class’s actions always be directly mentioned in the problem domain 
description
No