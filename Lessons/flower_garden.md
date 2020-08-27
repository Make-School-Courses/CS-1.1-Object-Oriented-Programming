# The Flower Garden

In this assignment we use turtle graphics combined with OOP to create a beautiful garden!

Use [this code](https://repl.it/@MakeSchool/flowergardenstarter#main.py) to get started.

<iframe src="https://repl.it/@MakeSchool/flowergardenstarter?lite=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>



You are given a function that draws a flower using turtle graphics.

**For this assignment you will need to complete the following requirements:**  

1. Using the given draw_flower() function as a starting point, create a class called Flower that has the following properties:
    
    1. num_petals: the number of petals the final flower will have
    1. color: the color of the petals
    1. petal_length: how long each petal will be
    1. petal_size: how thick each petal will be
    1. x: the x location on the drawing
    1. y: the y location on the drawing

    The Flower class will also have the following methods:
    
    1. get_turn_degrees(): a helper method that will take in the number of petals and return how many degrees the turtle will need to turn to draw the next petal
    1. draw(): a method that when called will draw the flower using the above properties

1. Create another class of your choice that will represent something else in your garden. An idea could be a Tree class that has properties such num_leaves, color, x, y, and height. Your class will need to to have at least three properties and least one method.

1. Write an automated test that uses asserts to check if your get_turn_degrees() helper function is working correctly

1. Instantiate at least three flowers and at least three of the objects derived from the class of your choice to complete your garden!


**When you are finished submit a link to your code on Gradescope as well as a demo video showing your code running and explaining your code as well as what coding constructs you used**

Stretch Challenges

1. Use inheritance to create a superclass for your garden class that your Flower and class of your choice can inherit from

1. Create an even more complex garden with more than just two types of objects

1. Turtle graphics includes some basic event handler methods such as [onclick()](https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.onclick) and [ondrag()](https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.ondrag), use these to make your garden art interactive!


