---
title: "Coding the Thermometer"
date: 2022-07-12T00:24:01+02:00
categories: ["raspberry"]
---
In this post, I will describe the code I have developed to run the thermometer, 
log the data and save it in such a way that it can be used to carry out some 
(limited) analytics. At this point, the thermometer has already been installed 
<!-- and the libraries have been installed (check [Setting up the thermometer]("/content/posts/raspberry/setting-up-thermometer.md") -->
<!-- and the libraries have been installed (check [Setting up the thermometer]({{< ref "/content/posts/raspberry/setting-up-thermometer.md" >}})) -->

Part of the code I am showing here was taken from the 
[Ardumotive - How to use the DHT22](https://www.ardumotive.com/how-to-use-the-dht-22-en.html) 
I have already referenced. I then expanded on it to add some simple logging. 

### Libraries
To run the code, only three libraries are needed: the `Adafruit_DHT` library, 
<!-- which was installed in the [previous post]({{< ref "/content/posts/raspberry/setting-up-thermometer.md" >}}), the  -->
`time` library (for `sleep`), and the `datetime` library for better date/time
utilities. 

`sleep` is needed to slow down the program, so that the sensor is able to gather
the information (in fact, it cannot be accessed more than once every two seconds).

```python
# Library for reading from the DHT sensor
import Adafruit_DHT as dht
from time import sleep
from datetime import datetime as dt
```

### The main loop
The main loop of the progam features a `while True` loop, which will let the program 
run until it gets interrupted by the user. As soon as the program runs, the log file
is opened in append mode, so that it is possible to add more lines without deleting 
previous readings (this is pretty useful when debugging!). The value of `DHT_data` 
is set to be the pin that is connected to the DATA output of the DHT22 sensor. 

Next, the while loop is executed. In each iteration of the loop, the timestamp of the
iteration is saved in `now`, then the sensor is read. The values of temperature
and humidity are printed on screen, then put together with the timestamp in 
variable `data_line` and added to the log file. 

The loop is wrapped in a `try`-`except` block, so that it is possible to interrupt it 
"gracefully" using Ctrl+C. When this happens, the log file is closed and the program
terminates. 

```python
#Set DATA pin (this is the pin I will be connecting the DATA output of the chip to)
DHT_data = 4 

# Open the log file in append mode, so that previous readings will not be deleted 
# when the program restarts.
fw = open('log.txt', 'a')

try: 
    # Run forever, until the program is killed through Ctrl+C
    while True:
        # Getting timestamp for the current measurement
        now = dt.now()
        # Reading Humidity and Temperature from DHT22
        h,t = dht.read_retry(dht.DHT22, DHT_data)

        # Print Temperature and Humidity on Shell window
        print('Time={0}\tTemp={1:0.1f}*C\tHumidity={2:0.1f}%'.format(now, t, h))

        # Preparing the datetime object for logging, splitting date and time for convenience.
        this_date = now.date()
        this_time = now.time()
        # Writing the data in CSV format.
        data_line = "{},{},{},{}\n".format(this_date, this_time, t,h)
        fw.write(data_line)

        sleep(30) #Wait 30 seconds and read again

except KeyboardInterrupt:
    fw.close()
    print('Ending the program.')
```

When all is said and done, this is a possible output of the program:
```
Time=2022-07-12 00:57:15.430657 Temp=25.0*C     Humidity=58.2%
Time=2022-07-12 00:57:56.118202 Temp=25.0*C     Humidity=58.3%
Time=2022-07-12 00:58:29.214395 Temp=25.0*C     Humidity=58.3%
Time=2022-07-12 00:58:59.776892 Temp=25.0*C     Humidity=58.5%
Time=2022-07-12 00:59:30.340131 Temp=25.1*C     Humidity=58.5%
Time=2022-07-12 01:00:13.552538 Temp=25.1*C     Humidity=58.3%
Time=2022-07-12 01:00:46.646864 Temp=25.1*C     Humidity=58.4%
Time=2022-07-12 01:01:17.210069 Temp=25.1*C     Humidity=58.4%
Time=2022-07-12 01:01:52.816956 Temp=25.1*C     Humidity=58.5%
```

Note that there is a bug in the line 
```
print('Time={0}\tTemp={1:0.1f}*C\tHumidity={2:0.1f}%'.format(now, t, h))
```
which is caused by the temperature sensor returning invalid data: this raises
an exception in the `print` function and interrupts the program. I was not able
to reproduce it (after admittedly not a lot of testing) to add a fix, but a simple
solution to the problem is simply deleting the offending line. At least, until I
figure out a fix. 

So there we go! This is how it is possible to code a simple log of temperature 
and humidity by using a Raspberry Pi and a DHT22 sensor. In a future post, I will
be play around with some data visualisation and plot the temperature and humidity
over time. 

Thanks for reading!