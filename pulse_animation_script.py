import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def foo(inputTransmit: serial.Serial) -> str:
    inputTransmit.write(b's')                                     # Transmit the char 'g' to receive the Arduino data point
    return inputTransmit.readline().decode('ascii') # Decode receive Arduino data as a formatted string
        #print(i)                                           # 'i' is a incrementing variable based upon frames = x argument

class AnimationPlot:

    def pulseAnimate(self, i, pulseDataList, inputTransmit):
        arduinoData = foo(inputTransmit)
        print(arduinoData)
        try:
     
            tempAndPulse = arduinoData.split(",");
            pulseDataList.append(float(tempAndPulse[1]))
            #pulseDataList.append(float(tempAndPulse[1]))      # Convert to float
                                                              # Add to the list holding the fixed number of points to animate

        except:                                             # Pass if data point is bad                               
            pass

        pulseDataList = pulseDataList[-100:]   
        #pulseDataList = pulseDataList[-100:0]                        # Fix the list size so that the animation plot 'window' is x number of points
        
        pulseAx.clear() 
        #pulseAx.clear()                                         # Clear last data frame
        
        self.getPlotFormat()
        pulseAx.plot(pulseDataList)
        #pulseAx.plot(pulseDataList)                                   # Plot new data frame
        

    def getPlotFormat(self):
        pulseAx.set_ylim([0, 150])                              # Set Y axis limit of plot
        pulseAx.set_title("Arduino Data")                        # Set title of figure
        pulseAx.set_ylabel("Temperature (C)")  
                                   # Set title of y axis

pulseDataList = []      
                                   # Create empty list variable for later use
                                                        
fig = plt.figure()  
   
                               # Create Matplotlib plots fig is the 'higher level' plot window
pulseAx = fig.add_subplot(111)   
                         # Add subplot to main fig window



inputTransmit = serial.Serial("/dev/cu.usbmodem101", 115200)                       # Establish Serial object with COM port and BAUD rate to match Arduino Port/rate
print(foo(inputTransmit))
time.sleep(2)                                           # Time delay for Arduino Serial initialization 


pulseRealTimePlot = AnimationPlot()


                                                        # Matplotlib Animation Fuction that takes takes care of real time plot.
                                                        # Note that 'fargs' parameter is where we pass in our dataList and Serial object. 
pulseAni = animation.FuncAnimation(fig, pulseRealTimePlot.pulseAnimate, frames=100, fargs=(pulseDataList, inputTransmit), interval=100) 



plt.show()                         
                     # Keep Matplotlib plot persistent on screen until it is closed
inputTransmit.close()   