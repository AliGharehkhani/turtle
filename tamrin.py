# import package

import turtle 

 

# method to draw ellipse

def draw(turtle,rad): 

     

  # rad --> radius of arc 

  for i in range(2): 

     

    # two arcs 

    turtle.circle(rad,90) 

    turtle.circle(rad//2,90) 

Window=turtle.Screen()
Ruby=turtle.Turtle()


# Main section

# tilt the shape to negative 45

Ruby.seth(-45) 

 

# calling draw method

draw(Ruby,100)

Window.mainloop()