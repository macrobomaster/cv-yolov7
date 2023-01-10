
# Demo
![ezgif com-gif-maker](https://user-images.githubusercontent.com/103611360/211449746-98be8161-c797-401e-aa54-fdb01309fba6.gif)

# Description
As shown in the demo, the red solid circle represents the centre of the orange and the green circle represents the predicted position of the orange.
I also tried the same method with one of our robot video under label, it doesn't work very well due to the detection function and I believe once we cooperate the 
kalman function with the YOLO, we can get much better results.

# The Functions

For the three different code files:

  - &nbsp;The _Kalmanfilter_ is the most important function that take the previous coordinates as the input and output the predicted coordinates.
  - &nbsp;The _orange_detector_ is the function used to detect the orange appeared in the demo. 
  Its principle is to track the obvious orange color appear in the frame and return the coordinates of it.
  - &nbsp;The _orange_prediction_ is the main function. It takes the coordinates from _orange_detector_ to draw the solid red circle and 
  also puts them into _Kalmanfilter_ to draw the green circle.
  
  <sub>Source: pysource.com <sub>  
