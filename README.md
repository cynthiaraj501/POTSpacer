# POTSpacer


The POTS (Postural Orthostatic Tachycardia Syndrome) Pacer is a wearable technology device that warns individuals of an oncoming POTS "attack," which is characterized by fainting, light-headedness, etc. The device constantly monitors pulse and body temperature data; upon detecting an abnormal increase in these vital signs, the device vibrates in order to alert the individual so that they can proceed safely and prevent injury. Users can also access their real-time data and view it in a graphical format. This data will be stored in a database for table display on an app as well.
We built our project using a number of different, yet somewhat unfamiliar, technologies. We used C++ in the Arduino IDE to enable data collection from a temperature sensor and a pulse sensor. We also attached a small vibration motor for the alert feature of our device (it vibrates before a POTS "attack" to alert users). We then wrote Python scripts to receive and display the data on animated graphs so that the user can visualize their results. Finally, we used Firebase to store data that can be dynamically updated; Swift was used to create an app that would display this data for the user.

We used C++ in the Arduino IDE to handle data collection and processing with an Arduino Uno. We also used Python to create the real-time graphical displays with output from the Arduino. Finally, we used Swift to create an app table view display of data stored in Firebase.
We would like to connect our real-time data to Firebase in order to display our data analysis in the app we've created.
