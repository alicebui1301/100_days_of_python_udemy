# How to use OOP: Classes and Objects
## Introduction to Object Oriented Programming Implementation
We have seen a little bit about why Object Oriented Programming is really useful. Now, let's take a look at how you would actually go about implementing Object Oriented Programming.

## Modeling Real-World Objects in OOP
In the last lesson, we discussed an example of a restaurant where we hired three types of staff and had a manager who managed all these different types of staff. The reason Object Oriented Programming is called so is because it tries to model a real-world object.

For example, if we are creating a virtual restaurant, we would need to model a virtual chef, waiter, cleaner, and manager.

## Attributes and Methods of an Object
Let's say we want to model a waiter. To do this, we need to consider two things: what it has and what it does.

### Attributes (What it has)
- Is it holding a plate? (true or false)
- Which tables is it responsible for? For example, tables 4, 5, and 6.

### Methods (What it does)
- Taking an order to the chef.
- Taking payments and adding money to the restaurant.
- These two aspects, what the waiter has and what the waiter does, are the two most important things that make up an object: its attributes and its methods.

## Understanding Attributes
Attributes are basically variables associated with a modeled object like our waiter. They are not free-floating variables but are attached to a particular object. For example, the waiter's tables responsible is an attribute.

## Understanding Methods
Methods are functions that a particular modeled object can perform. For example, a waiter object can take an order or take payment. These are not free-floating functions but are tied to the object.

## Terminology in Object Oriented Programming
There are many new words in Object Oriented Programming and programming in general. Over time, these terms will become familiar. For now, remember that in Object Oriented Programming, we try to model real-life objects that have things (attributes) and can do things (methods).

## Attributes are usually modeled with variables.
Methods are modeled by functions.
Essentially, an object combines some piece of data and some functionality altogether in the same entity.

## Classes and Objects
We can have multiple objects generated from the same type. When we model a particular job in our virtual restaurant, like the waiter's job, and determine what the waiter has and what it can do, we can generate multiple versions of the same object.

For example, we could have Henry who is a waiter and Betty who is also a waiter. We can generate as many of these as we want from the same blueprint.

In Object Oriented Programming, we call this blueprint or type a class. The individual objects generated from the blueprint are called objects.

## Creating Objects from Classes
Now, let's take a look at how you use these class blueprints to create an actual object.

## Key Takeaways
- Object Oriented Programming (OOP) models real-world objects by combining data and functionality.
- Objects have attributes (variables representing what they have) and methods (functions representing what they can do).
- Attributes are variables attached to specific objects, not free-floating.
- Multiple objects can be created from the same class blueprint, each representing an individual instance.