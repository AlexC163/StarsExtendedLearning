# StarsExtendedLearning

## Essay regarding the graph

A Hertzsprung-Russell (or H-R) diagram is used to organize the life cycle of a star through the relationship between a star’s luminosity and a star’s surface temperature. By plotting many stars on this graph, we can find similarities between stars in the same class and ultimately use the H-R diagram to map out the life cycle of a star.
For my extended learning project, I have come up with and implemented my version of this. There are three main components to this project. These components include the variables used to determine the location of stars on my graph, the classification of stars on my graph, and the tools and resources used to implement the graph.

When determining the variables to use for my graph, I knew that I had to choose carefully - to allow for maximum understanding when looking at my graph, the variables should show a clear correlation between multiple stars of a similar class. For this to occur, I first chose two variables to keep consistent. These were luminosity and surface temperature - which are the same as an H-R diagram. I then wanted to show how there are many similarities between stars - so I have shown the relationships between stars and their radial velocity, mass, and solar radius. In this essay, I will not only talk about how I got to this point, but how you can use these factors to help group stars.

The second component of my project involved classifying the stars on my graph. I did this by giving each class of star a different color and symbol on my graph. This has allowed anyone to look at my graph and observe that the stars of the same color and shape - are close together - and subsequently in the same class. In order to make this even more visible, I have circled the stars on my graph.

The final component of my project is the tools and resources used to implement the graph. To implement the graph, I first had to figure out how I was going to display it. A few ideas came to mind. I could use MATLAB, which is a programming language used for data visualization - exactly my purpose. However, MATLAB requires an account associated with a university or company - which I did not have access to. Another option that came to mind was R, which is a programming language used for statistics - such as graphing (which is what I was doing here). However, I do not have much experience in R and I knew that there had to have been a much better option. That is when I thought of Python. I knew that there must be a tool to graph in Python - as it is one of the largest programming languages in the world. However, I did not know what this tool was. I began researching possibilities and came across multiple options. However, the option that seemed to be the most promising was matplotlib. Matplotlib is a data visualization tool used in Python. With it, I would be able to implement a 3D graph and display the knowledge that I had collected. I began learning matplotlib through online videos, documentation, and experimentation. And before long, I had created the beginnings of what was to come of my project.

I was persistent, constantly learning new information concerning my graph, and how I could not only optimize it on the backend but also make it visually appealing. And that takes us to where we are now.
With my graph, you can visualize the relations through different stars. My graph takes a step beyond the Hertzberg-Russell diagram - stepping into the third dimension. As seen in the below images, the stars in the same classes are near each other - which shows that they have relations to one another. Although I used surface temperature, luminosity, and radial velocity as the factors, this could easily be implemented with many different factors. While some stars are astray, in general, there is a clear pattern to stars in the same class.

With my graph, you can visualize the relations through different stars. My graph takes a step beyond the Hertzberg-Russell diagram - stepping into the third dimension. As seen in the below images, the stars in the same classes are near each other - which shows that they have relations to one another. Although I used surface temperature, luminosity, radial velocity, mass, and solar radius as the factors, this could easily be implemented with many other factors as well. While some stars are astray, in general, there is a clear pattern to stars in the same class.


## Code output (Graph Images)

![radial_velocity](https://user-images.githubusercontent.com/95631939/208335651-4923e775-83cf-4795-a343-1976e632a965.png)
![masses](https://user-images.githubusercontent.com/95631939/208335653-d9655e5c-17e9-4fc2-aa9c-ec6bbe868647.png)
![solar_radii](https://user-images.githubusercontent.com/95631939/208335662-99a816a8-c296-471b-918f-22071da08bee.png)


### Set up

    pip install matplotlib
