# ColorBasedTracking

Based on the color code of object in HSV (Hue, Saturation, Value).

I will first identify HSV code of the color that I need to track. 

Then by using OpenCV I will track that object in real-time. 

I will mask out the HSV code color area by reading the pre-processed frame.

Next I will make a minimum enclosing circle bounding the color area.

Using the position of the color I will track the position. If it is in the left from the centre then output will print left, if it is in the center, the ouput will print move ahead until a certain limit.


