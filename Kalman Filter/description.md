
# Demo
![ezgif com-gif-maker](https://user-images.githubusercontent.com/103611360/211449746-98be8161-c797-401e-aa54-fdb01309fba6.gif)

# Description
As shown in the demo, the red solid circle represents the centre of the orange and the green circle represents the predicted position of the orange.
I also tried the same method with one of our robot video under label, it doesn't work very well due to the detection function and I believe once we cooperate the 
kalman function with the YOLO, we can get much better results.

# The Functions

For the code file:

  - &nbsp;The _Kalmanfilter_ is the most important function that take the previous coordinates as the input and output the predicted coordinates. To implement the prediction in our YOLO code, just import the _Kalmanfilter_ into the code file and call it. 
  - Input: current coordinates (x,y)
  - Output: the predicted coordinates (new_x,new_y) --- note that the naming is just for understanding


  <sub>Source: pysource.com <sub>  
