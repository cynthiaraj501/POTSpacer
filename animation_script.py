import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def foo(inputTransmit: serial.Serial) -> str:
    inputTransmit.write(b's')                                     # Transmit the char 'g' to receive the Arduino data point
    return inputTransmit.readline().decode('ascii') # Decode receive Arduino data as a formatted string
    
class AnimationPlot:

    def animate(self, i, tempDataList, inputTransmit):
        arduinoData = foo(inputTransmit)
        
        try:
     
            tempAndPulse = arduinoData.split(",");
            tempDataList.append(float(tempAndPulse[0]))
                                                            # Add to the list holding the fixed number of points to animate

        except:                                             # Pass if data point is bad                               
            pass

        tempDataList = tempDataList[-100:]   
                                                            # Fix the list size so that the animation plot 'window' is x number of points
        
        ax.clear() 
                                                            # Clear last data frame
        
        self.getPlotFormat()
        ax.plot(tempDataList)
                                         
    def getPlotFormat(self):
        ax.set_ylim([0, 150])                              # Set Y axis limit of plot
        ax.set_title("Arduino Temperature Data")            # Set title of figure
        ax.set_ylabel("Temperature (C)")  

    def pulseAnimate(self, i, pulseDataList, inputTransmit):
        arduinoData = foo(inputTransmit)
        
        try:
     
            tempAndPulse = arduinoData.split(",");
            pulseDataList.append(float(tempAndPulse[1]))
                                                        # Add to the list holding the fixed number of points to animate

        except:                                         # Pass if data point is bad                               
            pass

        pulseDataList = pulseDataList[-100:]            # Fix the list size so that the animation plot 'window' is x number of points
                                
        
        pulseAx.clear() 
                                                        # Clear last data frame
        
        self.pulseGetPlotFormat()
        pulseAx.plot(pulseDataList)
                                         # Plot new data frame
        

    def pulseGetPlotFormat(self):
        pulseAx.set_ylim([0, 150])                              # Set Y axis limit of plot
        pulseAx.set_title("Arduino Pulse Data")                        # Set title of figure
        pulseAx.set_ylabel("Pulse")  
                                   # Set title of y axis

                            
tempDataList = []      
                                   # Create empty list variable for later use
                                                        
fig = plt.figure()  
                                    # Create Matplotlib plots fig is the 'higher level' plot window
ax = fig.add_subplot(111)           # Add subplot to main fig window

inputTransmit = serial.Serial("/dev/cu.usbmodem101", 115200)          # Establish Serial object with COM port and BAUD rate to match Arduino Port/rate

time.sleep(2)                                                         # Time delay for Arduino Serial initialization 
realTimePlot = AnimationPlot()


                                                                    # Matplotlib Animation Fuction that takes takes care of real time plot.
                                                                     # Note that 'fargs' parameter is where we pass in our dataList and Serial object. 
ani = animation.FuncAnimation(fig, realTimePlot.animate, frames=100, fargs=(tempDataList, inputTransmit), interval=100) 


#####SAME THING FOR PULSE PLOT
pulseDataList = []      
                                                                          
fig = plt.figure()  
   
pulseAx = fig.add_subplot(111)                           # Add subplot to main fig window


time.sleep(2)                                           # Time delay for Arduino Serial initialization 


pulseRealTimePlot = AnimationPlot()
                                                        # Matplotlib Animation Fuction that takes takes care of real time plot.
                                                        # Note that 'fargs' parameter is where we pass in our dataList and Serial object. 
pulseAni = animation.FuncAnimation(fig, pulseRealTimePlot.pulseAnimate, frames=100, fargs=(pulseDataList, inputTransmit), interval=100) 

plt.show()                                        
inputTransmit.close()   